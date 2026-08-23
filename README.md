# Potentiometric Map - Interactive Tutorial

Practical tutorial for spatial interpolation and piezometric analysis in Python.

## 📚 About the Project

This repository contains an interactive tutorial on creating and analyzing potentiometric maps, developed in ArcGIS and published with MyST (Markedly Structured Text) and hosted on GitHub Pages.

**Access**: The page will be available at `https://hydrologywatersecurity.github.io/potentiometric_map/`

## 🌎 Available Dataset



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

### Add a Markdown page

1. Create a file in `content/XX_page_name.md`
2. Add reference to `myst.yml`:

```yaml
toc:
  - file: content/XX_page_name.md
```

### Add a Notebook

1. Place `.ipynb` file in `notebooks/`
2. Add reference to `myst.yml`:

```yaml
toc:
  - file: notebooks/XX_notebook_name.ipynb
```

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
