# Roadmap, capacidade e riscos

## Capacidade e horizonte

Hipótese: dois devs Android, 1 QA, analista e designer parciais, lead acumulado por um dev. Planejar 70% da capacidade nominal para histórias; 30% para revisão, integração, bugs e descoberta. Faixa inicial 12–16 semanas para MVP pessoal, sujeita a política/API e estado do build. Uma pessoa sozinha: expectativa inicial de 5–8 meses em dedicação substancial, sem compromisso de prazo. Valores monetários dependem de taxas reais; orçamento = dias por papel × diária + aparelhos/serviços aprovados. Sem compra automática.

| Etapa | Janela indicativa | Entrega/gate | Paralelismo seguro |
|---|---|---|---|
| Fundação | Semanas 1–2 | G0: baseline, build, inventário e decisão API | Design/analista trabalham com dados fictícios |
| Dados e sessão | Semanas 3–4 | G1: banco, contratos, sync simulada e segredo isolado | UI de amigos com repository fake |
| Amigos | Semanas 5–6 | Busca, filtros, categorias, pins e snapshot incremental | Mundo prepara estados separados |
| Mundos | Semanas 7–8 | G2: detalhes progressivos, instâncias e coleções | QA de lifecycle e migração |
| Feed e consolidação | Semanas 9–10 | Feed paginado, configurações, diagnósticos e acessibilidade | Revisor/perf valida fluxos anteriores |
| Beta pessoal | Semanas 11–12 | G3: uso diário, regressão e correções | Designer finaliza ativos |
| Contingência/1.0 | Semanas 13–16 | G4: versão pessoal assinada e rollback | Alertas só se gates anteriores concluídos |

Pós-1.0: alertas seletivos, acompanhamento opcional, importação/exportação, edição remota e recomendações. Não encaixar todo pós-MVP na contingência. Estimativas S/M/L no backlog são relativas e devem ser refinadas com dados do time.

## Caminho crítico

Baseline e viabilidade → contratos/sessão → Room e sincronização → amigos/mundos → testes integrados → release. Marca e protótipo podem avançar paralelamente. Se autenticação não estiver resolvida, demonstrar MVP com fixtures; não apresentar isso como produto conectado pronto.

## Riscos

| Risco | Probabilidade/impacto inicial | Responsável | Mitigação e gatilho |
|---|---|---|---|
| Regras de credenciais/API incompatíveis | Alta/alto | PO + lead | Spike em G0; decisão escrita; sem assumir que Apache resolve API |
| API muda formato sem aviso | Alta/alto | Dados | Adapter + testes de contrato + erro parcial; monitorar upstream semanalmente |
| Carga/reconexão consome bateria | Média/alto | Lead/QA | Background após MVP, medição física e opt-in |
| Dados antigos parecem atuais | Alta/alto | UX/Dados | observedAt e lacunas obrigatórias |
| Importação corrompe dados | Média/alto | Dados/QA | Somente formato conhecido, staging/transação e backup |
| Rebranding vira reescrita total | Média/alto | Lead | PRs verticais e manutenção da stack inicial |
| Escopo cresce com extras do upstream | Alta/médio | PO | Lista explícita de fora de escopo e corte por marco |
| Nome/ícone conflita com terceiro | Desconhecida/médio | PO/design | Verificação antes de distribuição, nome provisório |
| Falta aparelho/tester | Média/médio | PO/QA | Reservar capacidade G0; não substituir bateria por emulador |
| Fork diverge e perde correções | Média/alto | Lead | Revisão upstream regular e cherry-pick testado |

## Primeiros dez dias úteis

Dias 1–2: baseline fixado, build sem release público, documentos de licenças e tarefas refinadas. Dias 3–4: medição e protótipo de tarefas; spike de autenticação e contratos. Dias 5–6: fixtures, CI local do fork e fronteira do gateway. Dias 7–8: schema Room, reducer de eventos e UI fake. Dias 9–10: demonstração de amigos com cache, revisão de risco e reestimativa. Saída: plano calibrado, não apenas scaffold vazio.
