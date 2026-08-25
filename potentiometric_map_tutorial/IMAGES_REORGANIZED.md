# Tutorial Images - Reorganized Structure

## Overview

All **40 figures** have been reorganized with descriptive names that correspond to the tutorial content structure. Each image is now named to clearly indicate its section and purpose.

## Image Organization by Section

### 1. Fundamentals (Figures 1-3)
- **01_objective_title.png** - Course title and learning objectives
- **02_study_area_catawba.png** - Catawba River Basin location map
- **03_groundwater_concept.png** - Groundwater concepts diagram

### 2. Data Collection: GGIS (Figures 4-11)
- **04_ggis_interface_map.png** - GGIS web map interface showing well locations
- **05_ggis_select_polygon.png** - Polygon selection tool in right panel
- **06_ggis_download_button.png** - Download button location and step
- **07_ggis_registration_form.png** - Data download registration form
- **08_ggis_file_ready.png** - File ready confirmation screen
- **09_ggis_metadata.png** - Downloaded metadata display
- **10_usgs_alternative_nc.png** - USGS North Carolina data portal
- **11_usgs_monitoring_map.png** - USGS HUC8 basin selection map

### 3. Data Processing: Excel Filtering (Figures 12-19)
- **12_excel_well_data.png** - Excel spreadsheet with well data columns
- **13_excel_filter_tool.png** - Excel filter tool applied to data
- **14_excel_missing_data.png** - Identifying rows with missing values
- **15_excel_vlookup_setup.png** - VLOOKUP formula for matching IDs
- **16_excel_hydrogeology_tab.png** - Well.ods Hydrogeology worksheet
- **17_excel_confinement_status.png** - Confined/Unconfined status column
- **18_excel_paste_special.png** - Paste Special dialog (formulas to values)
- **19_excel_final_dataset.png** - Final cleaned dataset with unconfined wells only

### 4. ArcGIS: Loading Data (Figures 20-27)
- **20_arcgis_add_data_menu.png** - Map menu → Add Data option
- **21_arcgis_browse_dialog.png** - Browse file selection dialog
- **22_arcgis_csv_selection.png** - CSV file selection from working directory
- **23_arcgis_create_points_menu.png** - Create Points From Table context menu
- **24_arcgis_xy_table_dialog.png** - XY Table to Points configuration dialog
- **25_arcgis_coordinate_system.png** - WGS84 coordinate system selection
- **26_arcgis_wells_map.png** - Well points displayed on map
- **27_arcgis_boundary_added.png** - Catawba River Basin boundary polygon added

### 5. Water Table Calculation (Figures 28-32)
- **28_arcgis_attribute_table.png** - Attribute Table showing well data
- **29_arcgis_add_field.png** - Add Field dialog
- **30_arcgis_field_calculator.png** - Field Calculator toolbar
- **31_arcgis_expression_builder.png** - Expression Builder with formula
- **32_arcgis_calculated_values.png** - Calculated hydraulic head values

### 6. Spatial Interpolation: TPS & IDW (Figures 33-39)
- **33_arcgis_analysis_tools.png** - Analysis tab with Tools ribbon
- **34_arcgis_ebk_dialog.png** - Empirical Bayesian Kriging dialog
- **35_arcgis_tps_interpolation.png** - TPS interpolation result (smooth surface)
- **36_arcgis_symbology_classes.png** - Symbology classification panel
- **37_arcgis_tps_result_colored.png** - Styled TPS surface with Turbo colors
- **38_arcgis_idw_dialog.png** - IDW interpolation geoprocessing dialog
- **39_arcgis_idw_result.png** - IDW result showing local peaks

### 7. Clipping & Finalization (Figure 40)
- **40_arcgis_extract_by_mask.png** - Extract by Mask tool for clipping raster

## Format Information

- **Format:** PNG (lossless compression)
- **Total Size:** ~14.4 MB
- **Average Size:** 360 KB per figure
- **Resolution:** High quality for web display and printing

## Usage in Markdown

### Basic Syntax
```markdown
![Description](../assets/images/XX_name.png)
```

### Recommended: Captioned Figures (MyST Syntax)
```markdown
:::{figure} ../assets/images/XX_name.png
:alt: Accessibility description
:width: 600px

**Figure 1:** Figure caption explaining the content and relevance.
:::
```

## Implementation Notes

- All image paths use relative references (`../assets/images/`)
- Images are integrated into content sections in logical order
- Each figure includes descriptive alt-text for accessibility
- Caption format: `**Figure X:** [Description]`
- Images are 600px width for optimal web rendering

## Deployment

When deployed to GitHub Pages:
- Base URL: `https://hydrologywatersecurity.github.io/potentiometric_map/`
- Images served from: `.../assets/images/`
- All relative paths automatically resolve correctly

## Accessibility Checklist

- ✓ All images include descriptive alt-text
- ✓ Figures have numbered captions
- ✓ Captions explain content and significance
- ✓ Images are named with descriptive terms
- ✓ Image quality preserved for readability
