#!/usr/bin/env python3
"""Mini-SIEM (NIST 800-61) — correlaciona logs de firewall, autenticacao e antivirus,
pontua risco por IP e classifica severidade. Exercicio Parte 3 de Resposta a Incidentes."""
from collections import defaultdict

logs_firewall = [("10.0.0.5","ALLOW"),("192.168.1.10","BLOCK"),("10.0.0.5","ALLOW")]
logs_auth     = [("10.0.0.5","LOGIN_FAIL"),("10.0.0.5","LOGIN_FAIL"),("172.16.0.8","LOGIN_SUCCESS")]
logs_av       = [("10.0.0.5","MALWARE_DETECTED")]

pesos = {"BLOCK":2, "LOGIN_FAIL":3, "MALWARE_DETECTED":10}
score = defaultdict(int)
for fonte in (logs_firewall, logs_auth, logs_av):
    for ip, ev in fonte:
        score[ip] += pesos.get(ev, 0)

print(f"{'IP':<16}{'Score':<7}Severidade")
for ip, s in sorted(score.items(), key=lambda x:-x[1]):
    nivel = "CRITICO" if s >= 12 else "ALTO" if s >= 6 else "MEDIO"
    print(f"{ip:<16}{s:<7}{nivel}")
