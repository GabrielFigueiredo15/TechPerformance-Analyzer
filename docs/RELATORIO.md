# Relatório Técnico

## Medidas de Associação Correlação e Regressão Linear

**Integrantes:** Gabriel Catter, Daniel Gonçalves e Lucas Dian  
**Disciplina:** Métodos Quantitativos em Computação - UNIFOR  
**Data:** outubro de 2026

## Objetivo

Investigar quais características técnicas de computadores estão associadas ao desempenho relativo publicado (`PRP`) e construir um modelo de regressão linear múltipla para apoiar a análise de novas configurações.

## Base de dados

Foi utilizada a base **Machine CPU**, disponibilizada pelo OpenML. Ela possui 209 equipamentos e as seguintes variáveis:

| Variável | Descrição |
| --- | --- |
| `MYCT` | Tempo de ciclo da máquina, em nanossegundos |
| `MMIN` / `MMAX` | Memória principal mínima e máxima, em KB |
| `CACH` | Memória cache, em KB |
| `CHMIN` / `CHMAX` | Número mínimo e máximo de canais |
| `PRP` | Desempenho relativo publicado |

## Metodologia

1. Carregamento e tratamento dos dados no pandas.
2. Verificação de valores ausentes e diagnóstico inicial.
3. Cálculo da matriz de correlação de Pearson.
4. Criação de gráficos de dispersão entre `PRP` e `MMAX`, `CACH`, `MYCT` e `CHMAX`.
5. Ajuste de uma regressão linear múltipla com `PRP` como resposta.
6. Previsão de desempenho para uma nova configuração.

## Principais interpretações

- Memória máxima, memória cache e canais máximos apresentam associação positiva com o desempenho relativo.
- O tempo de ciclo apresenta associação negativa: ciclos maiores tendem a estar associados a menor desempenho.
- Correlação mostra associação, mas não comprova causalidade.
- O modelo de regressão avalia as variáveis em conjunto e pode ser usado como apoio à decisão, não como garantia de desempenho.

## Configuração avaliada

| Característica | Valor |
| --- | --- |
| `MYCT` | 50 ns |
| `MMIN` | 4.000 KB |
| `MMAX` | 16.000 KB |
| `CACH` | 64 KB |
| `CHMIN` | 4 |
| `CHMAX` | 16 |

Execute o script para gerar a previsão e os gráficos com a base atual.

## Situação 2

A segunda situação da atividade exige uma pesquisa real com pelo menos 20 estudantes, relacionando horas diárias de uso do celular e mensagens enviadas por dia. Os dados devem ser coletados antes de se calcular a reta de regressão simples, o coeficiente de correlação e o R².

## Referência

OPENML. [Machine CPU - dataset 230](https://www.openml.org/d/230).
