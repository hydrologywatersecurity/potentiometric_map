# Spatial Interpolation: Methods and Implementation

## Introduction to Interpolation

Spatial interpolation creates a continuous surface from discrete well point data. The goal is to estimate potentiometric head values at locations where measurements don't exist.

## Method Comparison: TPS vs. IDW

| Characteristic | Thin Plate Spline (TPS) | Inverse Distance Weighting (IDW) |
|---|---|---|
| **Smoothness** | Smooth, natural surface | More local variation |
| **Extrapolation** | Reasonable beyond data range | Conservative at edges |
| **Requirements** | Requires SAGA toolbox | Native QGIS functionality |
| **Data density sensitive** | Less sensitive | More sensitive |
| **Recommended** | ✓ Preferred for this tutorial | Alternative if SAGA unavailable |
| **Processing time** | Longer | Faster |
| **Quality** | Higher overall quality | Good for quick assessment |

## Option A: Thin Plate Spline (TPS) - Preferred Method

### Why TPS?

Thin Plate Spline interpolation is preferred because it:

- Produces smooth, natural-looking surfaces
- Handles scattered data well
- Provides reliable extrapolation
- Creates realistic potentiometric patterns
- Less influenced by local clustering
- Better for regional flow interpretation

### Implementation Steps

#### Step 1: Open Analysis Tools

1. In ArcGIS Pro:
   - Click the **Analysis** tab
   - Navigate through the **Tools**

:::{figure} ../assets/images/33_arcgis_analysis_tools.png
:alt: ArcGIS Analysis tab showing Tools ribbon
:width: 600px

**Figure 1:** Open the Analysis tab to access geoprocessing tools.
:::

#### Step 2: Navigate to Empirical Bayesian Kriging

1. Expand the tool hierarchy:
   - **Analysis** → **Tools**
   - Find **Empirical Bayesian Kriging**
   - This tool performs TPS interpolation via SAGA backend

:::{figure} ../assets/images/34_arcgis_ebk_dialog.png
:alt: ArcGIS Empirical Bayesian Kriging geoprocessing dialog
:width: 600px

**Figure 2:** Geoprocessing panel showing Empirical Bayesian Kriging parameters.
:::

#### Step 3: Configure Parameters

Set the following parameters:

| Parameter | Value | Notes |
|---|---|---|
| **Input Features** | `catawba_basin_wells_filtered_XYTabletoPoints` | Your filtered wells layer |
| **Z Value Field** | `water_table_head` | The water table elevation field |
| **Output Geostatistical Layer** | `TPS_interpolation` | Output layer name |
| **Output Cell Size** | 1.0E-02 (0.01 degrees) | Fine resolution |
| **Semivariogram Model Type** | **Thin plate spline** | Essential for TPS method |

:::{figure} ../assets/images/35_arcgis_tps_interpolation.png
:alt: ArcGIS TPS interpolation result showing colored surface
:width: 600px

**Figure 3:** TPS interpolation result displaying smooth potentiometric surface.
:::

#### Step 4: Style the Result

1. Right-click the output raster layer
2. Apply visualization styling:
   - **Symbology** → **Raster**
   - Select **Continuous Color Ramp**
   - Recommended: **Turbo** color scheme
   - Set rendering to **Linear** gradient

:::{figure} ../assets/images/36_arcgis_symbology_classes.png
:alt: ArcGIS Symbology panel showing classification options
:width: 600px

**Figure 4:** Configure symbology with geometric interval classification.
:::

:::{figure} ../assets/images/37_arcgis_tps_result_colored.png
:alt: ArcGIS TPS result with Turbo color ramp applied
:width: 600px

**Figure 5:** Final styled TPS surface with color classification.
:::

### Key Parameter Explanations

**Cell Size (0.001 degrees):**
- At equator ≈ 111 meters
- Provides detail without excessive processing
- Adjust based on data density and region size

**Minimum Points (1):**
- Allows extrapolation in data-sparse areas
- Ensures complete coverage
- TPS handles edge cases well with smooth transitions

#### Step 4: Execute Interpolation

1. Click **Run** button
2. Monitor progress bar
3. Wait for completion (time varies by extent and data size)

#### Step 5: Style the Result

1. Open the output raster layer `na_freatic_interpolado_TPS.sdat`
2. Apply visualization styling:
   - **Symbology** → **Raster**
   - Select **Continuous Color Ramp**
   - Recommended: **Turbo** color scheme
   - Set rendering to **Linear** gradient
   - Adjust transparency if needed

The styled raster now displays your interpolated potentiometric surface!

## Option B: Inverse Distance Weighting (IDW) - Alternative Method

### When to Use IDW

Use IDW if SAGA is unavailable or for quick analysis:

- Simpler workflow
- Native ArcGIS tools
- Faster computation
- Good for validation

### Implementation Steps

#### Step 1: Access IDW Tool

1. Open **Analysis** → **Tools**
2. Search for: **"IDW"**
3. Select **Inverse Distance Weighted** interpolation tool

:::{figure} ../assets/images/38_arcgis_idw_dialog.png
:alt: ArcGIS IDW interpolation geoprocessing dialog
:width: 600px

**Figure 6:** IDW tool geoprocessing panel with parameters.
:::

#### Step 2: Configure Parameters

- **Input Features**: `catawba_basin_wells_filtered_XYTabletoPoints`
- **Z Value Field**: `water_table_head`
- **Output Geostatistical Layer**: `IDW_interpolation`
- **Cell Size**: 1E-02 (same as TPS)
- **Power**: 2 (standard for IDW)

#### Step 3: Execute and Style

:::{figure} ../assets/images/39_arcgis_idw_result.png
:alt: ArcGIS IDW result showing interpolated surface
:width: 600px

**Figure 7:** IDW interpolation result (note local peaks typical of IDW method).
:::

## Quality Assessment

### Verify Interpolation Results

1. **Visual inspection:**
   - Does the surface look smooth and realistic?
   - Are patterns consistent with expected flow?
   - Any unrealistic artifacts or bullseye patterns?

2. **Statistical validation:**
   - Compare interpolated values at well locations to original data
   - Calculate RMS error if cross-validation available
   - Check for reasonable minimum/maximum values

3. **Comparison with source data:**
   - Overlay well points on surface
   - Values should align with point locations
   - No sharp discontinuities at points

## Output Files

### TPS Result
- **File**: `na_freatic_interpolado_TPS.sdat` (SAGA format)
- **Use**: Preferred for final potentiometric map

### IDW Result
- **File**: `superficie_interpolada_IDW.tif` (GeoTIFF format)
- **Use**: Alternative if TPS unavailable

Both can be converted to common formats (GeoTIFF, ASCII) for sharing or further analysis.
