# Configuração de Deploy - Potentiometric Map

## 📋 Visão Geral

Este documento descreve a configuração de deploy automático do projeto usando GitHub Actions e GitHub Pages.

## 🔧 Componentes Configurados

### 1. GitHub Actions Workflow (`.github/workflows/static.yml`)

**O que faz:**
- Dispara automaticamente quando há push na branch `main`
- Apenas executa quando há mudanças em `potentiometric_map_tutorial/` ou no próprio workflow
- Compila o site MyST em HTML
- Publica automaticamente no GitHub Pages

**Fluxo:**
```
Push para main
    ↓
GitHub Actions verifica mudanças
    ↓
Se houver mudanças em potentiometric_map_tutorial/ ou workflow:
    ↓
- Setup Node.js 20
- Instala MyST CLI via npm
- Compila: cd potentiometric_map_tutorial && myst build --html
- Configura GitHub Pages
- Upload artefato de _build/html
- Deploy automático
```

### 2. MyST Configuration (`potentiometric_map_tutorial/myst.yml`)

**Configurações principais:**
- **title**: Título do projeto
- **toc**: Estrutura de navegação (Table of Contents)
- **site.template**: Usa `book-theme` para layout de livro
- **site.base_url**: URL de publicação no GitHub Pages
- **site.actions**: Links adicionais (Colab, etc)

### 3. .gitignore na Raiz

**Arquivos ignorados:**
- `_build/` - Output compilado do MyST
- `node_modules/` - Dependências npm
- `__pycache__/` - Cache Python
- `.venv/`, `venv/` - Ambientes virtuais
- `.vscode/`, `.idea/` - Configurações de IDEs
- `.env` - Variáveis de ambiente
- E outros arquivos temporários

## 🚀 Processo de Deploy

### Trigger
- Push na branch `main` com mudanças em `potentiometric_map_tutorial/**` ou `.github/workflows/static.yml`

### Execução
1. GitHub Actions inicia job `deploy`
2. Node.js 20 é configurado
3. MyST CLI é instalado globalmente
4. `myst build --html` é executado dentro de `potentiometric_map_tutorial/`
5. Arquivos compilados são coletados de `potentiometric_map_tutorial/_build/html`
6. Pagina é publicada em `https://hydrologywatersecurity.github.io/potentiometric_map/`

### Tempo
- Deploy geralmente leva 1-2 minutos
- Página fica disponível ~30 segundos após conclusão

## 📊 Status do Deploy

Acesse:
- **Actions**: https://github.com/hydrologywatersecurity/potentiometric_map/actions
- **Logs**: Clique no último run para ver detalhes
- **Página Publicada**: https://hydrologywatersecurity.github.io/potentiometric_map/

## ⚙️ Configuração do GitHub Pages

**Requerimentos (configurar em Settings → Pages):**
- Source: Deploy from a branch
- Branch: `gh-pages` (criada automaticamente pelo workflow)
- Folder: `/ (root)`

O workflow cria e atualiza a branch `gh-pages` automaticamente.

## 🔐 Permissões Necessárias

O workflow requer estas permissões (já configuradas):
```yaml
permissions:
  contents: read        # Ler repositório
  pages: write         # Publicar no Pages
  id-token: write      # OIDC token para deploy
```

## 🛠️ Troubleshooting

### Deploy falha com "myst build" error
- Verificar sintaxe do `myst.yml`
- Garantir que arquivos no TOC existem
- Verificar formato dos Markdown/Notebooks

### Página não atualiza
- Aguardar ~1 minuto após push
- Limpar cache do navegador (Ctrl+Shift+Delete)
- Verificar GitHub Actions → Actions tab

### Build bem-sucedido mas página não muda
- Verificar branch `gh-pages` foi atualizada
- Verificar Settings → Pages → Source está correto
- Tentar acesso com URL completa: `https://hydrologywatersecurity.github.io/potentiometric_map/`

## 📝 Modificações Futuras

### Para alterar estrutura:
1. Editar `potentiometric_map_tutorial/myst.yml`
2. Adicionar/remover páginas em `content/` ou `notebooks/`
3. Fazer commit e push

### Para usar diferentes versões do MyST:
1. Editar `.github/workflows/static.yml`
2. Mudar `node-version: 20` ou `npm install -g mystmd@versão`

### Para adicionar dependências Python:
1. Criar `requirements.txt` em `potentiometric_map_tutorial/`
2. Adicionar step ao workflow:
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

## 📚 Referências

- [MyST CLI Docs](https://mystmd.org/guide/quickstart)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [OIDC in GitHub Actions](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)

## 🆘 Suporte

Para problemas com deploy:
1. Verificar logs em GitHub Actions
2. Executar `myst build --html` localmente para reproduzir
3. Verificar arquivo `.github/workflows/static.yml` para sincronização
