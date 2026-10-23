# Exercícios Práticos de Resposta a Incidentes (p1 e p2)

Resolução das **partes práticas** dos roteiros *Resposta-a-incidentes-Exercícios-p1* e *p2* (Defense Operations / FIAP), baseadas no **NIST SP 800-61 Rev. 2**. Inclui os cenários dissertativos e **todos os mini-laboratórios em Python** — executáveis, com saída real capturada em `exercicios-praticos/prints/`.

As respostas teóricas (Parte 3 do p1) e os cenários da Parte 4 estão em [`RESPOSTAS.md`](RESPOSTAS.md); aqui ficam os cenários que faltavam do **p2 Parte 1** e os códigos das Partes 7/8 (p1) e 2/3 (p2).

---

## p2 — Parte 1: Simulações (cenários dissertativos)

### Exercício 1 — Alerta de malware em estação do financeiro (10:15)
- **Classificação:** **Médio a Alto** (host de setor sensível; depende se executou/propagou).
- **Primeira ação (≤5 min):** **isolar o host da rede** (desconectar cabo/Wi-Fi) sem desligar, para conter e preservar memória.
- **Evidências a coletar:** hash do arquivo, caminho, logs do AV/EDR, logs de processo (Sysmon), conexões de rede, timestamps, usuário logado.
- **Quem notificar:** SOC/CSIRT, gestor de TI e, se houver dado pessoal, o DPO/jurídico.
- **Desligar?** **Não** — isolar da rede mantendo ligado preserva artefatos voláteis (memória, processos, chaves).

### Exercício 2 — Vazamento de credenciais (acessos indevidos em e-mail corporativo)
- **Logs a analisar:** autenticação (login, IP, geolocalização, MFA), logs do provedor de e-mail (M365/Google), VPN, acessos a aplicações SSO.
- **Sistemas possivelmente comprometidos:** caixas de e-mail, SSO/IdP, qualquer app federado, e serviços onde a senha foi reutilizada.
- **Contenção imediata:** forçar reset de senha das contas afetadas, revogar sessões/tokens, **ativar MFA**, bloquear IPs/regras maliciosas, procurar regras de encaminhamento maliciosas criadas pelo atacante.
- **Comunicação externa:** **sim, pode haver obrigação** — se dados pessoais foram expostos, a LGPD exige avaliação de notificação à ANPD e aos titulares.

### Exercício 3 — Ransomware em servidor de arquivos
- **Isolar ou manter ligado?** **Isolar da rede** imediatamente (sem hard power-off, para preservar memória/chaves).
- **Restaurar backup já ou investigar antes?** **Investigar antes** — identificar variante, vetor de entrada e escopo; restaurar só após garantir erradicação, senão reinfecta.
- **Equipes:** CSIRT/SOC, infra/backup, jurídico/DPO, comunicação e, se necessário, suporte externo/seguro cibernético.
- **Riscos de pagar o resgate:** não garante a chave, financia o crime, pode violar sanções legais, e marca a organização como pagadora (alvo recorrente).

### Exercício 4 — DDoS no site corporativo
- **É incidente de disponibilidade** (pilar **Disponibilidade** da CIA); pode ser cortina de fumaça para outro ataque.
- **Medidas técnicas imediatas:** acionar proteção anti-DDoS/CDN (Cloudflare/WAF), rate limiting, geo/IP blocking, scaling, blackhole/scrubbing com o provedor.
- **Comunicação:** acionar o provedor de hospedagem/upstream e a operadora; comunicar status interno e, se necessário, público (página de status).
- **Evidências:** capturas de tráfego, logs do WAF/CDN, volumetria, IPs de origem, timeline.

### Exercício 5 — Pós-incidente de phishing (Lessons Learned)
- **Relatório executivo (1 pág):** o que aconteceu, impacto, ações tomadas, tempo de resposta (MTTD/MTTR), status final.
- **3 melhorias de processo:** (1) treinamento/simulação de phishing recorrente; (2) DMARC/SPF/DKIM + MFA obrigatório; (3) playbook de resposta a phishing com purge automático de mensagens.
- **Métrica de prevenção:** taxa de cliques em simulações de phishing (meta decrescente) e tempo de contenção.
- **Falha raiz:** ausência de filtro/treino que permitiu o clique e a entrega da credencial.

