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

:::{figure} ../assets/images/28_arcgis_attribute_table.png
:alt: ArcGIS Attribute Table showing well data with ID, coordinates, elevation, water depth columns
:width: 600px

**Figure 1:** Attribute Table with well data ready for calculation field.
:::

2. Add a new field for the calculated hydraulic head:
   - Click **Add Field** button
   - Field name: `water_table_head` (English version)
   - Data type: **Double**
   - Click **OK**

:::{figure} ../assets/images/29_arcgis_add_field.png
:alt: ArcGIS Add Field dialog
:width: 600px

**Figure 2:** Add new field for water table head calculations.
:::

### Calculate Values

1. Right-click on the new `water_table_head` field → **Field Calculator**

:::{figure} ../assets/images/30_arcgis_field_calculator.png
:alt: ArcGIS Field Calculator toolbar appearing above attribute table
:width: 600px

**Figure 3:** Field Calculator toolbar for expression entry.
:::

2. Enter the calculation formula:
   - Use the names of your existing fields
   - Typical formula: `!elevation! - !water_depth!`
   - Adjust field names to match your data structure

:::{figure} ../assets/images/31_arcgis_expression_builder.png
:alt: ArcGIS Expression Builder dialog with field list and formula
:width: 600px

**Figure 4:** Expression Builder showing field selection and formula entry: !elevation! - !median_water_depth!
:::

3. Click **OK** to calculate values for all wells

:::{figure} ../assets/images/32_arcgis_calculated_values.png
:alt: ArcGIS Attribute Table showing calculated water_table_head values
:width: 600px

**Figure 5:** Calculated hydraulic head values now populated in the water_table_head column.
:::

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
