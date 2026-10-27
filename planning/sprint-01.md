# Sprint 01 — fundação

Objetivo: tornar o build reproduzível, medir a base e permitir desenvolvimento com fixtures sem dependência de uma conta real. Horizonte proposto: dez dias úteis após disponibilizar o ambiente; sem equipe real ainda atribuída.

| Ordem | Item | Dono por função | Próxima ação / saída |
|---|---|---|---|
| 1 | NO-001 | Android/lead | Instalar JDK 21 + SDK, executar checks e guardar APK/hash |
| 2 | NO-004 | Release/analista | Inventário de licença e links/ativos herdados |
| 3 | NO-003 | Lead/analista | Decisão documentada sobre auth/API atual; pode rodar em paralelo à preparação |
| 4 | NO-005 | Design/Nate | Validar três fluxos com dados fictícios |
| 5 | NO-006 | Lead | Vincular origin conhecido, executar CI e configurar regras de branch |
| 6 | NO-002 | QA | Baseline no aparelho após NO-001; sem números inventados |
| 7 | NO-007 | Android dados | Definir gateway testável sem alterar todos os endpoints |
| 8 | NO-008 | QA/dados | Fixtures e servidor simulado para paginação/erros/eventos |

A preparação já contém documentação, scripts, identidade de desenvolvimento e workflow. Build standardDebug, testes unitários e lint já passaram no destino (ver docs/development/VALIDATION.md). NO-001 ainda exige registrar APK/hash do baseline; NO-006 ainda exige decidir e configurar as regras de branch com os checks reais. Todos os IDs permanecem Backlog até refinamento/atribuição pelo time.

Primeira fatia de implementação após fundação: lista de amigos alimentada por repository fake, estados inicial/cache/refresh/erro parcial, IDs estáveis e teste que demonstre que recomendações lentas não bloqueiam a lista. Não iniciar por troca de toda a navegação, iconografia final ou módulos.

Gate G0: build demonstrado, baseline com protocolo, inventário inicial e decisão de API registrada. Quando autenticação não estiver resolvida, prosseguir em fixtures e registrar claramente o limite.

## Atualização com evidência — 27/10/2026

- NO-001: Done para build smoke; baseline do SHA 5761edde registrada com hash do
  APK, comandos e limites em [NO-001-baseline](../docs/development/NO-001-baseline.md).
  A exigência anterior de registrar APK/hash está atendida; NO-002 segue pendente.
- NO-004: In Progress; [inventário inicial](../docs/development/NO-004-inventory.md)
  entregue. Licenças transitivas, proveniência de ativos e avisos empacotados ainda
  exigem revisão. As demais tarefas conservam seus estados. G0 permanece aberto.

- NO-007: In Progress; [contrato de leitura de amigos](../docs/development/NO-007-friends-contract.md),
  fake e adapter com doze testes de contrato aprovados. Falta migrar o ScreenModel;
  nenhuma integração autenticada ou tela fake foi habilitada nesta fatia.
