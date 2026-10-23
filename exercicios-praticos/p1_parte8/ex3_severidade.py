#!/usr/bin/env python3
"""IR p1 - Parte 8 - Ex 3: Classificacao de severidade (NIST: priorizacao de incidentes)."""


def severidade(evento):
    if evento == "ransomware":
        return "CRITICO"
    if evento == "vazamento_dados":
        return "ALTO"
    if evento == "phishing":
        return "MEDIO"
    return "BAIXO"


eventos = ["phishing", "login_fail", "ransomware", "vazamento_dados"]

for e in eventos:
    print(f"{e:<16} -> {severidade(e)}")
