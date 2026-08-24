# Calculating the Water Table Elevation

## Concept: Groundwater Hydraulic Head

The **groundwater hydraulic head** (also called water table elevation) represents the elevation of the water surface at each well location. It is calculated as:

### Formula

$$
\text{Hydraulic Head} = \text{Surface Elevation} - \text{Static Water Level Depth}
$$

Or:

$$
h = z_{surface} - d_{water}
$$

Where:
- **h** = Hydraulic head (water table elevation) [meters above sea level]
- **z_surface** = Ground surface elevation at well location [meters above sea level]
- **d_water** = Static water level depth below surface [meters]

### Example Calculation

**Well Example:**
- Surface elevation: 300 m above sea level
- Static water level depth: 15 m below surface
- Hydraulic head: 300 - 15 = **285 m above sea level**

This calculated value represents the potentiometric head at that well location.

## Implementing in ArcGIS

### Add Calculation Field

1. Open the **Attribute Table** for your `pocos_mde` layer:
   - Right-click on the layer → **Attribute Table**

2. Add a new field for the calculated hydraulic head:
   - Click **Add Field** button
   - Field name: `na_freatic` (Portuguese: "nível freático" = water table level)
   - Data type: **Double**
   - Click **OK**

### Calculate Values

1. Right-click on the new `na_freatic` field → **Field Calculator**

2. Enter the calculation formula:
   - Use the names of your existing fields
   - Typical formula: `!elevation! - !water_depth!`
   - Adjust field names to match your data structure

3. Click **OK** to calculate values for all wells

### Verify Results

1. Examine the calculated `na_freatic` column:
   - Values should be reasonable (typically 100-500m for most regions)
   - Should be less than surface elevation
   - Check for any NULL or impossible values

2. Remove any records with:
   - NULL hydraulic head values
   - Negative or unrealistic values
   - Wells with insufficient data

## Interpretation

### Water Table Patterns

The hydraulic head values represent the elevation of the water table across your study area. Patterns to look for:

- **High hydraulic heads**: Recharge areas (higher water table)
- **Low hydraulic heads**: Discharge areas (lower water table)
- **Gradual changes**: Typical flow patterns
- **Sharp changes**: Possible faults, barriers, or boundaries

### Quality Indicators

Good quality potentiometric data should show:

- Smooth spatial variation (no random jumps)
- Logical flow from high to low elevations
- Consistent pattern with regional geology
- Correlation with topography in unconfined aquifers

## Next Steps

With the `na_freatic` field calculated, you now have the primary data for spatial interpolation. This field will be used in the subsequent steps to:

1. Create an interpolated potentiometric surface (raster)
2. Generate equipotential contour lines
3. Produce the final potentiometric map
