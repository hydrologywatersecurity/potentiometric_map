# Potentiometric Map - Interactive Tutorial

Practical tutorial for spatial interpolation and piezometric analysis in Python.

## 📚 About the Project

This repository contains a comprehensive interactive tutorial on creating potentiometric surface maps using spatial interpolation techniques. The tutorial covers the complete workflow from groundwater data acquisition through final map generation using ArcGIS and open-source tools.

**Tutorial Focus:**
- Extract groundwater data from the GGIS (Geological and Groundwater Information System)
- Process well data in ArcGIS
- Calculate water table elevations
- Apply spatial interpolation methods (Thin Plate Spline and Inverse Distance Weighting)
- Generate equipotential contour lines
- Create professional potentiometric maps

**Study Area**: Catawba River Basin (North Carolina) with publicly available groundwater data

**Access**: The tutorial is published at `https://hydrologywatersecurity.github.io/potentiometric_map/`

## 🌎 Tutorial Structure

The tutorial is organized into four main sections:

### 1. **Fundamentals**
   - Course objectives and learning outcomes
   - Study area description (Catawba River Basin)
   - Groundwater data sources and characteristics

### 2. **Data Processing**
   - Data extraction from GGIS web interface
   - Loading and preparing data in ArcGIS
   - Well data quality control and filtering
   - Water table elevation calculations

### 3. **Spatial Interpolation**
   - Interpolation methods overview (TPS vs IDW)
   - Thin Plate Spline implementation (preferred method)
   - Inverse Distance Weighting alternative
   - Equipotential contour line extraction

### 4. **Map Finalization**
   - Clipping contours to aquifer boundaries
   - Final styling and visualization
   - Publication-ready map creation



## 📁 Repository Structure

```
potentiometric_map/
├── .github/
│   └── workflows/
│       └── static.yml           # Automatic deployment workflow
├── potentiometric_map_tutorial/ # Main tutorial folder
│   ├── myst.yml                 # MyST configuration
│   ├── intro.md                 # Home page
│   ├── content/                 # Markdown content
│   ├── notebooks/               # Jupyter notebooks
│   └── _build/                  # Compiled output (ignored by git)
├── .gitignore                   # Git ignore configuration
└── README.md                    # This file
```

## 🛠️ How to Work on the Tutorial

### Prerequisites

- Node.js 20+
- MyST CLI

### Installation

```bash
# Install MyST CLI globally
npm install -g mystmd

# Or, locally (recommended):
cd potentiometric_map_tutorial
npm install mystmd
```

### Local Development

```bash
cd potentiometric_map_tutorial

# Compile the site
myst build --html

# Serve locally (if available)
myst serve
```

**Note**: When deployed to GitHub Pages, the `BASE_URL` environment variable is automatically set to `/potentiometric_map` in the workflow. This ensures links work correctly in the subfolder deployment.

## 📝 Content Editing

### Current Tutorial Pages

The tutorial is organized as follows:

- `intro.md` - Welcome and navigation
- **Fundamentals Section:**
  - `content/01_conceitos_hidrogeologia.md` - Concepts and study area
  - `content/02_coleta_dados.md` - Data collection from GGIS
- **Data Processing Section:**
  - `content/03_data_processing_arcgis.md` - ArcGIS setup and well filtering
  - `content/04_water_table_calculation.md` - Water table calculations
- **Spatial Interpolation Section:**
  - `content/05_interpolation_methods.md` - TPS and IDW methods
  - `content/06_equipotential_extraction.md` - Contour line extraction
- **Map Finalization Section:**
  - `content/07_contour_clipping.md` - Clipping to boundaries

### Add a New Page

1. Create a file in `potentiometric_map_tutorial/content/XX_page_name.md`
2. Update `potentiometric_map_tutorial/myst.yml` with the new file:

```yaml
- title: "Section Name"
  children:
    - file: content/XX_page_name.md
```

### Add a Notebook

1. Place `.ipynb` file in `potentiometric_map_tutorial/notebooks/`
2. Add reference to `myst.yml`:

```yaml
- file: notebooks/XX_notebook_name.ipynb
```

### Tutorial Template

Use the provided template files to maintain consistency:
- `potentiometric_map_tutorial/content/TEMPLATE_pagina.md` - Markdown template
- `potentiometric_map_tutorial/notebooks/TEMPLATE_notebook.ipynb` - Notebook template

## 📋 Deployment Checklist

Before pushing, make sure:

- ✅ Content is in `potentiometric_map_tutorial/`
- ✅ File `myst.yml` is updated with new pages
- ✅ No files in `_build/` are committed (check `.gitignore`)
- ✅ Internal links are correct
- ✅ Images have relative paths

## 🚀 Performing Deployment

Simply push to the `main` branch:

```bash
git add .
git commit -m "Update tutorial"
git push origin main
```

GitHub Actions will automatically:
1. Compile the site to HTML
2. Upload files to GitHub Pages
3. Publish the page

Wait ~30 seconds for the page to be available.

## 📖 References

- [MyST Documentation](https://mystmd.org)
- [GitHub Pages](https://pages.github.com/)
- [GitHub Actions](https://docs.github.com/en/actions)

## 👨‍💻 Author

M.S. Bruno Ken Marchezepe - University of São Paulo
Prof. Ph.D. Paulo Tarso Sanches de Oliveira - University of North Carolina at Charlotte

## 📄 License

See `LICENSE` file
