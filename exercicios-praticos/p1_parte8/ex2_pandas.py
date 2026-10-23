#!/usr/bin/env python3
"""IR p1 - Parte 8 - Ex 2: Analise com Pandas (volume grande).
Aprendizado: priorizacao, estatistica basica, visao de tendencia."""
import os
import pandas as pd

BASE = os.path.join(os.path.dirname(__file__), "..", "dados", "logs.csv")
df = pd.read_csv(BASE)  # colunas: data, evento, ip

falhas = df[df["evento"] == "login_fail"]
top_ips = falhas["ip"].value_counts().head(5)

print("IPs mais suspeitos (por nº de login_fail):")
print(top_ips.to_string())
