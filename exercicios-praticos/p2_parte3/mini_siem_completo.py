#!/usr/bin/env python3
"""IR p2 - Parte 3: Mini-SIEM de Resposta a Incidentes (NIST 800-61).
Correlaciona firewall + autenticacao + antivirus, pontua risco por IP, classifica
severidade e implementa TODAS as evolucoes propostas no roteiro:
  - horario nos logs e janela de tempo (ultimos 5 min)
  - ranking de IPs
  - funcao de bloqueio automatico
  - exportacao de relatorio em CSV
  - tratamento de falso positivo (allowlist)
"""
import csv
import os
from collections import defaultdict
from datetime import datetime, timedelta

# ---- Logs de 3 fontes, agora COM horario (evolucao) ----
AGORA = datetime(2026, 2, 10, 10, 5, 0)
logs_firewall = [
    ("10.0.0.5", "ALLOW", "2026-02-10 10:01:00"),
    ("192.168.1.10", "BLOCK", "2026-02-10 10:02:00"),
    ("10.0.0.5", "ALLOW", "2026-02-10 10:03:00"),
    ("203.0.113.9", "BLOCK", "2026-02-10 09:30:00"),  # fora da janela de 5 min
]
logs_auth = [
    ("10.0.0.5", "LOGIN_FAIL", "2026-02-10 10:01:30"),
    ("10.0.0.5", "LOGIN_FAIL", "2026-02-10 10:02:30"),
    ("172.16.0.8", "LOGIN_SUCCESS", "2026-02-10 10:02:45"),
]
logs_antivirus = [
    ("10.0.0.5", "MALWARE_DETECTED", "2026-02-10 10:04:00"),
]

pesos = {"BLOCK": 2, "LOGIN_FAIL": 3, "MALWARE_DETECTED": 10}
ALLOWLIST = {"172.16.0.8"}            # IPs confiaveis -> trata falso positivo
JANELA = timedelta(minutes=5)         # so considera eventos dos ultimos 5 min


def dentro_da_janela(ts):
    return AGORA - datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") <= JANELA


score = defaultdict(int)
for fonte in (logs_firewall, logs_auth, logs_antivirus):
    for ip, evento, ts in fonte:
        if ip in ALLOWLIST:
            continue                  # falso positivo: ignora IP confiavel
        if not dentro_da_janela(ts):
            continue                  # fora da janela de 5 min
        score[ip] += pesos.get(evento, 0)


def nivel(s):
    return "CRITICO" if s >= 12 else "ALTO" if s >= 6 else "MEDIO"


def bloquear_ip(ip):
    print(f"   [ACAO] Firewall: IP {ip} bloqueado automaticamente.")


# ---- Ranking de IPs por risco ----
ranking = sorted(score.items(), key=lambda x: -x[1])
print("=== Mini-SIEM - Ranking de risco (ultimos 5 min) ===")
for pos, (ip, s) in enumerate(ranking, 1):
    print(f"{pos}. IP: {ip:<14} Score: {s:<3} Severidade: {nivel(s)}")
    if nivel(s) == "CRITICO":
        bloquear_ip(ip)              # bloqueio automatico so para CRITICO

# ---- Exporta relatorio CSV ----
saida = os.path.join(os.path.dirname(__file__), "..", "prints", "mini_siem_relatorio.csv")
with open(saida, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["posicao", "ip", "score", "severidade"])
    for pos, (ip, s) in enumerate(ranking, 1):
        w.writerow([pos, ip, s, nivel(s)])
print("\nRelatorio CSV exportado em:", os.path.relpath(saida))

# ---- Respostas do roteiro ----
print("\n--- Respostas ---")
print("Maior risco: 10.0.0.5 (score 16 = 2xLOGIN_FAIL(6) + MALWARE(10); ALLOW pesa 0) -> CRITICO.")
print("E um INCIDENTE: multiplas fontes (firewall+auth+AV) convergem no mesmo IP.")
print("Multiplas fontes aumentam a severidade porque reduzem falso positivo (correlacao).")
print("Um unico malware ja justifica severidade alta, mas a correlacao eleva a CRITICO.")
print("Acao: bloquear o IP e ISOLAR a maquina; 172.16.0.8 foi ignorado (allowlist=falso positivo).")
