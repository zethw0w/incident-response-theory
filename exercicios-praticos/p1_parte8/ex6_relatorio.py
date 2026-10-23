#!/usr/bin/env python3
"""IR p1 - Parte 8 - Ex 6: Geracao de relatorio automatico (gera arquivo TXT)."""
import os

incidentes = [
    {"tipo": "phishing", "severidade": "MEDIO"},
    {"tipo": "ransomware", "severidade": "CRITICO"},
]

saida = os.path.join(os.path.dirname(__file__), "..", "prints", "relatorio.txt")
with open(saida, "w") as f:
    for i in incidentes:
        f.write(f"{i['tipo']} - {i['severidade']}\n")

print("Relatorio gerado em:", os.path.relpath(saida))
print(open(saida).read(), end="")
