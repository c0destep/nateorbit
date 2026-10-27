---
name: nateorbit-plan-task
description: Refinar tarefas NateOrbit com dependências, critérios verificáveis e handoff. Usar ao preparar uma história ou escolher a próxima fatia da sprint.
---

# Preparar uma tarefa

Ler AGENTS.md, planning/sprint-01.md e o item em planning/backlog.json.
Consultar os documentos de produto/arquitetura pertinentes em docs/planning/.

- Inspecionar o fluxo existente antes de desenhar a alteração. Diferenciar estado
  implementado de arquitetura planejada. Identificar IDs e dependências bloqueadoras.
- Definir problema, resultado observável, limite da fatia e cenários de falha.
  Priorizar fixtures e contratos enquanto NO-003/NO-009 estiverem pendentes.
- Selecionar testes por comportamento; para performance, definir medição comparável,
  aparelho/build e dados sintéticos. Não inventar números ou estimativas cumpridas.
- Usar docs/templates/historia.md ou docs/templates/handoff.md conforme a saída.
  Separar responsabilidade de análise, implementação, revisão e QA; não presumir
  que há pessoas atribuídas ou subagentes disponíveis.
- Se atualizar backlog, manter JSON, CSV e dependências coerentes. Rodar make verify.

Entregar uma tarefa executável com aceite, evidência esperada e próxima ação.
