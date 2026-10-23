# Resposta a Incidentes (p1) — Estrutura de Equipe, Plano de IR e Reflexão

Complementa [`RESPOSTAS.md`](RESPOSTAS.md) e [`EXERCICIOS-PRATICOS.md`](EXERCICIOS-PRATICOS.md). Base: NIST SP 800-61 Rev. 2.

> As Partes 1 e 2 do roteiro p1 são dinâmicas interativas no Menti, aplicadas em sala pelo professor. Não têm resposta escrita, então não estão aqui.

---

## Parte 4 — Exercício Prático 5: Estrutura de Equipe

**Situação:** empresa pequena, atacada com frequência, sem equipe dedicada.

**Modelo de equipe adequado:** equipe **mista**, com um responsável interno de segurança (pode ser o gestor de TI acumulando o papel) e **SOC/MDR terceirizado** para monitoramento 24x7. Montar um CSIRT próprio é caro e inviável nesse porte. Terceirizar tudo faz a empresa perder o contexto do negócio.

**Ferramentas mínimas:**
- EDR/antivírus gerenciado nas estações e servidores.
- Coleta centralizada de logs (SIEM leve ou serviço gerenciado) com relógio sincronizado por NTP.
- Firewall/WAF com logs ativos e MFA em e-mail, VPN e contas administrativas.
- Backups com cópia offline (regra 3-2-1), testados periodicamente.
- Gerenciador de senhas e filtro anti-phishing no e-mail.

**Políticas iniciais:** política de segurança da informação, política de resposta a incidentes (o que é incidente, quem decide, quem comunica), política de senhas/MFA, de backup e de uso aceitável.

**Treinamento essencial:** conscientização para todos (phishing, senhas, relato de incidente) e simulações de phishing recorrentes. Para o responsável de TI, treinamento em triagem de alertas e um exercício de mesa (*tabletop*) por semestre.

---

## Parte 5 — Mini Plano de Resposta a Incidentes

**1. Definição de incidente.** Evento que viola ou ameaça violar as políticas de segurança, afetando confidencialidade, integridade ou disponibilidade (ex.: malware, acesso não autorizado, vazamento, ransomware, DDoS).

**2. Lista de contatos**

| Papel | Responsabilidade | Contato |
|---|---|---|
| Coordenador do incidente (TI/Segurança) | Decide contenção e escalonamento | ramal / celular de plantão |
| SOC/MDR | Detecção, análise, evidências | canal 24x7 do provedor |
| Jurídico / DPO | LGPD, notificação à ANPD e aos titulares | e-mail do DPO |
| Comunicação | Porta-voz único, comunicado interno e externo | assessoria |
| Diretoria executiva | Decisões de impacto ao negócio (ex.: resgate) | diretor responsável |
| Provedores (cloud, ISP, seguro cibernético) | Apoio técnico e acionamento de apólice | contratos |

**3. Ferramentas disponíveis:** EDR, SIEM/logs centralizados, firewall/WAF, gerenciador de backup, sandbox/VirusTotal, ferramentas forenses (cópia da imagem de disco e memória) e canal de comunicação fora de banda.

**4. Fluxo de comunicação**
`Detecção → Analista de plantão abre o chamado → Classifica a severidade → Coordenador é acionado → (Alto/Crítico) Diretoria + Jurídico → Porta-voz comunica → Atualizações em intervalos definidos → Encerramento e relatório`.
Regra: só o porta-voz fala com o público e a imprensa. Detalhes técnicos não saem em canais abertos.

**5. Checklist de resposta**
- [ ] Registrar horário, quem detectou e o sintoma
- [ ] Classificar a severidade (baixa/média/alta/crítica)
- [ ] Preservar evidências (logs, imagem de memória/disco) antes de limpar
- [ ] Conter: isolar o host, bloquear IP/domínio, desativar conta
- [ ] Erradicar: remover malware, corrigir a vulnerabilidade, resetar credenciais
- [ ] Recuperar: restaurar de backup validado e monitorar reinfecção
- [ ] Avaliar notificação legal (LGPD) com o jurídico
- [ ] Reunião de lições aprendidas e atualização do plano

**6. Métricas de sucesso:** MTTD e MTTR (reduzir a cada trimestre), % de incidentes contidos em até X horas, taxa de cliques em simulações de phishing, % de backups restaurados com sucesso nos testes e nº de incidentes recorrentes.

---

## Parte 6 — Exercício de Reflexão

**1. O que aconteceria se a fase de pós-incidente fosse ignorada?**
A organização repete os mesmos erros. A causa raiz continua aberta, o processo e as políticas não evoluem e as métricas (MTTD/MTTR) não melhoram. O mesmo ataque, ou um parecido, volta a funcionar.

**2. Qual o maior risco de não documentar incidentes?**
Perder o **aprendizado e a prova**. Sem registro não há linha do tempo para a análise de causa raiz, nem evidência para uma ação jurídica, nem como demonstrar conformidade (LGPD, auditoria). Também não é possível medir a evolução, e quando a equipe muda o conhecimento vai embora junto.

**3. Segurança é mais técnica ou mais processual? Justifique.**
É **processual com suporte técnico**. A tecnologia detecta e bloqueia, mas quem define o que é incidente, quem decide, quem comunica e como aprende é o **processo**. Na prática a maioria dos incidentes explora falha humana ou de processo: phishing, senha fraca, falta de patch e backup sem teste. Uma ferramenta excelente sem processo de resposta falha na hora do incidente. Um bom processo com ferramentas modestas ainda responde de forma organizada. É por isso que o NIST estrutura o ciclo em fases e papéis, e não em produtos.
