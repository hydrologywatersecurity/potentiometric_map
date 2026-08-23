# Template - Add New Page

This is a template file to add new pages to the tutorial.

## How to use

1. **Copy this file** with a new name following the pattern: `XX_page_name.md`
   - Example: `03_spatial_interpolation.md`, `04_ordinary_kriging.md`

2. **Edit the content** following the MyST/Markdown structure

3. **Add to `myst.yml`** in the `toc` section:

```yaml
toc:
  - file: intro.md
  - title: "Fundamentals"
    children:
      - file: content/01_conceitos_hidrogeologia.md
      - file: content/02_coleta_dados.md
      - file: content/03_new_page.md  # ← Add here
```

## Recommended Structure

### Header (H1)
```markdown
# Page Title
```

### Sections (H2)
```markdown
## Introduction

Initial paragraph...

## Main Concepts

Content...

## Examples

Code or practical examples...

## Conclusion

Summary...
```

## MyST Resources

### Images
```markdown
![Alt text](../assets/image.png)
```

### Code
```python
def example_function(param):
    return param * 2
```

### Cross-references
```markdown
(ref-section-name)=
## Section with reference

Reference: [Link](ref-section-name)
```

### Admonitions
```markdown
```{note}
Important note
```

```{warning}
Warning!
```
```

### Equations
```markdown
$$
E = mc^2
$$
```

## Tips

- Use plain Markdown for maximum compatibility
- Keep file names simple (no special characters)
- Number sequentially to control order
- Add internal links when relevant
- Include practical examples whenever possible

## References

- [MyST Markdown Docs](https://mystmd.org/guide/markdown)
- [Jupyter Book](https://jupyterbook.org/)
