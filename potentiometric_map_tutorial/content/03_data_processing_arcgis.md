# Data Processing: Preparation in ArcGIS

## Overview

After extracting groundwater data from GGIS, the next step is to process and prepare the data in ArcGIS for spatial analysis. This section covers loading data, organizing layers, and preparing for interpolation.

## Excel Data Filtering

### Prepare Your Dataset

:::{figure} ../assets/images/12_excel_well_data.png
:alt: Excel spreadsheet with well data columns
:width: 600px

**Figure 1:** Well data in Excel showing ID, coordinates, elevation, and water depth.
:::

:::{figure} ../assets/images/13_excel_filter_tool.png
:alt: Excel filter tool applied to well data
:width: 600px

**Figure 2:** Apply Excel Filter tool to identify and remove wells with missing data.
:::

:::{figure} ../assets/images/14_excel_missing_data.png
:alt: Excel showing rows with missing elevation or water depth values
:width: 600px

**Figure 3:** Identify and remove wells lacking elevation or water depth information.
:::

### Filter Unconfined Wells

:::{figure} ../assets/images/15_excel_vlookup_setup.png
:alt: Excel VLOOKUP formula for matching well IDs
:width: 600px

**Figure 4:** Use VLOOKUP formula to match well IDs between datasets.
:::

:::{figure} ../assets/images/16_excel_hydrogeology_tab.png
:alt: Excel well.ods Hydrogeology worksheet
:width: 600px

**Figure 5:** Access the Hydrogeology tab in well.ods file for aquifer type information.
:::

:::{figure} ../assets/images/17_excel_confinement_status.png
:alt: Excel showing confinement status column with Confined/Unconfined values
:width: 600px

**Figure 6:** Retrieved confinement status for each well using VLOOKUP.
:::

:::{figure} ../assets/images/18_excel_paste_special.png
:alt: Excel Paste Special dialog for converting formulas to values
:width: 600px

**Figure 7:** Use Paste Special → Values to convert formulas to permanent data.
:::

:::{figure} ../assets/images/19_excel_final_dataset.png
:alt: Excel final cleaned dataset with only unconfined wells
:width: 600px

**Figure 8:** Final cleaned dataset containing only unconfined wells with complete data.
:::

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

:::{figure} ../assets/images/20_arcgis_add_data_menu.png
:alt: ArcGIS Map menu showing Add Data option
:width: 600px

**Figure 9:** Access the Add Data option through the Map menu.
:::

:::{figure} ../assets/images/21_arcgis_browse_dialog.png
:alt: ArcGIS Browse dialog for file selection
:width: 600px

**Figure 10:** Browse to select your well data CSV file.
:::

:::{figure} ../assets/images/22_arcgis_csv_selection.png
:alt: ArcGIS file browser showing CSV and shapefile options
:width: 600px

**Figure 11:** Select your cleaned well data file from the working directory.
:::

### Create Points from Table

1. Right-click on the table in Contents panel
2. Select: **Create Points From Table** → **XY Table To Points**
3. Configure the dialog:
   - X Field: longitude
   - Y Field: latitude  
   - Z Field: elevation (optional)
   - Coordinate System: WGS84 (EPSG:4326)

:::{figure} ../assets/images/23_arcgis_create_points_menu.png
:alt: ArcGIS Create Points From Table context menu
:width: 600px

**Figure 12:** Right-click table and select Create Points From Table option.
:::

:::{figure} ../assets/images/24_arcgis_xy_table_dialog.png
:alt: ArcGIS XY Table to Points configuration dialog
:width: 600px

**Figure 13:** Configure X, Y, and Z fields for point creation.
:::

:::{figure} ../assets/images/25_arcgis_coordinate_system.png
:alt: ArcGIS coordinate system selection (WGS84)
:width: 600px

**Figure 14:** Select WGS84 as the coordinate system for all working layers.
:::

### Import Boundary Shapefile

1. Extract the `catawba_river_basin.rar` archive
2. Add `boundaries_catawba.shp` to your project:
   - **Map** → **Add** → **Add Data**
   - Select `boundaries_catawba.shp`
3. This creates the analysis boundary polygon

:::{figure} ../assets/images/26_arcgis_wells_map.png
:alt: ArcGIS map showing well points added to project
:width: 600px

**Figure 15:** Wells points now displayed on the map.
:::

:::{figure} ../assets/images/27_arcgis_boundary_added.png
:alt: ArcGIS map showing wells and Catawba River Basin boundary polygon
:width: 600px

**Figure 16:** Catawba River Basin boundary added for reference and analysis constraint.
:::

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
