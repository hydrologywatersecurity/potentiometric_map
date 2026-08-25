# Post-Processing: Clipping Contours to Study Area

## Concept: Domain Constraint

After generating equipotential contours, you must clip them to your study area boundary. This:

- Removes extrapolated contours outside your area
- Focuses analysis on your domain
- Creates publication-ready maps
- Eliminates unreliable interpolated values
- Improves visualization clarity

## Clipping to Aquifer Boundary

### Step 1: Add Labels to Contours

Before finalizing, add elevation labels to your contours:

1. Right-click the contour layer → **Label**
2. Enable labeling with the `Contour` field (elevation values)
3. Adjust label properties for readability

### Step 2: Style Contour Lines

1. Right-click contour layer → **Symbology**
2. Apply styling:
   - **Line Color**: Dark blue or black
   - **Line Weight**: 0.5-1.0 points
   - **Transparency**: 70-80% for overlay visualization
3. Optionally use different line styles for major/minor contours

### Final Output

Your potentiometric map is now complete with:
- ✓ Clipped raster surface (TPS interpolation)
- ✓ Labeled equipotential contour lines
- ✓ Well point locations overlay
- ✓ Study area boundaries
- ✓ Professional styling for publication

## Map Composition

For presentation-ready maps, include:

1. **Main elements:**
   - Clipped equipotential contours (primary feature)
   - Well point locations (reference data)
   - Study area boundary (context)
   - Hillshade or topography (background)

2. **Supporting elements:**
   - Scale bar
   - North arrow
   - Legend with contour intervals
   - Title and date
   - Author attribution
   - Projection information

### Step 3: Execute Clipping

1. Click **Run**
2. The output shapefile contains only contours within the aquifer boundary
3. Result: `linhas_equipotenciais_recortado.shp`

## Optional: Clipping to Basin Boundary

### Regional Context Mapping

For broader regional analysis, optionally repeat clipping using the Catawba River Basin boundary:

#### Step 1: Secondary Clipping

1. Open Clip tool again
2. **Input layer**: `linhas_equipotenciais_recortado.shp` (already aquifer-clipped)
3. **Overlay layer**: `boundaries_catawba` (CRB boundary polygon)
4. **Output file**: `linhas_equipotenciais_bacia_CRB.shp`

#### Why Do This?

- Provides regional hydrological context
- Shows how aquifer flows relate to basin structure
- Better for publications and presentations
- Allows comparison of multiple aquifers

## Final Output Specifications

### Clipped Contour Layer Attributes

The final clipped layer should contain:

**Geometric properties:**
- Valid line geometries (no self-intersections)
- Proper topology with aquifer/basin boundary
- No gaps or slivers along clipping boundary
- Correct spatial reference

**Attribute data:**
- ELEV field with elevation values for all features
- Proper data types
- No NULL values
- Contours properly labeled

### Quality Assurance Checklist

Before finalizing:

- ✓ All contours within boundary polygon
- ✓ No truncated or incomplete contours
- ✓ Elevation values consistent throughout
- ✓ Labels positioned correctly
- ✓ Layer properly styled for presentation
- ✓ Attribute table complete and valid
- ✓ File saved in appropriate projection

## Creating Publication-Ready Maps

### Map Composition

For final presentation, include:

1. **Main elements:**
   - Clipped equipotential contours (primary feature)
   - Well point locations (reference data)
   - Study area boundary (context)
   - DEM hillshade or topography (background reference)

2. **Supporting elements:**
   - Scale bar
   - North arrow
   - Legend with contour intervals
   - Title and date
   - Author attribution
   - Projection information

3. **Visualization best practices:**
   - High contrast colors
   - Clear labeling
   - Appropriate transparency
   - Consistent styling
   - Professional appearance

## Exporting Final Maps

### Raster Export (for presentations)

1. **File** → **Export**
2. Format: PNG or PDF (300 dpi for print)
3. Includes all map elements

### Vector Export (for further analysis)

- Format: GeoPackage (.gpkg) or Shapefile (.shp)
- Preserves editability and attributes
- Suitable for next analysis stages

## Summary of Outputs

| File | Format | Purpose | Status |
|---|---|---|---|
| `na_freatic_interpolado_TPS` | SDAT/TIF | Interpolated surface | Intermediate |
| `linhas_equipotenciais.shp` | Shapefile | Full contours | Intermediate |
| `linhas_equipotenciais_recortado.shp` | Shapefile | Aquifer-clipped | **Final** |
| `linhas_equipotenciais_bacia_CRB.shp` | Shapefile | Basin-clipped | Optional |

The **aquifer-clipped contours** (`linhas_equipotenciais_recortado.shp`) are your primary deliverable, representing the final potentiometric map for analysis and interpretation.
