#!/usr/bin/env python3
"""IR p1 - Parte 7 - Ex 3: Detectar acessos externos a arquivos confidenciais
(Pilar afetado: Confidencialidade | Fase: Contencao)."""

acessos = [
    {"usuario": "joao", "arquivo": "clientes.xlsx", "origem": "interna"},
    {"usuario": "maria", "arquivo": "financeiro.xlsx", "origem": "externa"},
    {"usuario": "ana", "arquivo": "publico.pdf", "origem": "externa"},
]

for a in acessos:
    if a["origem"] == "externa" and "xlsx" in a["arquivo"]:
        print("Possivel vazamento:", a)
