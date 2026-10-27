# Arquitetura e dados

## Stack decidida

Kotlin + Compose + Material 3; coroutines/Flow; OkHttp; Room para dados estruturados; DataStore para preferências sem segredos; Android Keystore para proteção de chaves se persistência de sessão vier a ser permitida. Preservar inicialmente Glide e Voyager do upstream. Injeção por construtores e um AppContainer no início; introduzir framework apenas se houver necessidade demonstrada. Congelar versões resolvidas em G0, sem atualizar tudo junto com refatoração.

## Fluxo

Compose observa StateFlow de ViewModel/ScreenModel. Este depende de repository. Repository lê Room e coordena gateway HTTP/WebSocket através do SyncCoordinator. Dados da API passam por DTO → validação → modelo de domínio → transação local. UI não possui cliente HTTP nem recebe cookies.

Estado padrão: `data`, `isInitialLoading`, `isRefreshing`, `lastSuccessAt`, `error`, `isStale`, `syncCoverage`. Erro de atualização mantém data. “Nenhum resultado” só é estado final com resposta válida ou consulta local vazia conhecida.

## Organização gradual

Primeiro usar pacotes dentro do app para reduzir impacto no build. Após G1, extrair módulos quando fronteiras estiverem testadas:

- app: composição, navegação e entry points.
- core/model: entidades e erros de domínio, sem Android quando possível.
- core/network: gateway e transporte, DTOs, orçamento de requisições.
- core/database: Room, DAO, migrações e fixtures.
- core/session: ciclo de sessão e SessionStore.
- core/sync: sincronização, reconciliação e frescor.
- core/designsystem: componentes e tokens.
- feature/friends, worlds, collections, activity, settings: UI e modelos.

Features não dependem umas das outras; navegação passa IDs. Contratos em core; nenhuma dependência circular. Não criar um módulo por classe.

## Modelo lógico

| Entidade | Chave / campos essenciais | Regra |
|---|---|---|
| AccountScope | accountId | Escopo em todas as tabelas pessoais, mesmo com uma conta ativa |
| Friend | accountId,userId; nome,status,plataforma,location,observedAt | Status desconhecido diferente de offline |
| World | worldId; nome,descrição,thumb,updatedAt | Metadados públicos em cache com invalidação |
| Instance | accountId,locationId; worldId,instanceId,visibility,region,observedAt | Chave mantém identidade completa e não presume acesso |
| RemoteFavorite | accountId,favoriteId; targetId,type,groupId | Não conflitar com categoria local |
| LocalCategory | accountId,categoryId; nome,ordem | UUID local |
| FriendCategory | accountId,userId,categoryId | Associação N:N, índice por categoria |
| PersonalNote | accountId,targetType,targetId; texto,updatedAt | Só local; nunca enviada automaticamente |
| Collection / CollectionItem | accountId,collectionId[,worldId] | Coleções locais; índice de ordem |
| ActivityEvent | accountId,eventId; userId,type,observedAt,dedupeKey | IDs únicos; payload mínimo, retenção configurável |
| SyncMetadata | accountId,resourceKey; lastSuccessAt,coverage | Distingue snapshot completo de parcial |
| AlertRule | accountId,ruleId; alvo,evento,cooldown | Pós-MVP, desligado por padrão |

Não armazenar senha nessas tabelas. Tokens não ficam em Room/DataStore comum. Históricos são locais e representam eventos observados, não a verdade completa da atividade de alguém.

## Sincronização

1. Renderizar snapshot local imediatamente.
2. Garantir sessão válida por operação única compartilhada; nunca vários logins simultâneos.
3. Buscar amigos online; persistir páginas em staging e publicar progresso sem apagar snapshot válido.
4. Buscar offline/favoritos em prioridade menor. Só remover ausentes após snapshot completo bem-sucedido; página com erro não confirma exclusão.
5. Enriquecer mundos visíveis sob demanda, compartilhando chamadas em andamento por chave.
6. Aplicar eventos por usuário com ordem serializada. Se socket iniciou antes do snapshot, bufferizar eventos durante a carga e reaplicar na transação final. Se não houver versão/ordem confiável do servidor, marcar lacuna e reconciliar os alvos; não inventar garantia de consistência perfeita.
7. Reconectar com backoff exponencial e jitter, limite de 60 s proposto, reset após conexão estável. Cancelar tentativas ao logout/desligar acompanhamento.

Orçamento inicial interno: no máximo 3 leituras HTTP simultâneas, 1 reconciliação por recurso e deduplicação de requisições idênticas; valores ajustáveis por testes, não limites oficiais da API. HTTP 429: respeitar Retry-After quando fornecido, pausar fila e limitar retentativas; sem loop infinito. Escritas de convite não repetem automaticamente após timeout ambíguo.

Frescor proposto: presença via eventos quando conectado; reconciliar após lacuna/retorno, em vez de polling contínuo; mundo público TTL inicial de 24 h e refresh explícito; favoritos revalidados ao abrir e após escrita. Valores são política do app, calibrada após G0. Mudança de visibilidade invalida informação sensível mais cedo que TTL.

## Background

MVP: observação enquanto app está ativo, cache ao retornar. WorkManager só para tarefas adiáveis apropriadas, não como websocket permanente nem relógio exato. Modo contínuo futuro exige experimento de foreground service compatível com regras Android, notificação visível, opt-in e botão parar. Não declarar specialUse apenas para contornar restrições. Sem backend no MVP.
