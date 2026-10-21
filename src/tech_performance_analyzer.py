"""Análise de desempenho de computadores com correlação e regressão linear múltipla.

Base: Machine CPU (OpenML, dataset 230).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from sklearn.datasets import fetch_openml

OUTPUT_DIR = Path("outputs")
PREDICTORS = ["MYCT", "MMIN", "MMAX", "CACH", "CHMIN", "CHMAX"]


def load_data() -> pd.DataFrame:
    """Baixa a base Machine CPU e prepara as variáveis numéricas."""
    dataset = fetch_openml(name="machine_cpu", version=1, as_frame=True, parser="auto")
    data = dataset.data.copy()
    data["PRP"] = dataset.target
    return data.astype(float)


def save_plots(data: pd.DataFrame) -> None:
    """Gera matriz de correlação e gráficos de dispersão."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(9, 7))
    sns.heatmap(data.corr(), annot=True, cmap="RdBu_r", center=0, fmt=".2f")
    plt.title("Matriz de correlação - Machine CPU")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "matriz_correlacao.png", dpi=160)
    plt.close()

    variables = ["MMAX", "CACH", "MYCT", "CHMAX"]
    figure, axes = plt.subplots(2, 2, figsize=(12, 8))
    for axis, variable in zip(axes.ravel(), variables):
        sns.regplot(data=data, x=variable, y="PRP", ax=axis,
                    scatter_kws={"alpha": 0.65}, line_kws={"color": "black"})
        axis.set_title(f"{variable} x PRP")
    figure.suptitle("Características técnicas e desempenho relativo", fontweight="bold")
    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "graficos_dispersao.png", dpi=160)
    plt.close(figure)


def fit_model(data: pd.DataFrame):
    """Ajusta e retorna o modelo OLS para prever PRP."""
    features = sm.add_constant(data[PREDICTORS])
    return sm.OLS(data["PRP"], features).fit()


def predict_configuration(model) -> float:
    """Prevê o PRP da configuração proposta no enunciado."""
    configuration = pd.DataFrame([{
        "const": 1, "MYCT": 50, "MMIN": 4000, "MMAX": 16000,
        "CACH": 64, "CHMIN": 4, "CHMAX": 16,
    }])
    return float(model.predict(configuration).iloc[0])


def main() -> None:
    data = load_data()
    print("\n--- DIAGNÓSTICO INICIAL ---")
    print(f"Equipamentos: {len(data)}")
    print(f"Valores ausentes: {data.isna().sum().sum()}")
    print("\nCorrelação com PRP:")
    print(data.corr()["PRP"].sort_values(ascending=False))

    save_plots(data)
    model = fit_model(data)
    print("\n--- REGRESSÃO LINEAR MÚLTIPLA ---")
    print(model.summary())
    print(f"\nPRP previsto para a nova configuração: {predict_configuration(model):.2f}")
    print("Gráficos salvos na pasta outputs/.")


if __name__ == "__main__":
    main()
