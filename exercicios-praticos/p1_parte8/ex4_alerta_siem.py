#!/usr/bin/env python3
"""IR p1 - Parte 8 - Ex 4: Alerta automatico (simulacao de SIEM).
Evolui para e-mail (smtplib) ou bot de Telegram/Slack."""


def alerta(msg):
    print(f"[ALERTA SOC] {msg}")


tentativas = 12

if tentativas > 10:
    alerta(f"Possivel ataque de forca bruta detectado ({tentativas} tentativas)")
