\
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd


def save_choropleth(
    gdf: gpd.GeoDataFrame,
    column: str,
    output_path: Path,
    title: str,
    cmap: str = "Reds",
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plot_gdf = gdf.to_crs("EPSG:3857")
    fig, ax = plt.subplots(figsize=(12, 12))
    plot_gdf.plot(
        column=column,
        cmap=cmap,
        linewidth=0.1,
        edgecolor="black",
        legend=True,
        ax=ax,
        missing_kwds={"color": "lightgrey", "label": "Missing data"},
    )
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)
    ax.set_axis_off()
    ax.set_title(title, fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
