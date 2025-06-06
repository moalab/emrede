# 📊 Painel Interativo – Programa em Rede dos Núcleos de Inovação Tecnológica do Estado

Este repositório contém o código-fonte do painel interativo construído com Streamlit para visualizar e analisar os dados do **Programa em Rede – Ciclo 2**, que envolve os Núcleos de Inovação Tecnológica (NITs) do Espírito Santo.

## 🎯 Objetivo

Fornecer uma plataforma interativa, leve e acessível para:
- Acompanhar as atividades do programa
- Visualizar dados por eixo estratégico, tipo de ação, datas e participantes
- Gerar relatórios em Excel e PDF
- Auxiliar na prestação de contas e na gestão do programa

## 🧱 Estrutura do Painel

- **Visão Geral** – indicadores principais e gráficos de distribuição
- **Por Eixo Estratégico** – filtro e análise por Estrutura de Apoio, Gestão, Sustentabilidade e Alianças
- **Por Tipo de Atividade** – reuniões, oficinas, entregas
- **Tabela Interativa** – pesquisa e filtros por participante, eixo, data e tipo
- **Linha do Tempo** – visualização cronológica das ações
- **Exportação** – botões para download em Excel e PDF

## 🖼️ Identidade Visual

- Cores baseadas na nova identidade FAPES 2024:
  - Azul: `#213b8b`
  - Verde: `#aebc14`
  - Preto: `#000000`
- Estilo minimalista, com foco em legibilidade e objetividade

## 🚀 Como executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/painel-programa-em-rede.git
cd painel-programa-em-rede
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode o painel:

```bash
streamlit run app.py
```

## 📁 Estrutura de Arquivos

```
📦 painel-programa-em-rede
├── 📁 data/                       # Planilhas e base consolidada
├── 📁 assets/                     # Logos, ícones, arquivos visuais
├── 📄 app.py                      # Código principal do painel
├── 📄 requirements.txt            # Dependências Python
└── 📄 README.md                   # Este arquivo
```

## 👨‍💻 Desenvolvimento

Desenvolvido por **Gabriel Torobay**, com base nos dados oficiais do **Programa em Rede** e na identidade visual da **FAPES – Fundação de Amparo à Pesquisa e Inovação do Espírito Santo**.
