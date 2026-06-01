\
from __future__ import annotations

from pathlib import Path
from typing import List

import geopandas as gpd
import pandas as pd
import requests
from owslib.wfs import WebFeatureService


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def discover_wfs_layers(capabilities_url: str) -> List[str]:
    """
    Return the available layer names from a WFS GetCapabilities endpoint.
    """
    last_error = None
    for version in ("2.0.0", "1.1.0", "1.0.0"):
        try:
            wfs = WebFeatureService(url=capabilities_url, version=version)
            return list(wfs.contents.keys())
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f"Could not read WFS capabilities: {last_error}")


def load_wfs_layer(capabilities_url: str, layer_name: str, crs: str | None = None) -> gpd.GeoDataFrame:
    """
    Download a WFS layer directly into a GeoDataFrame.
    """
    last_error = None
    for version in ("2.0.0", "1.1.0", "1.0.0"):
        try:
            wfs = WebFeatureService(url=capabilities_url, version=version)
            response = wfs.getfeature(typename=[layer_name])
            gdf = gpd.read_file(response)
            if crs and gdf.crs is not None and str(gdf.crs) != crs:
                gdf = gdf.to_crs(crs)
            return gdf
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f"Could not load WFS layer '{layer_name}': {last_error}")


def download_csv(url: str, output_path: Path, **read_csv_kwargs) -> pd.DataFrame:
    """
    Download a CSV to disk and return a DataFrame.
    """
    ensure_parent(output_path)
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    output_path.write_bytes(resp.content)
    return pd.read_csv(output_path, **read_csv_kwargs)


def save_geodataframe(gdf: gpd.GeoDataFrame, output_path: Path) -> None:
    """
    Save geospatial data in a portable format.
    """
    ensure_parent(output_path)
    suffix = output_path.suffix.lower()
    if suffix in (".gpkg", ".geojson", ".json", ".shp"):
        gdf.to_file(output_path)
    else:
        raise ValueError(f"Unsupported geospatial output format: {suffix}")


def save_dataframe(df: pd.DataFrame, output_path: Path) -> None:
    ensure_parent(output_path)
    df.to_csv(output_path, index=False)
