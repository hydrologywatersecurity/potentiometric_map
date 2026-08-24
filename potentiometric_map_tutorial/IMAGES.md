# Tutorial Images Guide

## Overview

This tutorial includes **40 high-quality figures** extracted from the original Word document. Images are stored in PNG format (lossless) for optimal quality in web browsers.

## Image Format & Recommendations

### Current Setup: PNG Format ✅

**Advantages:**
- Lossless compression (no quality loss)
- Supports transparency (alpha channel)
- Smaller file size than uncompressed images
- Direct extraction from docx (maintains original quality)
- Excellent for screenshots and diagrams

**Total Size:** ~14.4 MB (all 40 figures)
- Average per figure: ~360 KB
- Largest: 02_figure.png (1.5 MB - likely full-page diagram)

### Why PNG is Best for This Tutorial

1. **Screenshots & GIS Dialogs**: PNG is ideal for software UI screenshots
2. **Diagrams & Maps**: Crisp lines and text remain sharp
3. **Web Optimization**: Modern browsers handle PNG efficiently
4. **No Quality Loss**: Important for technical documentation

### Alternative Formats (If Needed)

| Format | Use Case | Pros | Cons |
|--------|----------|------|------|
| **PNG** | ✅ Current | Lossless, small, transparent | Larger than JPG for photos |
| **WebP** | High-volume deployments | Smaller than PNG/JPG | Less browser support in older versions |
| **SVG** | Diagrams, flowcharts | Infinitely scalable | Not suitable for screenshots |
| **JPG** | High-compression photos | Smallest file size | Lossy quality, no transparency |

## Image Manifest

All images are stored in: `potentiometric_map_tutorial/assets/images/`

### Image Inventory

| File | Size | Likely Content | Section |
|------|------|-----------------|---------|
| 01_figure.png | 98.9 KB | Title page / Introduction | Intro |
| 02_figure.png | 1496.2 KB | Study area map (large diagram) | Concepts |
| 03_figure.png | 579.6 KB | Data structure diagram | Data Collection |
| 04_figure.png | 967.7 KB | Regional map/context | Study Area |
| 05_figure.png | 779.3 KB | Well data example | Data Collection |
| 06_figure.png | 117.6 KB | Icon/small diagram | Data Processing |
| ... | ... | ... | ... |
| 22_figure.png | 110.4 KB | Processing Toolbox screenshot | Interpolation |
| 23_figure.png | 1214.2 KB | SAGA navigation menu | Interpolation |
| 26_figure.png | 1299.2 KB | TPS settings dialog | Interpolation |
| 31_figure.png | 1239.0 KB | Contour tool interface | Equipotential |
| 32_figure.png | 838.2 KB | Contour parameters | Equipotential |
| 36_figure.png | 569.5 KB | Clipping tool | Clipping |
| 37_figure.png | 105.1 KB | Clipping settings | Clipping |
| 40_figure.png | 237.7 KB | Final map example | Clipping |

## Using Images in Markdown

### Basic Syntax

```markdown
![Description of figure](../assets/images/XX_figure.png)
```

### With Caption (MyST Syntax)

```markdown
:::{figure} ../assets/images/XX_figure.png
:alt: Description for accessibility
:name: fig-descriptive-name

**Figure Caption:** Description of what the figure shows.
:::
```

### Recommended: Captioned Figures

For technical documentation, captions provide context:

```markdown
:::{figure} ../assets/images/22_figure.png
:alt: Screenshot of QGIS Processing Toolbox menu
:width: 600px

**Figure 1:** Open the Processing Toolbox using Ctrl + Alt + T to access spatial interpolation tools.
:::
```

## Image Placement Strategy

### By Section

**Fundamentals (01_concepts.md, 02_data_collection.md)**
- Use: 01_figure.png (title/intro)
- Use: 02-05_figure.png (study area, data examples)
- Total: ~5-6 figures

**Data Processing (03_data_processing.md, 04_water_table.md)**
- Use: 06-21_figure.png (ArcGIS interface, layer operations)
- Total: ~15 figures

**Spatial Interpolation (05_interpolation.md)**
- Use: 22, 23, 26_figure.png (SAGA toolbox, TPS settings)
- Use: 24-25_figure.png (IDW alternative)
- Total: ~8 figures

**Equipotential Extraction (06_equipotential.md)**
- Use: 27-32_figure.png (contour tool, styling)
- Total: ~6 figures

**Map Finalization (07_clipping.md)**
- Use: 33-40_figure.png (clipping tool, final output)
- Total: ~8 figures

## Optimization Notes

### Current Status
✅ All 40 images extracted as PNG  
✅ Organized in: `potentiometric_map_tutorial/assets/images/`  
✅ Manifest created: `manifest.json`  

### Next Steps
1. Map each figure to correct content section
2. Add MyST figure references with captions
3. Test rendering in local build
4. Verify image paths work in GitHub Pages deployment

### File Size Considerations

- **Total images:** 14.4 MB
- **First page load:** ~2-3 figures visible (50-100 KB)
- **Full page load:** All 40 figures (14.4 MB)
- **Recommendation:** Users on slower connections will load incrementally

## Deployment

When deployed to GitHub Pages:
- Images served from: `https://hydrologywatersecurity.github.io/potentiometric_map/assets/images/`
- All relative paths from markdown should work automatically
- No CDN needed (hosted on GitHub Pages)

## Accessibility

All images should include:
1. **Alt text** (describe for screen readers)
2. **Caption** (explain significance)
3. **Figure number** (reference in text)

Example:
```markdown
:::{figure} ../assets/images/22_figure.png
:alt: QGIS Processing Toolbox with SAGA menu expanded
:name: fig-processing-toolbox

**Figure 1:** Click Processing Toolbox (Ctrl + Alt + T) and navigate to SAGA → Raster Spline to access Thin Plate Spline interpolation.
:::
```
