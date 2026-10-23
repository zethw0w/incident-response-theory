#!/usr/bin/env python3
"""IR p1 - Parte 8 - Ex 1: Analisar um .log externo (auth.log) em vez de lista fixa.
NIST: Deteccao e Analise + Correlacao de Eventos."""
import os
from collections import Counter

BASE = os.path.join(os.path.dirname(__file__), "..", "dados", "auth.log")

with open(BASE) as f:
    linhas = f.readlines()

ips_falha = [l.split()[-1] for l in linhas if "login_fail" in l]
contagem = Counter(ips_falha)

for ip, qtd in contagem.items():
    if qtd >= 5:
        print(f"[ALERTA] Forca bruta detectada: {ip} ({qtd} tentativas)")
