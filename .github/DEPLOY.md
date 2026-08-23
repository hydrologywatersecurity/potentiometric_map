# Deployment Configuration - Potentiometric Map

## 📋 Overview

This document describes the automatic deployment configuration of the project using GitHub Actions and GitHub Pages.

## 🔧 Configured Components

### 1. GitHub Actions Workflow (`.github/workflows/static.yml`)

**What it does:**
- Triggers automatically when there is a push to the `main` branch
- Only executes when there are changes in `potentiometric_map_tutorial/` or the workflow itself
- Compiles the MyST site to HTML
- Automatically publishes to GitHub Pages

**Flow:**
```
Push to main
    ↓
GitHub Actions checks changes
    ↓
If there are changes in potentiometric_map_tutorial/ or workflow:
    ↓
- Setup Node.js 20
- Install MyST CLI via npm
- Compile: cd potentiometric_map_tutorial && myst build --html
- Configure GitHub Pages
- Upload _build/html artifact
- Automatic deployment
```

### 2. MyST Configuration (`potentiometric_map_tutorial/myst.yml`)

**Main settings:**
- **title**: Project title
- **toc**: Navigation structure (Table of Contents)
- **site.template**: Uses `book-theme` for book-like layout
- **site.base_url**: Publication URL on GitHub Pages
- **site.actions**: Additional links (Colab, etc)

### 3. .gitignore at Root

**Ignored files:**
- `_build/` - Compiled MyST output
- `node_modules/` - npm dependencies
- `__pycache__/` - Python cache
- `.venv/`, `venv/` - Virtual environments
- `.vscode/`, `.idea/` - IDE configurations
- `.env` - Environment variables
- And other temporary files

## 🚀 Deployment Process

### Trigger
- Push to `main` branch with changes in `potentiometric_map_tutorial/**` or `.github/workflows/static.yml`

### Execution
1. GitHub Actions starts `deploy` job
2. Node.js 20 is configured
3. MyST CLI is installed globally
4. `myst build --html` is executed inside `potentiometric_map_tutorial/`
5. Compiled files are collected from `potentiometric_map_tutorial/_build/html`
6. Page is published at `https://hydrologywatersecurity.github.io/potentiometric_map/`

### Timing
- Deployment usually takes 1-2 minutes
- Page becomes available ~30 seconds after completion

## 📊 Deployment Status

Access:
- **Actions**: https://github.com/hydrologywatersecurity/potentiometric_map/actions
- **Logs**: Click the latest run to see details
- **Published Page**: https://hydrologywatersecurity.github.io/potentiometric_map/

## ⚙️ GitHub Pages Configuration

**Requirements (configure in Settings → Pages):**
- Source: Deploy from a branch
- Branch: `gh-pages` (automatically created by workflow)
- Folder: `/ (root)`

The workflow automatically creates and updates the `gh-pages` branch.

## 🔐 Required Permissions

The workflow requires these permissions (already configured):
```yaml
permissions:
  contents: read        # Read repository
  pages: write         # Publish to Pages
  id-token: write      # OIDC token for deployment
```

## 🛠️ Troubleshooting

### Deployment fails with "myst build" error
- Check syntax of `myst.yml`
- Ensure TOC files exist
- Check Markdown/Notebooks format

### Page doesn't update
- Wait ~1 minute after push
- Clear browser cache (Ctrl+Shift+Delete)
- Check GitHub Actions → Actions tab

### Build successful but page doesn't change
- Check if `gh-pages` branch was updated
- Verify Settings → Pages → Source is correct
- Try accessing with full URL: `https://hydrologywatersecurity.github.io/potentiometric_map/`

## 📝 Future Modifications

### To change structure:
1. Edit `potentiometric_map_tutorial/myst.yml`
2. Add/remove pages in `content/` or `notebooks/`
3. Commit and push

### To use different MyST versions:
1. Edit `.github/workflows/static.yml`
2. Change `node-version: 20` or `npm install -g mystmd@version`

### To add Python dependencies:
1. Create `requirements.txt` in `potentiometric_map_tutorial/`
2. Add step to workflow:
```yaml
- name: Setup Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'

- name: Install Python dependencies
  run: |
    cd potentiometric_map_tutorial
    pip install -r requirements.txt
```

## 📚 References

- [MyST CLI Docs](https://mystmd.org/guide/quickstart)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [OIDC in GitHub Actions](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)

## 🆘 Support

For deployment issues:
1. Check logs in GitHub Actions
2. Run `myst build --html` locally to reproduce
3. Check `.github/workflows/static.yml` for sync
