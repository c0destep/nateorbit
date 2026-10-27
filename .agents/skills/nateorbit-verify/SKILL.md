---
name: nateorbit-verify
description: Validar alterações NateOrbit com checks proporcionais e evidências reais. Usar antes de handoff ou PR e ao investigar falhas de build, teste ou lint.
---

# Verificar a alteração

Ler AGENTS.md e docs/development/VALIDATION.md. Inspecionar diff e critérios da tarefa.

- Docs/skills/scripts: rodar make verify. Scripts novos/alterados precisam de execução
  representativa, incluindo falha de pré-requisito quando relevante.
- Código/dependências/build Android: rodar make check. Escolher regressões adicionais
  a partir de docs/planning/09-qualidade-e-testes.md, conforme o comportamento alterado.
- Instrumentação: make connected-test somente com dispositivo pronto. Registrar serial
  anonimizado/modelo, API e build. Não afirmar teste de UI por ter só compilado.
- Separar ausência de JDK/SDK/rede de erro do projeto. Não alterar pins, desligar lint,
  remover testes ou usar continue-on-error para produzir um resultado verde.
- Desempenho: comparar mesmos dados, build e aparelho; marcar hipótese quando não há
  medição. O teste ExampleUnitTest legado não valida os fluxos do produto.
- Usar docs/templates/revisao.md e handoff.md. Incluir comando, saída resumida,
  relatórios (app/build/reports e app/build/test-results), falhas e não executados.

Atualizar o registro de validação pertinente sem sobrescrever evidências históricas.
Done depende do aceite da tarefa, não apenas da existência de arquivos.
