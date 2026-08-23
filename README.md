# Mapa Potenciométrico - Tutorial Interativo

Tutorial prático para interpolação espacial e análise piezométrica em Python.

## 📚 Sobre o Projeto

Este repositório contém um tutorial interativo sobre criação e análise de mapas potenciométricos, desenvolvido com MyST (Markedly Structured Text) e hospedado no GitHub Pages.

## 🚀 Publicação Automática

A página do tutorial é **publicada automaticamente** sempre que há um push na branch `main` que afeta a pasta `potentiometric_map_tutorial/`.

### Workflow do GitHub Actions

O arquivo `.github/workflows/static.yml` configura:

1. **Trigger**: Detecta mudanças em `potentiometric_map_tutorial/**` ou no próprio workflow
2. **Build**: Compila o site MyST em HTML
3. **Deploy**: Publica automaticamente no GitHub Pages

**Acesso**: A página estará disponível em `https://hydrologywatersecurity.github.io/potentiometric_map/`

## 📁 Estrutura do Repositório

```
potentiometric_map/
├── .github/
│   └── workflows/
│       └── static.yml           # Workflow de deploy automático
├── potentiometric_map_tutorial/ # Pasta principal do tutorial
│   ├── myst.yml                 # Configuração MyST
│   ├── intro.md                 # Página inicial
│   ├── content/                 # Conteúdo em Markdown
│   ├── notebooks/               # Notebooks Jupyter
│   └── _build/                  # Saída compilada (ignorada pelo git)
├── .gitignore                   # Configuração de arquivos ignorados
└── README.md                    # Este arquivo
```

## 🛠️ Como Trabalhar no Tutorial

### Pré-requisitos

- Node.js 20+
- MyST CLI

### Instalação

```bash
# Instalar MyST CLI globalmente
npm install -g mystmd

# Ou, localmente (recomendado):
cd potentiometric_map_tutorial
npm install mystmd
```

### Desenvolvimento Local

```bash
cd potentiometric_map_tutorial

# Compilar o site
myst build --html

# Abrir em um servidor local (se disponível)
myst serve
```

## 📝 Edição de Conteúdo

### Adicionar página em Markdown

1. Criar arquivo em `content/XX_nome_pagina.md`
2. Adicionar referência ao `myst.yml`:

```yaml
toc:
  - file: content/XX_nome_pagina.md
```

### Adicionar Notebook

1. Colocar arquivo `.ipynb` em `notebooks/`
2. Adicionar referência ao `myst.yml`:

```yaml
toc:
  - file: notebooks/XX_nome_notebook.ipynb
```

## 📋 Checklist para Deploy

Antes de fazer push, certifique-se de:

- ✅ Conteúdo está em `potentiometric_map_tutorial/`
- ✅ Arquivo `myst.yml` está atualizado com as novas páginas
- ✅ Nenhum arquivo em `_build/` foi commitado (verificar `.gitignore`)
- ✅ Links internos estão corretos
- ✅ Imagens têm caminhos relativos

## 🚀 Realizando Deploy

Simplesmente faça push para a branch `main`:

```bash
git add .
git commit -m "Atualizar tutorial"
git push origin main
```

O GitHub Actions executará automaticamente:
1. Compila o site em HTML
2. Faz upload dos arquivos para GitHub Pages
3. Publica a página

Aguarde ~30 segundos para a página estar disponível.

## 📖 Referências

- [MyST Documentation](https://mystmd.org)
- [GitHub Pages](https://pages.github.com/)
- [GitHub Actions](https://docs.github.com/en/actions)

## 👨‍💻 Autor

Bruno Ken Marchezepe - USP São Carlos

## 📄 Licença

Veja arquivo `LICENSE`