#!/usr/bin/env python3
"""Deteccao de forca bruta a partir de arquivo de log de autenticacao (NIST: Deteccao e Analise)."""
from collections import Counter
logs = [
 "2026-02-10 10:01:23 LOGIN_FAIL 192.168.0.10","2026-02-10 10:01:25 LOGIN_FAIL 192.168.0.10",
 "2026-02-10 10:01:29 LOGIN_SUCCESS 10.0.0.2","2026-02-10 10:02:10 LOGIN_FAIL 192.168.0.10",
 "2026-02-10 10:03:11 LOGIN_FAIL 192.168.0.10",
]
tent = Counter(l.split()[3] for l in logs if "LOGIN_FAIL" in l)
for ip, n in tent.items():
    if n >= 3:
        print(f"[ALERTA] Possivel forca bruta: {ip} ({n} falhas)")