### Exercício 6 — Classificação rápida (Evento / Incidente / Falso Positivo)
| Item | Classificação |
|---|---|
| Porta 22 aberta externamente | **Evento** (exposição/config; vira incidente se explorada) |
| Funcionário perdeu notebook | **Incidente** (risco à Confidencialidade) |
| Tentativas de login falhas repetidas | **Incidente** (força bruta) — ou evento, conforme volume |
| Atualização de sistema falhou | **Falso Positivo** / evento operacional (não é segurança) |
| E-mail com link suspeito | **Incidente** (phishing) a triar |

---

## p1 — Parte 7: Simulações em Python (`exercicios-praticos/p1_parte7/`)

| Script | O que faz | Resposta / Fase NIST |
|---|---|---|
| `ex1_bruteforce.py` | Conta `login_fail` por IP | Alerta p/ `192.168.0.10` (4 falhas) — Detecção/Análise |
| `ex2_malware_extensao.py` | Filtra `.exe/.scr/.bat` | `invoice.exe`, `atualizacao.scr`, `notasfiap.bat` — Detecção |
| `ex3_vazamento.py` | Acesso externo a `.xlsx` | `maria/financeiro.xlsx` — Confidencialidade/Contenção |
| `ex4_metricas_mttd_mttr.py` | Calcula MTTD/MTTR | MTTD=2h, MTTR=6h — Pós-Incidente |
| `ex5_resposta_automatizada.py` | Bloqueia IP (função) | Contenção/automação |

## p1 — Parte 8: "Vamos evoluir?" (`exercicios-praticos/p1_parte8/`)

| Script | O que faz |
|---|---|
| `ex1_ler_log_real.py` | Lê `dados/auth.log` real → alerta `192.168.0.10` (6 tentativas) |
| `ex2_pandas.py` | Lê `dados/logs.csv` com pandas → ranking de IPs por `login_fail` |
| `ex3_severidade.py` | Classifica eventos em CRÍTICO/ALTO/MÉDIO/BAIXO |
| `ex4_alerta_siem.py` | Dispara alerta SOC acima de limiar |
| `ex5_dashboard.py` | Gráfico de incidentes por tipo (matplotlib → `prints/dashboard_incidentes.png`) |
| `ex6_relatorio.py` | Gera `prints/relatorio.txt` |

## p2 — Parte 2: Mini-laboratórios (`exercicios-praticos/p2_parte2/`)
- `ex1_login_suspeito.py` — força bruta: **IP suspeito `192.168.0.10`**; é **incidente**; contenção = bloquear IP + reset/MFA.
- `ex2_arquivos_suspeitos.py` — integridade por hash: isolar **`sistema.exe`** (fora da allowlist); fase **Detecção**.
- `ex3_alerta_ransomware.py` — decisão: **contenção (isolar)**, notificar CSIRT/jurídico, **não** fazer hard power-off (versão não-interativa para rodar em CI).

## p2 — Parte 3: Mini-SIEM completo (`exercicios-praticos/p2_parte3/mini_siem_completo.py`)
Correlaciona **firewall + autenticação + antivírus** e implementa **todas as evoluções** do roteiro:
- **horário nos logs + janela de tempo** (só últimos 5 min);
- **ranking de IPs** por score de risco;
- **bloqueio automático** para severidade CRÍTICA;
- **exportação CSV** (`prints/mini_siem_relatorio.csv`);
- **falso positivo** tratado via allowlist (`172.16.0.8` ignorado).

Saída: `10.0.0.5` → score **16** → **CRÍTICO** (2×LOGIN_FAIL + MALWARE), bloqueado automaticamente. É **incidente** porque três fontes distintas convergem no mesmo IP (correlação reduz falso positivo).

---

### Como rodar
```bash
python3 exercicios-praticos/p1_parte7/ex1_bruteforce.py
python3 exercicios-praticos/p2_parte3/mini_siem_completo.py
# (ex2_pandas e ex5_dashboard requerem: pip install pandas matplotlib)
```
