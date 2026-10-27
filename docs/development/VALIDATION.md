# Validação desta preparação — 27/10/2026

## Executado

- Clone do upstream com histórico; HEAD de origem confirmado em eb3978247d969e2c593837175fc7598e95f51b35.
- Branch chore/nateorbit-bootstrap e remoto upstream configurados; origin de destino ausente.
- Documentos/backlog/templates incorporados, ID de desenvolvimento e nome ajustados, licença preservada.
- Workflow nightly herdado desativado; CI debug com actions fixadas em SHA e permissão contents:read.

Verificações locais aprovadas: 36 IDs únicos e dependências sem ciclos; XML do app parseado; licença e identidade conferidas; workflow sem schedule/publicação, actions fixadas em SHA; sintaxe Python/Bash/YAML e git diff --check aprovados.

## Limitações encontradas

Java disponível: OpenJDK runtime 17, sem javac. Android SDK/sdkmanager/adb ausentes. Tentativa de `./gradlew assembleStandardDebug testStandardDebugUnitTest lintStandardDebug --no-daemon`: falha no download do Gradle 9.3.1 com `java.net.SocketException: Network is unreachable`, antes de configurar o projeto.

Nenhum build Android, teste unitário Gradle, lint, teste instrumentado ou benchmark pôde ser executado. Nenhum APK foi gerado. A execução de CI precisa ocorrer no repositório destino e pode revelar problemas herdados de dependências/configuração ainda não observados.

## Ainda pendente

Validar ambiente e tasks no CI, inventariar dependências, implementar testes de domínio, definir autenticação, remover persistência de senha herdada, revisar links/ícones upstream e escolher destino GitHub. Preparação de repositório não conclui G0.


## Preparação Codex/Linux — 27/10/2026

- AGENTS.md revisado; cinco skills de repositório validadas pelo validador oficial.
- make verify aprovado: integridade da base/backlog/XML, links/pins de ambiente e
  sete testes dos scripts Linux. Testes incluem SDK incompleto, JDK ausente,
  variáveis conflitantes e provisionamento simulado com caminhos contendo espaços.
- Sintaxe Bash, metadados YAML e git diff --check conferidos.
- make doctor confirma que este executor ainda tem runtime Java 17, sem JDK 21 e
  sem Android SDK. Build/testes/lint Android não foram aprovados aqui.
- Destino definido: c0destep/nateorbit. A importação inicial via Actions preserva
  a base upstream fixada e remove o workflow de importação do resultado. Apenas
  esse job usa contents:write para o primeiro envio; o CI recorrente usa leitura.
- Resultado remoto de importação e build deve ser consultado em Actions; esta
  seção não antecipa aprovação. O app continua sem modo fake implementado.


## Importação remota e primeiro CI

Importação confirmada na main: d9902091568c9be990ff466271ba97d3031d4623,
com eb3978247d969e2c593837175fc7598e95f51b35 como segundo pai; 510 arquivos
confirmados pela árvore GitHub. Workflow temporário removido.

Execução https://github.com/c0destep/nateorbit/actions/runs/40585324935:
importação e JDK aprovados, setup Android falhou antes da compilação porque a
action fixada solicita o pacote descontinuado `tools` por padrão. Correção:
passar `packages: platform-tools` explicitamente, mantendo as versões do app.
O CI recorrente será executado novamente; este registro não declara build aprovado.


## CI Android aprovado — 27/10/2026

Commit validado: 6de23c56bba7d1dba9cc8f349f2e75205998c596.
Execução: https://github.com/c0destep/nateorbit/actions/runs/40585516342
Job: debug-checks (122475758888), conclusão success.

JDK 21 e componentes do SDK instalados. `bash scripts/check.sh --stacktrace`
aprovou os checks de integridade, sete testes dos scripts e as tasks
`:app:assembleStandardDebug`, `:app:testStandardDebugUnitTest` e
`:app:lintStandardDebug`. Relatórios enviados no artefato android-check-reports.
O workflow recorrente tem apenas contents:read e não publica release/APK.

Essa evidência valida a base herdada e a preparação; os testes de domínio novos,
instrumentação, smoke em aparelho e benchmarks ainda não foram implementados ou
executados. O teste unitário legado não demonstra os critérios funcionais futuros.
A preparação não conclui todo G0 e não resolve NO-003/NO-009.

## Baseline cloud e início do inventário — 27/10/2026

NO-001 concluído para o SHA `5761edde7f135efcecfdeba876396de0ea141b23`:
[versões, comandos, logs, limites e hash do APK](NO-001-baseline.md).
Build standardDebug, sete testes dos scripts, um teste unitário herdado e lint
aprovados neste executor; lint com 137 avisos e nenhum erro. Setup repetido com
saída zero. Isso substitui as limitações antigas do ambiente para esta instância,
sem alterar os registros históricos acima. Aparelho e benchmark continuam pendentes.

NO-004 iniciado com [inventário de dependências, ativos e links](NO-004-inventory.md).
Revisão de transitivas/proveniência e avisos distribuídos permanece aberta.
