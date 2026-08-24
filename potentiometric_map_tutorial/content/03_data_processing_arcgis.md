# Data Processing: Preparation in ArcGIS

## Overview

After extracting groundwater data from GGIS, the next step is to process and prepare the data in ArcGIS for spatial analysis. This section covers loading data, organizing layers, and preparing for interpolation.

## Setting Up ArcGIS Project

### Create New Project

1. Launch **ArcGIS Pro**
2. Create a new project:
   - Click **"New"** → **"Project"**
   - Choose project location and name
   - Select appropriate coordinate system (typically WGS84/EPSG:4326 for initial work)

## Adding Vector Layers

### Import Well Data

1. Navigate to: **Map** → **Add** → **Add Data**
2. Locate your downloaded well data (.csv or shapefile)
3. Add the wells layer to your project
4. The wells should display as point features on your map

### Import Boundary Shapefile

1. Extract the `catawba_river_basin.rar` archive
2. Add `boundaries_catawba.shp` to your project:
   - **Map** → **Add** → **Add Data**
   - Select `boundaries_catawba.shp`
3. This creates the analysis boundary polygon

### Import DEM (Digital Elevation Model)

1. Obtain a DEM for your study area (e.g., USGS 30m DEM)
2. Add the DEM raster layer to your project
3. The DEM will be used for:
   - Reference elevation values
   - Spatial interpolation extent
   - Final map aesthetics

## Coordinate System Configuration

### Verify and Set Projection

1. Ensure all working vector layers are projected to the **same coordinate system**
   - Recommended: **WGS84 (EPSG:4326)** or local UTM zone
   - All layers MUST be in the same projection before interpolation

2. Check layer properties:
   - Right-click layer → **Properties**
   - Verify **Spatial Reference**
   - If needed, reproject using:
     - **Data Management Tools** → **Projections and Transformations** → **Project**

## Filtering Wells

### Assess Well Data Quality

1. Open the **Attribute Table** for your wells layer:
   - Right-click on wells layer → **Attribute Table**
2. Review the data structure:
   - Well ID
   - Latitude, Longitude
   - Surface elevation
   - Water depth measurements

### Remove Poor Quality Data

Filter and remove wells that have:

- Missing coordinates
- Invalid elevation values
- Insufficient water depth data
- Wells outside your study area boundary
- Duplicate records

### Selection by Location

1. Use **Select by Location** to keep only wells within your study boundary:
   - **Analysis** → **Select** → **Select by Location**
   - Select wells contained within the basin boundary polygon
   - Export selected wells to a new layer: `pocos_mde` (wells with DEM)

### Create Working Layer

Export filtered wells as a new shapefile:
- Name: `pocos_mde` (Portuguese: "poços com DEM" = wells with DEM)
- This layer will be used for all subsequent interpolation steps

## Data Preparation Checklist

- ✓ All layers in same coordinate system
- ✓ Wells layer contains valid coordinates
- ✓ Surface elevation values verified
- ✓ Water depth data quality checked
- ✓ Boundary polygon valid
- ✓ DEM aligned with vector layers
- ✓ Filtered wells exported to working layer
