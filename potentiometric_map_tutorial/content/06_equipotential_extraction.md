# Extracting Equipotential Contours

## Concept: Equipotential Lines

**Equipotential lines** (or contours) connect points of equal hydraulic head. They represent the potentiometric surface in 2D map form and are essential for:

- Visualizing groundwater flow patterns
- Identifying flow direction (perpendicular to contours)
- Determining gradient magnitude
- Assessing regional hydrogeology
- Creating professional maps

## Generating Contour Lines from Raster

### Step 1: Open Contour Tool

In ArcGIS/QGIS:
1. Navigate to: **Raster** → **Extraction** → **Contour...**
2. This tool converts your interpolated raster to vector contour lines

:::{figure} ../assets/images/31_figure.png
:alt: Raster menu with Extraction submenu showing Contour tool option
:width: 600px

**Figure 1:** Access the Contour tool through Raster → Extraction → Contour to convert your interpolated raster surface to vector contour lines.
:::

### Step 2: Configure Contour Parameters

Set the following parameters:

| Parameter | Setting | Notes |
|---|---|---|
| **Input layer** | `na_freatic_interpolado_TPS` | Your interpolated surface raster |
| **Interval between contours** | 10.0 meters | Creates a contour every 10m elevation change |
| **Attribute name** | `ELEV` | Field name storing elevation value |
| **Output contours** | `linhas_equipotenciais.shp` | Output shapefile name |

:::{figure} ../assets/images/32_figure.png
:alt: Contour tool dialog with interval set to 10.0, attribute name ELEV, and output filename
:width: 600px

**Figure 2:** Configure contour parameters: set interval to 10 meters, attribute to ELEV, and specify the output filename as `linhas_equipotenciais.shp`.
:::

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
