\
from __future__ import annotations

from pathlib import Path
import geopandas as gpd
import pandas as pd


def export_geodataframe(gdf: gpd.GeoDataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() in {".gpkg", ".geojson", ".json"}:
        gdf.to_file(output_path)
    else:
        raise ValueError(f"Unsupported geospatial format: {output_path.suffix}")


def export_dataframe(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
