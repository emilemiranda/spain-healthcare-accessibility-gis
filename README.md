# Mapping Healthcare Access Inequality in Spain: A GIS Vulnerability Index for Ageing Municipalities

## Project overview
A GIS project that maps municipal-level inequality in healthcare access by combining ageing population pressure, service proximity, and spatial statistics.

## Why it matters
Older adults are often most exposed to long travel distances, sparse service coverage, and uneven public-service distribution. This project identifies where those gaps are most concentrated.

## Data sources & attribution
- **IGN / CNIG** — municipal boundaries for Spain
- **INE** — population by sex and age
- **Generalitat Valenciana / Conselleria de Sanitat** — hospitals and health centers
- **Open Data Euskadi** — socio-sanitary resources

## Methodology
```text
Official GIS + demographic data
        ↓
Clean geometries and CRS
        ↓
Build 65+ population indicator
        ↓
Measure distance to services
        ↓
Create vulnerability index
        ↓
Run Moran’s I / hotspot analysis
        ↓
Export maps + rankings + interactive outputs
```

## Key outputs
- PNG choropleth map
- Interactive HTML map
- Top 20 vulnerable municipalities CSV
- GeoPackage with the final analysis layer

## Three findings
1. The vulnerability pattern is strongly clustered, not random.
2. Urban and island municipalities appear repeatedly in the highest-risk group.
3. Ageing pressure and access gaps overlap in the same places.

## Tech stack
Python, GeoPandas, Pandas, PySAL, Folium, Matplotlib, Contextily

## How to run
1. Create a virtual environment
2. Install requirements
3. Run notebooks in order:
   - 01 Data Discovery
   - 02 Download Raw Data
   - 03 Clean and Standardize
   - 04 Join Data and Build Indicators
   - 05 Hotspot Analysis and Maps

## Best recommendations
- Add travel-time analysis with road networks instead of straight-line distance
- Split the analysis by region to compare mainland vs island patterns
- Build a small dashboard or web map
- Add a time-series version of the index
- Pair the PNG summary graphic with the interactive HTML map
