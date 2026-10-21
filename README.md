# 📊 TechPerformance Analyzer

> Um projeto de análise de dados que transforma especificações técnicas em insights sobre desempenho computacional.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-0A66C2?style=for-the-badge&logo=python&logoColor=white)

## 💡 Sobre o projeto

O **TechPerformance Analyzer** é um projeto acadêmico de Métodos Quantitativos em Computação. Ele analisa a relação entre características de computadores - como memória máxima, memória cache, tempo de ciclo e canais de comunicação - e o desempenho relativo publicado de cada máquina.

Com **correlação de Pearson**, gráficos de dispersão e **regressão linear múltipla**, o projeto identifica quais fatores estão associados ao desempenho e estima o resultado esperado de uma nova configuração.

## 🎯 Objetivos

- Investigar a associação entre especificações técnicas e desempenho (`PRP`).
- Visualizar relações por meio de matriz de correlação e gráficos de dispersão.
- Ajustar um modelo de regressão linear múltipla.
- Avaliar significância estatística, R², R² ajustado, estatística F e p-valores.
- Prever o desempenho de uma configuração de computador proposta no estudo.

## 📈 Base de dados

O projeto utiliza a base [Machine CPU](https://www.openml.org/d/230), disponibilizada pelo OpenML. Ela reúne informações de **209 equipamentos**.

| Variável | Significado |
| --- | --- |
| `MYCT` | Tempo de ciclo do processador, em nanossegundos |
| `MMIN` | Memória principal mínima, em KB |
| `MMAX` | Memória principal máxima, em KB |
| `CACH` | Memória cache, em KB |
| `CHMIN` | Número mínimo de canais |
| `CHMAX` | Número máximo de canais |
| `PRP` | Desempenho relativo publicado |

## ✨ O que o projeto entrega

| Etapa | Resultado |
| --- | --- |
| Diagnóstico inicial | Quantidade de equipamentos e verificação de valores ausentes |
| Correlação | Relação de cada variável técnica com o desempenho |
| Visualização | Heatmap e gráficos de dispersão com linha de tendência |
| Regressão múltipla | Coeficientes, p-valores, R², R² ajustado e teste F |
| Previsão | Estimativa de `PRP` para uma nova configuração |

## 🚀 Como executar

```bash
git clone https://github.com/GabrielFigueiredo15/TechPerformance-Analyzer.git
cd TechPerformance-Analyzer
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python src/tech_performance_analyzer.py
```

Após a execução, os gráficos serão salvos na pasta `outputs/`.

## 🗂️ Estrutura do repositório

```text
.
├── docs/
│   └── RELATORIO.md
├── src/
│   └── tech_performance_analyzer.py
├── requirements.txt
└── README.md
```

## 🧠 Insights do estudo

- Memória máxima, cache e quantidade de canais tendem a apresentar relação positiva com o desempenho.
- Tempo de ciclo maior tende a se associar a menor desempenho relativo.
- Uma única especificação não explica todo o resultado: o modelo considera as variáveis de forma conjunta.
- Correlação indica associação, mas não prova causalidade.

## 👥 Integrantes

- Gabriel Catter
- Daniel Gonçalves
- Lucas Dian

## 🎓 Contexto acadêmico

Projeto desenvolvido para a disciplina de **Métodos Quantitativos em Computação**, do curso de Ciência da Computação da **UNIFOR**.

---

Feito com 💙, Python e dados para transformar especificações em decisões mais claras.
