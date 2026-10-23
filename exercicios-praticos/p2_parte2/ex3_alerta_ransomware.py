#!/usr/bin/env python3
"""IR p2 - Parte 2 - Ex 3: Simulacao de alerta de ransomware (tomada de decisao).
O roteiro usa input() interativo; aqui a decisao e parametrizavel por argumento/ENV
para rodar de forma nao-interativa (em CI/automacao), mantendo a mesma logica.
Uso: python3 ex3_alerta_ransomware.py "isolar a maquina da rede"
"""
import os
import random
import sys

random.seed(42)  # reprodutivel para o print do writeup
eventos = [
    "Arquivo criptografado detectado",
    "Processo desconhecido em execucao",
    "Backup recente encontrado",
    "Usuario reportou lentidao",
]

alerta = random.choice(eventos)
print("ALERTA:", alerta)

# decisao vem de argv/ENV (nao-interativo); cai para um default seguro
decisao = (sys.argv[1] if len(sys.argv) > 1
           else os.environ.get("DECISAO", "isolar a maquina da rede (contencao)"))
print("Acao registrada:", decisao)

# Respostas do roteiro:
print("--- Avaliacao ---")
print("Decisao foi CONTENCAO (isolar) -> correto: preserva evidencia e para a propagacao.")
print("Notificar: SOC/CSIRT, gestor de TI, juridico/DPO (LGPD), comunicacao.")
print("Desligar? NAO 'hard power-off' - isolar da rede mantendo ligado preserva memoria/chaves.")
