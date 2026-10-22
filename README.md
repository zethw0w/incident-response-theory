# Resposta a Incidentes & Segurança da Informação — Teoria

Respostas dos exercícios **teóricos e de simulação** do módulo de Resposta a Incidentes (Defense Operations / FIAP), baseados no **NIST SP 800-61 Rev. 2**.

## Conteúdo

- **[RESPOSTAS.md](RESPOSTAS.md)** — conceitos fundamentais (evento × incidente, tríade CIA), as 4 fases do NIST, detecção/análise, estrutura organizacional, comunicação, métricas (MTTD/MTTR) e os cenários práticos (força bruta, phishing, vazamento, ransomware, classificação rápida).
- **[SEGURANCA-INFORMACAO.md](SEGURANCA-INFORMACAO.md)** — por que inventariar ativos antes de proteger, e 3 motivações (LGPD/confidencialidade, continuidade/disponibilidade, integridade/reputação).
- **`scripts/`** — mini-laboratórios em Python propostos no roteiro:
  - `mini_siem.py` — correlaciona logs de firewall/auth/antivírus, pontua risco por IP e classifica severidade (CRÍTICO/ALTO/MÉDIO).
  - `detecta_bruteforce.py` — detecção de força bruta por contagem de falhas por IP.

## Estrutura
`prints/` — saída dos scripts Python (mini-SIEM e detecção de força bruta).
