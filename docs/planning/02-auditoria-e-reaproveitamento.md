# Auditoria e reaproveitamento do VRCAA

Referência: commit fixado no plano executivo. Evidência estática, sem profiler ou execução do APK. Caminhos abaixo relativos a `app/src/main/java/cc/sovellus/vrcaa/`, salvo indicação. Links completos em Fontes.

| Componente | Observação verificada | Ação e teste |
|---|---|---|
| manager/CacheManager.kt | buildCache reúne amigos, favoritos, notificações, recomendações e mundos e espera joinAll | Separar sincronizadores; atrasar recomendação artificialmente e provar que amigos aparecem |
| ui/screen/friends/FriendsScreenModel.kt | Loading depende da conclusão do cache global | Usar UiState por recurso, preservar dados anteriores durante refresh |
| activity/MainActivity.kt | Retorno após 15 minutos chama buildCache | Substituir por freshness por recurso e reconciliação limitada |
| ui/screen/world/WorldScreenModel.kt | Resultado aguarda instâncias e donos/grupos | Renderizar mundo primeiro e atualizar detalhes progressivamente |
| manager/RecommendationManager.kt | Consultas por tags em sequência no fluxo da carga geral | Tirar do startup; manter desativado até pós-MVP |
| ui/screen/friends/FriendsScreen.kt | Filtros/ordenação nos composables e items sem key explícita nos trechos examinados | Preparar listas fora da composição; key por ID; medir jank |
| manager/FavoriteManager.kt | Consultas de favorito percorrem grupos e itens | Índice por ID; observar favoritos junto a amigos; testar categoria alterada sem evento de amigo |
| api/vrchat/http/HttpClient.kt | Erro em fetchFriends devolve lista vazia, perdendo acumulado; tratamento 429 por aviso | Resultado tipado com dados parciais; pausa/retry limitado para leitura |
| extension/PreferencesExtension.kt | Senha e tokens persistidos como strings em SharedPreferences | Remover senha persistida; resolver política e novo armazenamento de sessão |
| api/vrchat/pipeline/PipelineSocket.kt | Reconexão por intervalo fixo, escopo próprio | Job único, cancelamento e reconciliação após lacuna |
| service/PipelineService.kt | onStartCommand inicia conexão e buildCache | Tornar início idempotente; testar chamadas repetidas e destruição |
| app/src/test/.../ExampleUnitTest.kt | Teste aritmético de exemplo | Substituir cobertura simbólica por testes de estado, paginação, sessão e migração |

## Preservar primeiro

Modelos/DTOs como referência de compatibilidade, interfaces de endpoints, mapeamentos de status/localização, traduções com atribuições, tratamento de eventos e infraestrutura Gradle. Revisar payloads e autenticação; reaproveitar não significa confiar sem teste.

## Adaptar por fronteiras

Encapsular cliente legado em VrchatGateway. Novas telas não chamam managers globais. Enquanto durar a migração, apenas um escritor é dono de cada entidade: o adaptador recebe eventos legados e persiste pelo novo repository. Evitar UI observando simultaneamente lista antiga e banco novo.

## Retirar da primeira navegação

Rich Presence/Discord, upload de mídia, busca externa de avatares, recomendações e interfaces específicas de Quest/Pico. Não apagar todas essas pastas no primeiro commit; desativar entry points, testar build e remover dependências quando não houver consumidores.

## Dívida a confirmar

Cobertura total de criptografia/backup, riscos de concorrência de flags globais de autorização, transições de ciclo de vida, migrações antigas e formatos exportados. Cada suspeita precisa de reprodução antes de ser anunciada como defeito comprovado. Não atribuir lentidão ao Kotlin, Compose ou aparelho sem medição.
