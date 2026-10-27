---
name: nateorbit-sync-review
description: Revisar sincronização, cache, paginação, WebSocket e sessão do NateOrbit. Usar em mudanças desses fluxos ou em uma revisão de concorrência e perda de dados.
---

# Revisar rede, cache e sessão

Ler AGENTS.md e o diff completo. Consultar docs/planning/03-arquitetura-e-dados.md,
09-qualidade-e-testes.md e 11-seguranca-licencas-release.md em docs/planning/ somente
quando afetados. Examinar os chamadores e o caminho até a UI, não só a função editada.

Verificar cenários pertinentes à alteração:

- Página posterior falha: preservar dados válidos; não interpretar snapshot incompleto
  como remoção dos amigos ausentes. Distinguir erro, vazio e dado parcial.
- Evento chega durante snapshot: evitar reversão para estado antigo; limitar dedupe
  e manter um escritor. Evento desconhecido/malformado não derruba a sessão.
- Logout ou troca de conta durante request/reconexão: cancelar jobs e descartar
  respostas de geração antiga, inclusive callbacks que chegam depois do cancelamento.
- 429: respeitar Retry-After válido, recuo limitado e cancelamento. Reconexão não
  pode criar jobs duplicados. Não repetir automaticamente convite ou outra mutação
  de resultado desconhecido após timeout.
- Cache visível durante refresh; mundo aparece antes das instâncias; amigos não
  aguardam recomendações. Diagnósticos não expõem credenciais/localização privada.
- Migração de dados pessoais é explícita/transacional, sem fallback destrutivo.

Usar fakes/servidor local; não chamar API real para provar esses cenários.
Reportar problemas verificáveis por severidade, arquivo/linha, cenário, impacto e
correção sugerida. Se não houver achados, registrar os limites da revisão e testes.
