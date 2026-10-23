#!/usr/bin/env python3
"""IR p1 - Parte 8 - Ex 5: Dashboard simples de incidentes (NIST: Pos-Incidente / metricas).
Usa matplotlib com backend 'Agg' para salvar PNG (headless) em vez de plt.show()."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

dados = {"tipo": ["phishing", "ransomware", "phishing", "vazamento"]}
df = pd.DataFrame(dados)

contagem = df["tipo"].value_counts()
contagem.plot(kind="bar", color="#c0392b")
plt.title("Incidentes por Tipo")
plt.tight_layout()

saida = os.path.join(os.path.dirname(__file__), "..", "prints", "dashboard_incidentes.png")
plt.savefig(saida, dpi=120)
print("Dashboard salvo em:", os.path.relpath(saida))
print(contagem.to_string())
