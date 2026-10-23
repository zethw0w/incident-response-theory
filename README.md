# Resposta a Incidentes & Segurança da Informação — Teoria

Respostas dos exercícios **teóricos e de simulação** do módulo de Resposta a Incidentes (Defense Operations / FIAP), baseados no **NIST SP 800-61 Rev. 2**.

## Conteúdo

- **[RESPOSTAS.md](RESPOSTAS.md)** — conceitos fundamentais (evento × incidente, tríade CIA), as 4 fases do NIST, detecção/análise, estrutura organizacional, comunicação, métricas (MTTD/MTTR) e os cenários práticos (força bruta, phishing, vazamento, ransomware, classificação rápida).
- **[EXERCICIOS-PRATICOS.md](EXERCICIOS-PRATICOS.md)** — resolução das **partes práticas dos roteiros p1 e p2**: os 6 cenários dissertativos do p2 (malware em estação, vazamento de credenciais, ransomware, DDoS, pós-incidente, classificação) e **todos os mini-laboratórios em Python** (p1 Parte 7/8 e p2 Parte 2/3), executáveis e com saída real.
- **[SEGURANCA-INFORMACAO.md](SEGURANCA-INFORMACAO.md)** — por que inventariar ativos antes de proteger, e 3 motivações (LGPD/confidencialidade, continuidade/disponibilidade, integridade/reputação).
- **`scripts/`** — mini-SIEM e detecção de força bruta (versão inicial).
- **`exercicios-praticos/`** — todos os exercícios Python dos roteiros p1 e p2, organizados por parte:
  - `p1_parte7/` (5 scripts) — força bruta, malware por extensão, vazamento, MTTD/MTTR, bloqueio automático.
  - `p1_parte8/` (6 scripts) — ler log real, pandas, severidade, alerta SIEM, dashboard (matplotlib), relatório TXT.
  - `p2_parte2/` (3 scripts) — login suspeito, integridade por hash, decisão de ransomware.
  - `p2_parte3/` — **mini-SIEM completo** com janela de tempo, ranking, CSV, bloqueio automático e tratamento de falso positivo.
  - `dados/` — logs de exemplo (`auth.log`, `logs.csv`); `prints/` — saídas e dashboard.

## Estrutura
`prints/` — saída dos scripts da versão inicial; `exercicios-praticos/prints/` — saídas dos exercícios p1/p2 (incluindo `dashboard_incidentes.png` e `mini_siem_relatorio.csv`).
