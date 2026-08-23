# Template - Adicionar Nova Página

Este é um arquivo template para adicionar novas páginas ao tutorial.

## Como usar

1. **Copiar este arquivo** com um novo nome seguindo o padrão: `XX_nome_pagina.md`
   - Exemplo: `03_interpolacao_espacial.md`, `04_kriging_ordinario.md`

2. **Editar o conteúdo** seguindo a estrutura MyST/Markdown

3. **Adicionar ao `myst.yml`** na seção `toc`:

```yaml
toc:
  - file: intro.md
  - title: "Fundamentos"
    children:
      - file: content/01_conceitos_hidrogeologia.md
      - file: content/02_coleta_dados.md
      - file: content/03_nova_pagina.md  # ← Adicionar aqui
```

## Estrutura Recomendada

### Cabeçalho (H1)
```markdown
# Título da Página
```

### Seções (H2)
```markdown
## Introdução

Parágrafo inicial...

## Conceitos Principais

Conteúdo...

## Exemplos

Código ou exemplos práticos...

## Conclusão

Resumo...
```

## Recursos MyST

### Imagens
```markdown
![Alt text](../assets/imagem.png)
```

### Código
```python
def funcao_exemplo(param):
    return param * 2
```

### Referências Cruzadas
```markdown
(ref-nome-da-secao)=
## Seção com referência

Referência: [Link](ref-nome-da-secao)
```

### Admonições
```markdown
```{note}
Nota importante
```

```{warning}
Aviso!
```
```

### Equações
```markdown
$$
E = mc^2
$$
```

## Dicas

- Use Markdown puro para máxima compatibilidade
- Mantenha nomes de arquivo simples (sem caracteres especiais)
- Numere sequencialmente para controlar a ordem
- Adicione links internos quando relevante
- Inclua exemplos práticos sempre que possível

## Referências

- [MyST Markdown Docs](https://mystmd.org/guide/markdown)
- [Jupyter Book](https://jupyterbook.org/)
