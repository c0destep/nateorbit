# NateOrbit — instruções de trabalho

## Contexto e leitura inicial

App Android pessoal de amigos e mundos do VRChat, derivado de VRCAA Apache-2.0.
Responder a Nate em português; identificadores de código em inglês. Interface do
ambiente Linux/Android Studio em inglês. Trabalhar com Kotlin, Compose e Material 3.

Antes de implementar, ler README.md, docs/development/START-HERE.md e
planning/sprint-01.md. Consultar somente os documentos de planejamento pertinentes.
O backlog corrente é planning/backlog.json; a arquitetura de destino está em
docs/planning/03-arquitetura-e-dados.md. Documentação de destino não prova código pronto.

## Mapa e decisões

- Código legado: app/src/main/java/cc/sovellus/vrcaa/{api,manager,helper,service,ui}.
- app é o único módulo Gradle atual. Preservar Voyager/ScreenModel e Glide enquanto
  não houver necessidade demonstrada de mudança. Room/DataStore são decisões de
  destino, ainda não implementadas; não afirmar que já existem.
- Manter namespace cc.sovellus.vrcaa e applicationId dev.nateorbit.app nesta fase;
  standardDebug instala dev.nateorbit.app.dev. Não renomear pacotes em massa.
- Gradle wrapper, AGP, Kotlin e SDK vêm do build; não atualizar versões para tentar
  corrigir erro de rede. scripts/android-env.json descreve os pré-requisitos Linux.
- Preservar LICENSE, copyrights e UPSTREAM.md. Incluir aviso de alteração nos
  arquivos upstream modificados. Nunca enviar trabalho para Nyabsi/VRCAA.

## Implementação

- Entregar uma fatia revisável por tarefa. Ajustar planejamento/ADR quando a decisão
  mudar. Não misturar redesign, atualização de bibliotecas e migração de banco.
- A primeira fatia usa fixtures sintéticas e repository fake. Não confundir isso
  com um modo demo já implementado: o fluxo de login legado continua presente.
- UI nova observa estado de ScreenModel/ViewModel via repository; não acessar HTTP
  ou managers globais diretamente em composables novos.
- Mostrar cache existente durante refresh. Amigos não esperam recomendações,
  favoritos ou detalhes de mundos. Erro parcial não significa lista vazia.
- Manter um escritor por entidade; cancelar jobs de sessão no logout e impedir
  callbacks antigos de repovoar estado. Usar chaves estáveis por ID nas listas.
- Não persistir novas senhas. Não registrar cookies, tokens, localizações privadas
  ou respostas de usuários reais em logs, fixtures, CI ou prompts.
- Autenticação real depende de NO-003/NO-009. Não inventar OAuth nem extrair cookies
  de navegador. Desenvolver offline enquanto a decisão permanecer pendente.
- Não usar destructive migrations de dados pessoais. Não alterar favoritos remotos
  para implementar categorias locais. Não introduzir retries cegos em ações remotas.

## Skills disponíveis

As skills do projeto estão em .agents/skills e acompanham o clone:

| Skill | Uso |
|---|---|
| $nateorbit-plan-task | Refinar uma tarefa, dependências, aceitação e handoff |
| $nateorbit-android-feature | Implementar uma fatia Kotlin/Compose |
| $nateorbit-sync-review | Revisar cache, rede, eventos e sessão |
| $nateorbit-verify | Escolher checks e registrar evidências |
| $nateorbit-linux | Diagnosticar JDK/SDK e preparar Linux |

Usar apenas as skills pertinentes. Papéis analista, implementador, revisor e QA
são responsabilidades, não uma exigência de criar subagentes. Não fixar modelos
ou esforços na documentação; respeitar a configuração real do Codex. Caso o usuário
peça delegação, relatar somente modelo/esforço realmente expostos pela ferramenta.

## Comandos e evidências

Executar na raiz; ver Makefile e docs/development/LINUX.md:

- make verify: integridade da base e testes dos scripts, sem Android/rede.
- make doctor: JDK/SDK/wrapper; informa o que falta sem instalar nada.
- make check: verify + doctor + assembleStandardDebug + testStandardDebugUnitTest
  + lintStandardDebug, com wrapper e --no-daemon.
- make connected-test: instrumentação com dispositivo/emulador já conectado;
  não tratar como verificação automática em ambiente sem dispositivo.

Para docs/skills, executar make verify; para código/build Android, make check e
regressões do comportamento afetado. UI exige evidência visual/acessibilidade;
sessão, paginação e banco exigem cenários de falha reais ou simulados. Não declarar
build, testes, benchmark ou QA aprovados sem execução. Informar comando, resultado,
bloqueio e próximo passo. O teste aritmético herdado não valida o domínio.

## Colaboração e revisão

Usar branches feat/NO-xxx-resumo, fix/NO-xxx-resumo ou chore/resumo. Não sobrescrever
mudanças alheias nem fazer force push. Revisão independente antes do merge; não
publicar release, assinar APK de produção ou mudar proteção de branch sem tarefa.
Handoff: problema, comportamento entregue, arquivos relevantes, checks, limitações
e próxima ação (docs/templates/handoff.md). Atualizar status com evidência; não
marcar todo G0 concluído por ter criado arquivos.

## Code Review Rules

Priorizar regressões verificáveis com arquivo/linha, impacto e reprodução:

- Sinalizar carga global bloqueando conteúdo já disponível ou erro de paginação
  removendo dados válidos. Sugerir estados independentes e snapshots completos.
- Sinalizar concorrência entre snapshot/eventos ou sessão antiga e nova capaz de
  perder/ressuscitar dados. Verificar cancelamento, deduplicação e escritor único.
- Sinalizar exposição de segredo, migração destrutiva e ação remota repetida após
  timeout. Formatação é responsabilidade dos checks, não um bloqueador inventado.
