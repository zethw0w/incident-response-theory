#!/usr/bin/env python3
"""IR p1 - Parte 7 - Ex 1: Deteccao de forca bruta em logs (NIST: Deteccao e Analise).
Identifica multiplas tentativas de login falhas a partir de uma lista de logs."""
from collections import Counter

logs = [
    "2026-01-01 10:00:01 login_fail 192.168.0.10",
    "2026-01-01 10:00:05 login_fail 192.168.0.10",
    "2026-01-01 10:00:07 login_success 192.168.0.20",
    "2026-01-01 10:00:09 login_fail 192.168.0.10",
    "2026-01-01 10:00:12 login_fail 192.168.0.10",
]

ips = [log.split()[-1] for log in logs if "login_fail" in log]
contagem = Counter(ips)

for ip, tentativas in contagem.items():
    if tentativas >= 3:
        print(f"ALERTA: Possivel forca bruta do IP {ip} ({tentativas} falhas)")
