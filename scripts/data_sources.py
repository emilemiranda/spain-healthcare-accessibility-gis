from dataclasses import dataclass

@dataclass(frozen=True)
class Source:
    name: str
    url: str
    kind: str
    notes: str = ""

SOURCES = [
    Source(
        name="Administrative boundaries of Spain",
        url="https://www.ign.es/wfs-inspire/unidades-administrativas?REQUEST=GetCapabilities&SERVICE=WFS&VERSION=2.0.0",
        kind="WFS",
        notes="Municipal, provincial, and regional boundaries."
    ),
    Source(
        name="Healthcare resources",
        url="http://www.sigmayores.csic.es/ArcGIS/services/Rec-Sanitarios/MapServer/WFSServer?REQUEST=GetCapabilities",
        kind="WFS",
        notes="Hospitals, health centers, and consultorios."
    ),
    Source(
        name="Social resources",
        url="http://www.sigmayores.csic.es/ArcGIS/services/Rec-Sociales/MapServer/WFSServer?REQUEST=GetCapabilities",
        kind="WFS",
        notes="Social resources for older people."
    ),
    Source(
        name="Population by sex and age",
        url="https://www.ine.es/jaxi/files/tpx/csv_bdsc/56961.csv",
        kind="CSV",
        notes="Municipality population by age."
    ),
]
