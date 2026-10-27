# Equipe, responsabilidades e processo

## Papéis

| Papel | Responsabilidade | Entrega |
|---|---|---|
| Product Owner — Nate | Prioridade, escopo, identidade e aceite de produto | Backlog ordenado e aceite por marco |
| Analista | Regras, cenários, rastreabilidade e restrições de API | Histórias com aceitação e decisões registradas |
| Tech Lead | Arquitetura, contratos, integração e riscos | ADRs e revisão de mudanças estruturais |
| Android A — dados | Sessão, rede, banco e sincronização | Implementação + testes de contratos/estado |
| Android B — experiência | Compose, navegação, acessibilidade e imagens | Telas + testes de fluxos |
| Designer | Pesquisa, protótipo e sistema visual | Especificações de estados e ativos finais |
| Revisor | Revisão independente de comportamento e riscos | Comentários acionáveis e aprovação fundamentada |
| QA/tester | Plano, exploração, regressão e evidências | Relatório de execução e defeitos reproduzíveis |
| Segurança/release | Segredos, licenças, assinatura e distribuição | Checklist com evidências e decisão de release |

Papéis podem ser acumulados, mas ninguém é o único aprovador da própria mudança crítica. Em equipe pequena, reservar explicitamente tempo do segundo desenvolvedor para revisão e do PO para validação. Não há pessoas contratadas ou tarefas atribuídas externamente por este pacote.

## RACI resumido

| Atividade | A — decide | R — executa | C — consulta |
|---|---|---|---|
| Escopo/aceitação | PO | Analista | QA/design/lead |
| Arquitetura | Lead | Android A/B | Segurança/QA |
| Marca/UX | PO | Designer | Analista/Android B |
| Critérios de teste | QA | QA + autores | Analista/lead |
| Merge | Lead/delegado | Revisor independente | QA/autor |
| Release pessoal | PO | Release | QA/lead |
| Publicação externa | PO | Release | Segurança/legal/plataforma |

## Fluxo de trabalho

Backlog → Refinamento → Ready → Em desenvolvimento → Revisão → QA → Aceite → Done. Blocked é atributo com motivo, responsável e próxima ação. Limite inicial: uma tarefa principal em desenvolvimento por pessoa; revisar antes de iniciar outra. Sprint de duas semanas, demonstração semanal curta, triagem assíncrona de bugs e retrospectiva ao final.

Definition of Ready: problema claro, requisito ligado, dependências conhecidas, critérios testáveis, exemplos sintéticos, design para estados relevantes, tamanho compatível com poucos dias. Spikes têm pergunta, limite de tempo e saída decidível; não terminam só em “pesquisei”.

Definition of Done: critérios cumpridos, build/checks verdes, testes adequados ao risco, revisão independente, acessibilidade quando há UI, logs redigidos, documentação/ADR atualizados, evidência anexada e sem bloqueadores abertos. Merge sem aceite não equivale a release.

## Git e revisão

Main protegida; branches curtas `feat/NO-xxx-resumo`, `fix/NO-xxx-resumo`; PR ligada à história; squash opcional preservando origem upstream no histórico base. Não fazer force push em main. Exigir ao menos um revisor independente; sessão, migração e release exigem revisão de lead/segurança e evidência QA. Para hotfix, reduzir escopo, não remover validações essenciais.

PRs devem explicar comportamento antes/depois e como testar; separar refactor e alteração funcional quando viável. Evitar PR gigante de rebranding + novo banco + rede. CODEOWNERS só após nomes reais; não usar identificadores fictícios como se fossem usuários GitHub.

## Trabalho de agentes de IA, se adotado pelo time

Mesmos papéis e critérios humanos. Cada tarefa informa arquivos/fronteira, objetivo, dependências e testes; um dono por arquivo em mutação simultânea. Agente analista não implementa requisito não aceito; agente revisor não aprova seu próprio patch; QA diferencia “planejado” de “executado”. Não enviar credenciais, dumps de amigos ou tokens aos prompts. Integrador resolve conflitos e roda testes do conjunto. Modelos/esforços dependem do ambiente e não estão fixados aqui. Nenhum time de agentes foi executado para fingir validação deste pacote.

## Handoff mínimo

ID, resultado esperado, diff/artefato, decisões, testes executados com ambiente, limitações, riscos, próxima pessoa responsável. Templates estão em `templates/`.
