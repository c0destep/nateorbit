# Fontes e limites da evidência

Consulta: 27/10/2026. Auditoria estática baseada em arquivos lidos nesta conversa, não execução, teste de invasão, teste de carga ou certificação jurídica. Metas, prazos, arquitetura e UX são propostas próprias, não declarações do upstream.

## Código fixado

- [README.md](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/README.md)
- [LICENSE](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/LICENSE)
- [app/build.gradle.kts](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/build.gradle.kts)
- [.github/workflows/nightly.yml](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/.github/workflows/nightly.yml)
- [app/src/main/java/cc/sovellus/vrcaa/manager/CacheManager.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/manager/CacheManager.kt)
- [app/src/main/java/cc/sovellus/vrcaa/ui/screen/friends/FriendsScreenModel.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/ui/screen/friends/FriendsScreenModel.kt)
- [app/src/main/java/cc/sovellus/vrcaa/activity/MainActivity.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/activity/MainActivity.kt)
- [app/src/main/java/cc/sovellus/vrcaa/ui/screen/world/WorldScreenModel.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/ui/screen/world/WorldScreenModel.kt)
- [app/src/main/java/cc/sovellus/vrcaa/manager/RecommendationManager.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/manager/RecommendationManager.kt)
- [app/src/main/java/cc/sovellus/vrcaa/ui/screen/friends/FriendsScreen.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/ui/screen/friends/FriendsScreen.kt)
- [app/src/main/java/cc/sovellus/vrcaa/manager/FavoriteManager.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/manager/FavoriteManager.kt)
- [app/src/main/java/cc/sovellus/vrcaa/api/vrchat/http/HttpClient.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/api/vrchat/http/HttpClient.kt)
- [app/src/main/java/cc/sovellus/vrcaa/extension/PreferencesExtension.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/extension/PreferencesExtension.kt)
- [app/src/main/java/cc/sovellus/vrcaa/api/vrchat/pipeline/PipelineSocket.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/api/vrchat/pipeline/PipelineSocket.kt)
- [app/src/main/java/cc/sovellus/vrcaa/service/PipelineService.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/service/PipelineService.kt)
- [app/src/main/java/cc/sovellus/vrcaa/helper/DatabaseHelper.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/main/java/cc/sovellus/vrcaa/helper/DatabaseHelper.kt)
- [app/src/test/java/cc/sovellus/vrcaa/ExampleUnitTest.kt](https://github.com/Nyabsi/VRCAA/blob/eb3978247d969e2c593837175fc7598e95f51b35/app/src/test/java/cc/sovellus/vrcaa/ExampleUnitTest.kt)

## Documentação externa

- [VRChat Creator Guidelines — API Usage / Bots](https://hello.vrchat.com/creator-guidelines): API pode mudar; restrições de credenciais e requisições. Revisão atual da página indicada como 06/10/2026.
- [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0): derivação, redistribuição e marca.
- [Android: offline-first](https://developer.android.com/topic/architecture/data-layer/offline-first): fonte local e atualização.
- [Android: arquitetura](https://developer.android.com/topic/architecture): separação UI/dados.
- [Compose: performance](https://developer.android.com/develop/ui/compose/performance/bestpractices): cálculo em composição e identidade de itens.
- [Android Keystore](https://developer.android.com/privacy-and-security/keystore): proteção de chaves, não autorização de uso de API.
- [WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent): trabalho persistente adiável.
- [Foreground services](https://developer.android.com/develop/background-work/services/fgs/service-types): tipos/restrições.
- [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview): otimização posterior a medição.
- [Especificação comunitária VRChat](https://github.com/vrchatapi/specification): referência auxiliar não oficial; não substitui condições da plataforma.
- [Issue de categorias favoritas](https://github.com/Nyabsi/VRCAA/issues/125): demanda registrada, não escopo automaticamente aprovado.

## Inventário de validação

Confirmado: SHA base, stack declarada, fluxos citados, licença raiz. Não validado: desempenho no aparelho, permissibilidade de autenticação do derivado, todas as dependências/ativos, registro de marca, domínio, release em lojas, importação de backup, orçamento de bateria. Marca gerada é conceito, não ativo vetorial final. Nenhuma tarefa deste pacote foi marcada Done por antecipação.
