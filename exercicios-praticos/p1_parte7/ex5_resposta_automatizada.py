#!/usr/bin/env python3
"""IR p1 - Parte 7 - Ex 5: Acao de contencao automatica (NIST: Contencao / automacao de resposta)."""

ip_suspeito = "192.168.0.10"


def bloquear_ip(ip):
    # Em producao: subprocess para iptables/nftables, API do firewall, EDR, etc.
    print(f"Firewall: IP {ip} bloqueado com sucesso.")


bloquear_ip(ip_suspeito)
