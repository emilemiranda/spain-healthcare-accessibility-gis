from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = DATA_DIR / "outputs"

# Official portal sources
BOUNDARIES_WFS = "https://www.ign.es/wfs-inspire/unidades-administrativas?REQUEST=GetCapabilities&SERVICE=WFS&VERSION=2.0.0"
HEALTH_WFS = "http://www.sigmayores.csic.es/ArcGIS/services/Rec-Sanitarios/MapServer/WFSServer?REQUEST=GetCapabilities"
SOCIAL_WFS = "http://www.sigmayores.csic.es/ArcGIS/services/Rec-Sociales/MapServer/WFSServer?REQUEST=GetCapabilities"
POPULATION_CSV = "https://www.ine.es/jaxi/files/tpx/csv_bdsc/56961.csv"

# Analysis settings
METRIC_CRS = "EPSG:3035"
MAP_CRS = "EPSG:3857"
GEOGRAPHIC_CRS = "EPSG:4326"

# Replace these after inspecting layer names and columns in Notebook 1.
BOUNDARY_LAYER = None
HEALTH_LAYER = None
SOCIAL_LAYER = None

# Replace these after inspecting columns in the raw data.
MUNICIPALITY_CODE_COL = None
MUNICIPALITY_NAME_COL = None
TOTAL_POP_COL = None  # optional
