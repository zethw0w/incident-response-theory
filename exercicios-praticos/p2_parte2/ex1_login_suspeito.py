#!/usr/bin/env python3
"""IR p2 - Parte 2 - Ex 1: Deteccao de tentativas de login suspeitas (forca bruta).
Respostas: IP suspeito = 192.168.0.10 (3 falhas); e um INCIDENTE (forca bruta em andamento);
acao de contencao = bloquear o IP e forcar reset/MFA da conta-alvo."""

logs = [
    "2026-02-10 10:01:23 LOGIN_FAIL 192.168.0.10",
    "2026-02-10 10:01:25 LOGIN_FAIL 192.168.0.10",
    "2026-02-10 10:01:29 LOGIN_SUCCESS 10.0.0.2",
    "2026-02-10 10:02:10 LOGIN_FAIL 192.168.0.10",
    "2026-02-10 10:03:11 LOGIN_FAIL 172.16.0.5",
]

tentativas = {}
for linha in logs:
    partes = linha.split()
    status, ip = partes[2], partes[3]
    if status == "LOGIN_FAIL":
        tentativas[ip] = tentativas.get(ip, 0) + 1

for ip, qtd in tentativas.items():
    if qtd >= 3:
        print(f"Possivel ataque de forca bruta: {ip} ({qtd} falhas)")
