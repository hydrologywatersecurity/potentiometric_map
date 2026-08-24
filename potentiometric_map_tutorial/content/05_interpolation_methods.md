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

#### Step 1: Open Processing Toolbox

1. In ArcGIS (via QGIS bridge or direct tool):
   - Press **Ctrl + Alt + T**
   - Or navigate: **Processing** → **Toolbox**

#### Step 2: Navigate to Interpolation Tool

1. Expand the tool hierarchy:
   - **SAGA** → **Raster - Spline Interpolation** → **Thin Plate Spline**

#### Step 3: Configure Parameters

Set the following parameters:

| Parameter | Value | Notes |
|---|---|---|
| **Points** | `pocos_mde` | Your filtered wells layer |
| **Attribute** | `na_freatic` | The water table elevation field |
| **Output extent** | Calculate from Layer → `dem` | Use DEM as reference extent |
| **Cellsize** | 0.001 | Fine resolution (about 100m at equator) |
| **Minimum points** | 1 | Allow interpolation with 1 point nearby |
| **Target Grid** | `na_freatic_interpolado_TPS.sdat` | Output file name and format |

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
- Native QGIS tools
- Faster computation
- Good for validation

### Implementation Steps

#### Step 1: Access IDW Tool

1. Open **Processing Toolbox** (Ctrl + Alt + T)
2. Search for: **"IDW Interpolation"**
3. Select the QGIS native IDW tool

#### Step 2: Configure Parameters

- **Input layer**: `pocos_mde`
- **Interpolation attribute**: `na_freatic`
- **Distance coefficient**: 2 (standard)
- **Extent**: Set to `dem` layer
- **Output resolution**: 0.001 degrees (same as TPS)
- **Output file**: `superficie_interpolada_IDW.tif`

#### Step 3: Execute and Style

1. Click **Run**
2. Apply similar styling (Turbo color ramp, linear gradient)

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
