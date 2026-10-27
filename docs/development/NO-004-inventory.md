# NO-004 — inventário inicial de origem e licenças

Status: In Progress. Base inspecionada: `5761edde7f135efcecfdeba876396de0ea141b23`.
Este levantamento não autoriza distribuição e não certifica licenças de terceiros.

## Código e dependências

LICENSE Apache-2.0 e copyrights por arquivo foram preservados. A origem e o SHA
upstream estão em UPSTREAM.md; não há alegação de endosso de Nyabsi ou VRChat.

- [Dependências diretas](evidence/no-004/direct-dependencies.csv): coordenadas,
  escopo, licença declarada no POM disponível e fonte para revisão. Entradas
  controladas pelo BOM e POMs sem licença explícita permanecem não determinadas.
  A licença declarada no POM é evidência de metadados, não análise do binário.
- [Grafo runtime resolvido](evidence/no-004/runtime-dependencies.txt): saída de
  `./gradlew :app:dependencies --configuration standardDebugRuntimeClasspath
  --no-daemon --console=plain`, concluída com sucesso. Inclui transitivas e
  versões escolhidas; ainda falta revisar suas licenças e avisos individualmente.
- Ferramentas de build: Gradle 9.3.1, AGP 9.0.1, plugins Kotlin/Compose 2.3.10 e
  AboutLibraries 13.2.1. Separar ferramentas das bibliotecas embarcadas na revisão.

O build emite aviso de integração AboutLibraries com AGP. A presença da tela
de licenças e do plugin não prova que todos os avisos foram empacotados.
Conferir o conteúdo distribuído antes de concluir NO-004.

## Ativos e traduções

[Inventário de 95 arquivos](evidence/no-004/assets.csv), com caminho, SHA-256 e
classificação: imagens, vetores drawable/mipmap, arte de loja e conceito de marca.
Nenhum ativo foi substituído nesta tarefa.

| Grupo | Origem observada | Situação / próxima ação |
| --- | --- | --- |
| Launcher, notificações e logos | Recursos herdados em app/src | Conferir autor/licença por ativo e substituir identidade herdada em NO-015 |
| Bandeiras e placeholder | Recursos drawable herdados | Origem por arquivo não documentada; localizar fonte e condições de redistribuição |
| Arte da loja | fastlane/metadata/android/en-US/images | Herdada; revisar direitos e identidade antes de distribuir |
| Traduções | 25 arquivos strings.xml em app/src/main/res | Herdadas/Crowdin; revisar atribuição, contribuições e referências a VRCAA |
| Conceito NateOrbit | brand/prompt.txt, tokens.json e PNG | Geração por ferramenta documentada no prompt; conceito, sem certificação de marca ou vetor final |
| Fontes | Nenhum arquivo ttf/otf no levantamento de app/src | Não presumir ausência de fontes nas dependências; conferir artefatos transitivos |

## Links herdados a revisar

| Destino | Uso no código | Ação antes de distribuição |
| --- | --- | --- |
| https://discord.gg/aJs8qJXuT3 | DISCORD_URL; CrashScreen.kt | Definir canal próprio ou remover ação de suporte |
| https://crowdin.com/project/vrcaa | CROWDIN_URL; SettingsScreen.kt | Definir fluxo de tradução do fork |
| https://ko-fi.com/Nyabsi | KOFI_URL; SettingsScreen.kt | Revisar/remover CTA de doação herdado, preservando atribuição |
| Nyabsi/VRCAA, F-Droid e Play do upstream | docs/upstream/README.md | Manter como arquivo histórico claramente identificado; não anunciar como distribuição do fork |

## Aceite restante e handoff

Feito: origem identificada, LICENSE/copyrights preservados, dependências diretas
levantadas, transitivas resolvidas, ativos classificados com hashes e links de
suporte listados. Nenhuma mudança de código, dependências ou lockfiles.

Pendente: conferir licenças/NOTICE das transitivas e textos completos, esclarecer
origem de bandeiras/logos/traduções, revisar licenças efetivamente empacotadas e
definir substituições dos CTAs. Responsabilidade: Release/Lead; sem pessoa atribuída.
Não marcar Done até resolver ou registrar uma decisão revisada para cada pendência.

Checks desta fatia documental: `make verify` e `git diff --check`. Próxima tarefa
executável de código: refinar NO-007 para contrato de amigos com fake e erros
tipados, preservando o gateway legado e sem autenticação real.
