# Resposta a Incidentes & Segurança da Informação — Respostas Teóricas

Baseado no **NIST SP 800-61 Rev. 2** (Computer Security Incident Handling Guide) e nos exercícios do módulo *Defense Operations*.

---

## Parte 1 — Conceitos Fundamentais

**1.1 Diferença entre evento e incidente**
Um **evento** é qualquer ocorrência observável num sistema ou rede (um login, um acesso a arquivo, um pacote de rede). Um **incidente** é um evento — ou conjunto de eventos — que viola, ou ameaça violar, as políticas de segurança, representando risco real à Confidencialidade, Integridade ou Disponibilidade. Todo incidente é um evento; nem todo evento é incidente.

**1.2 Três eventos que não são incidentes**
- Um usuário autenticando com sucesso no horário normal.
- Um backup agendado concluído.
- Uma atualização de software aplicada com êxito.

**1.3 Como um evento evolui para incidente**
Um evento vira incidente quando passa a indicar atividade maliciosa ou violação: por exemplo, "login falho" (evento isolado) → "500 logins falhos do mesmo IP seguidos de um sucesso" (incidente de força bruta com comprometimento).

## Parte 2 — Tríade CIA

**2.1** Confidencialidade (só autorizados acessam), Integridade (dados não são alterados indevidamente), Disponibilidade (sistemas acessíveis quando necessários).

**2.2 Exemplos por pilar**
- Confidencialidade: vazamento de planilha de clientes.
- Integridade: alteração não autorizada de registros financeiros / defacement.
- Disponibilidade: ataque DDoS que derruba o site.

## Parte 3 — Ciclo de Vida (NIST 800-61)

**3.1 As quatro fases:** Preparação → Detecção e Análise → Contenção, Erradicação e Recuperação → Atividade Pós-Incidente.

**3.2 Fase mais importante:** **Preparação** — sem políticas, equipe, ferramentas de log/monitoramento e treino prévios, todas as outras fases ficam caóticas e lentas.

**3.3 Políticas e treinamentos** ocorrem na fase de **Preparação**.

**3.4 Contenção vs. Erradicação:** Contenção = limitar o dano e impedir propagação (isolar máquina, bloquear IP, desativar conta). Erradicação = remover a causa raiz (apagar malware, fechar a vulnerabilidade, resetar credenciais).

## Parte 4 — Detecção e Análise

**4.1 Fontes de detecção:** SIEM/alertas de IDS-IPS, antivírus/EDR, logs (SO, firewall, aplicação), e relatos de usuários; também threat intel e anomalias de rede.

**4.2 Falso positivo:** alerta que aponta atividade maliciosa onde não há — consome tempo da equipe e, em excesso, gera *alert fatigue*.

**4.3 Qualidade dos logs é crítica** porque a análise, a correlação e a prova forense dependem de registros completos, íntegros e com timestamps sincronizados; sem bons logs não se reconstrói a linha do tempo nem se determina o escopo.

## Parte 5 — Estrutura Organizacional

**5.1 Centralizada vs. distribuída:** equipe centralizada (um CSIRT único para toda a organização) favorece padronização; distribuída (times por unidade/região) favorece proximidade e fuso, mas exige coordenação.

**5.2 Papel do jurídico:** orienta sobre obrigações legais (LGPD/GDPR, notificação de vazamento), preservação de evidências para eventual processo, contratos e responsabilização.

**5.3 Terceirizar o SOC** é recomendado quando a organização não tem escala/maturidade para operar 24/7 internamente, falta pessoal especializado, ou o custo de montar a capacidade supera o do serviço gerenciado (MSSP).

## Parte 6 — Comunicação

**6.1 Porta-voz definido** evita mensagens conflitantes, controla a narrativa e garante que apenas informação validada seja divulgada.

**6.2 Riscos de divulgar detalhes técnicos:** dar vantagem ao atacante, expor outras vítimas/vulnerabilidades, comprometer a investigação e gerar pânico ou dano reputacional.

## Parte 7 — Métricas

**7.1 MTTD** (Mean Time To Detect) — tempo médio entre o início do incidente e sua detecção.
**7.2 MTTR** (Mean Time To Respond/Recover) — tempo médio entre a detecção e a contenção/recuperação.
**7.3** Medir tempo de recuperação importa ao negócio porque indisponibilidade = perda financeira, de SLA e de confiança; reduzir o MTTR demonstra maturidade e justifica investimento.

---

## Parte 4 (prática) — Cenários

### Exercício 1 — 500 logins falhos às 02:30 do mesmo IP
1. É **incidente** (ataque de força bruta em andamento).
2. Fase: **Detecção e Análise** (em transição para Contenção).
3. Ações imediatas: bloquear o IP de origem no firewall/WAF, verificar se houve login bem-sucedido após as falhas, forçar reset da conta-alvo, habilitar MFA, preservar os logs.
4. Ferramentas: SIEM, logs de autenticação (`auth.log`/Security.evtx), firewall, fail2ban/Conditional Access.

### Exercício 2 — Phishing com link de redefinição de senha
- **Severidade:** Média a Alta (depende de quantos clicaram).
- **Contenção:** bloquear o domínio/URL no proxy e e-mail gateway, remover as mensagens das caixas (purge), resetar senhas de quem clicou.
- **Comunicação interna:** alertar todos os usuários, SOC, TI e, se houve credencial comprometida, o jurídico/DPO.
- **Prevenção futura:** treino de conscientização, DMARC/SPF/DKIM, MFA, simulações de phishing.

### Exercício 3 — Planilha de clientes exposta publicamente
1. Pilar afetado: **Confidencialidade**.
2. Acionar: SOC, DPO/jurídico (LGPD), dono do dado, comunicação.
3. Fase crítica: **Contenção** (remover o compartilhamento imediatamente) e, pela LGPD, avaliação de notificação à ANPD/titulares.
4. Recuperação: revogar links, revisar permissões, auditar quem acessou, rotacionar credenciais expostas.

### Exercício 4 — Ransomware com tela de resgate
- **Contenção imediata:** isolar as máquinas da rede (sem desligar, para preservar memória/chaves), bloquear o C2.
- **Erradicação:** identificar a variante e o vetor, remover o malware, corrigir a vulnerabilidade de entrada, resetar credenciais.
- **Recuperação:** restaurar de backups offline validados, monitorar reinfecção.
- **Lições aprendidas:** por que o backup/segmentação falhou, reforçar EDR e detecção.
- **Pagar o resgate não é recomendado:** não garante a chave, financia o crime e pode ter implicações legais.

### Exercício 6 — Classificação rápida
- Porta 22 aberta externamente → **Evento** (configuração; vira incidente se explorada).
- Funcionário perdeu notebook → **Incidente** (risco a dados, Confidencialidade).
- Tentativas de login falhas repetidas → **Incidente** (força bruta) ou evento, conforme volume.
- Atualização de sistema falhou → **Evento** (operacional, não é segurança).
- E-mail com link suspeito → **Incidente** (phishing) a ser triado.

---

*Referência: NIST SP 800-61 Rev. 2 — https://csrc.nist.gov/pubs/sp/800/61/r2/final*
