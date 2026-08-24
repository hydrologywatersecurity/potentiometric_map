# Data Collection: Extracting Data from GGIS

## Overview

The **GGIS (Geological and Groundwater Information System)** provides an interactive web map interface for accessing groundwater data. This section walks you through the data extraction process for your study area.

## Step-by-Step Guide

### Step 1: Access GGIS Web Map Interface

1. Open your web browser and navigate to the GGIS interactive map
2. Familiarize yourself with the interface:
   - Map display in the center
   - Data visualization menu on the right panel
   - Zoom and pan controls
   - Layer toggle options

### Step 2: Select Your Study Area

1. In the **right menu**, click on **"Select Well"**
2. Select **"Polygon"** tool
3. Define your area of interest by:
   - Creating a polygon boundary around your study area
   - For this tutorial, select the **Catawba River Basin** area
   - Double-click to finish the polygon
4. The right panel will display available wells within your selection

### Step 3: Download Data

1. Locate the **download button** in the right panel
2. Click the download button to proceed

### Step 4: Complete Registration

The download page requires your information:

- Email address
- Professional background
- Type of organization
- Country of residence
- Any other requested metadata

Fill out all fields accurately and click **"Download"**

### Step 5: Obtain Downloaded Files

After file generation, download the **.zip archive** which contains:

- **Timeseries data**: Water level measurements over time for each well
- **Well metadata**:
  - Well identifiers (IDs)
  - Coordinates (latitude, longitude)
  - Surface elevation
  - Data origin information
  - Aquifer classification (confined or unconfined)

## Supplementary Data

### Shapefile Boundaries

Additional boundary files support the analysis:

**catawba_river_basin.rar** - Contains:
- `boundaries_catawba.shp` - Shapefile delineating the Catawba River Basin boundary
- Associated files (.shx, .dbf, .prj)

These shapefiles are essential for clipping and constraining your final analysis to the study area boundary.

## Data Quality Considerations

### Verification Steps

1. Check coordinate systems match (typically WGS84 or local projection)
2. Verify elevation values are reasonable for your region
3. Examine temporal coverage and data gaps
4. Validate well classifications (confined vs. unconfined)
5. Remove duplicate or corrupted records

### Common Issues

- **Missing coordinates**: Remove wells without location data
- **Unrealistic elevations**: Verify against DEM data
- **Data gaps**: Document temporal coverage
- **Coordinate errors**: Compare with reference maps
