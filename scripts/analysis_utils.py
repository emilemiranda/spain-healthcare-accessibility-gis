\
from __future__ import annotations

import geopandas as gpd
import pandas as pd
from scipy.stats import zscore
from libpysal.weights import Queen
from esda.moran import Moran
from esda.getisord import G_Local


def standardize_geodataframes(*gdfs: gpd.GeoDataFrame, crs: str) -> list[gpd.GeoDataFrame]:
    cleaned = []
    for gdf in gdfs:
        obj = gdf.copy()
        if obj.crs is None:
            raise ValueError("Input GeoDataFrame has no CRS defined.")
        obj = obj.to_crs(crs)
        obj = obj[obj.geometry.notna()].copy()
        obj = obj[obj.is_valid].copy()
        cleaned.append(obj)
    return cleaned


def build_vulnerability_index(
    gdf: gpd.GeoDataFrame,
    aging_col: str,
    dist_health_col: str,
    dist_social_col: str,
    service_count_col: str,
) -> gpd.GeoDataFrame:
    out = gdf.copy()
    out["z_aging"] = zscore(out[aging_col].fillna(0))
    out["z_dist_health"] = zscore(out[dist_health_col].fillna(0))
    out["z_dist_social"] = zscore(out[dist_social_col].fillna(0))
    out["z_service_density"] = zscore(out[service_count_col].fillna(0))
    out["vulnerability_index"] = (
        out["z_aging"] + out["z_dist_health"] + out["z_dist_social"] - out["z_service_density"]
    )
    return out


def spatial_autocorrelation(gdf: gpd.GeoDataFrame, value_col: str):
    w = Queen.from_dataframe(gdf)
    w.transform = "R"
    values = gdf[value_col].fillna(0)
    moran = Moran(values, w)
    g_local = G_Local(values, w)
    out = gdf.copy()
    out["hotspot_z"] = g_local.Zs
    out["hotspot_p"] = g_local.p_sim
    return out, w, moran, g_local


def top_ranked(gdf: gpd.GeoDataFrame, value_col: str, n: int = 20) -> pd.DataFrame:
    cols = [c for c in gdf.columns if c != "geometry"]
    return gdf[cols].sort_values(value_col, ascending=False).head(n)
