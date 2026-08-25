# Extracting Equipotential Contours

## Concept: Equipotential Lines

**Equipotential lines** (or contours) connect points of equal hydraulic head. They represent the potentiometric surface in 2D map form and are essential for:

- Visualizing groundwater flow patterns
- Identifying flow direction (perpendicular to contours)
- Determining gradient magnitude
- Assessing regional hydrogeology
- Creating professional maps

## Generating Contour Lines from Raster

### Clipping to Aquifer Boundary

Before extracting contours, clip the interpolated raster to your study area:

:::{figure} ../assets/images/40_arcgis_extract_by_mask.png
:alt: ArcGIS Extract by Mask geoprocessing dialog
:width: 600px

**Figure 1:** Use Extract by Mask to clip the TPS raster to the Catawba River Basin boundary.
:::

1. Navigate to: **Analysis** → **Tools** → **Extract by Mask**
2. Configure:
   - **Input Raster**: `TPS_interpolation`
   - **Input Mask**: `catawba_river_basin_boundary`
   - **Output Raster**: `TPS_mask`
3. Click **Run**

### Step 1: Open Contour Tool

In ArcGIS Pro:
1. Navigate to: **Analysis** → **Tools** → **Contours**
2. This tool converts your clipped raster to vector contour lines

### Step 2: Configure Contour Parameters

Set the following parameters:

| Parameter | Setting | Notes |
|---|---|---|
| **Input Raster** | `TPS_mask` | Your clipped interpolated surface |
| **Contour Interval** | 50 meters | Creates a contour every 50m elevation change |
| **Base Contour** | 0 | Starting elevation value |
| **Output Feature Class** | `Contour_TPS_mask1` | Output contour lines |

1. Access **Analysis** → **Tools** → **Contours**
2. Set interval to 50 meters for regional scale visualization
3. Click **Run**

### Choosing Contour Interval

**10 meters** is typical for:
- Regional scale analysis
- Clear visualization without clutter
- Standard hydrological practice

**Alternative intervals:**
- **5 meters**: More detailed but crowded on large areas
- **20 meters**: Simplified view, better for small-scale maps
- **25 meters**: Good for very large study areas

### Step 3: Execute Contour Extraction

1. Click **Run**
2. Monitor progress
3. Output shapefile created: `linhas_equipotenciais.shp`

## Styling and Visualization

### Step 4: Apply Symbology

1. Right-click layer → **Symbology**
2. Enable **Labels**:
   - **Labeling** → **Single Labels**
   - Label field: **ELEV**
   - Adjust label size/font for readability

3. Adjust line properties:
   - **Line Color**: Dark blue or black for clarity
   - **Line Weight**: 0.5-1.0 points (thin but visible)
   - **Line Style**: Solid (simple/default)

### Step 5: Fine-tuning Display

Optional enhancements:

- **Transparency**: Reduce to 70-80% for overlay visualization
- **Dashed lines**: Use every 50m for major contours, solid for minor
- **Label frequency**: Show every other contour to reduce clutter
- **Color gradient**: Alternatively, color contours by elevation value

## Interpretation of Equipotential Patterns

### Reading the Map

The contour pattern reveals:

**Contour spacing:**
- Close contours = Steep hydraulic gradient = Faster flow
- Wide contours = Gentle gradient = Slower flow

**Contour shape:**
- Concentric closures = Groundwater mounds (recharge areas)
- Smooth curves = Regional flow patterns
- Abrupt bends = Boundaries or flow obstacles

**Flow direction:**
- Perpendicular to contours (high to low elevation)
- Spacing indicates flow velocity
- Curvature indicates flow convergence/divergence

## Output Specifications

### Quality Attributes

The final equipotential contour layer should have:

✓ All contours properly labeled with elevation values  
✓ Clear, consistent line styling  
✓ Labels positioned for readability  
✓ No gaps or discontinuities  
✓ Proper coordinate system information  
✓ Valid attribute table with ELEV field

### Data Validation

Before proceeding to clipping:

1. **Check elevation range:**
   - Min and max values reasonable?
   - Consistent with DEM data?

2. **Examine spacing:**
   - Uniform or variable (as expected)?
   - Consistent with data density?

3. **Verify data integrity:**
   - No overlapping contours
   - No duplicate geometries
   - Valid shapefile structure

## Output File

**File**: `linhas_equipotenciais.shp` (with .shx, .dbf, .prj files)

This is your primary output before final clipping to study area boundaries.
