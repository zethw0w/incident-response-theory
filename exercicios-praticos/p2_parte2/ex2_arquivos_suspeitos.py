#!/usr/bin/env python3
"""IR p2 - Parte 2 - Ex 2: Analise de integridade por hash.
Respostas: isolar 'sistema.exe' (hash fora da allowlist); fase NIST = Deteccao/Analise;
evidencias a registrar = hash, caminho, timestamps, usuario, origem do arquivo."""

arquivos = {
    "relatorio.pdf": "abc123",
    "financeiro.xlsx": "def456",
    "sistema.exe": "zzz999",
}

hashes_legitimos = ["abc123", "def456"]

for nome, h in arquivos.items():
    if h not in hashes_legitimos:
        print(f"Arquivo suspeito detectado: {nome} (hash {h} nao esta na allowlist)")
