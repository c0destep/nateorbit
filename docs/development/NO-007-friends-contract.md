# NO-007 — contrato de leitura de amigos, primeira fatia

Status: In Progress. Esta fatia cria a fronteira testável; não conclui a migração da UI.

## Problema e resultado

`HttpClient.friends.fetchFriends` mistura paginação recursiva e tratamento de erro:
uma falha devolve uma lista vazia. Não é possível adaptar esse retorno e recuperar
a informação perdida. O novo `FriendsRepository.fetchPage` distingue
`Success(FriendsPage)` de `Failure(FriendsError)` antes dessa perda.

O contrato é injetável por construtor, com implementações
`FakeFriendsRepository` e `LegacyFriendsRepository`. O adapter legado recebe uma
função suspensa que fornece `BaseClient.Result` para uma única página; não chama
o método recursivo antigo. Há projeção mínima imutável de ID, nome e status,
sem cookies, localização privada ou DTO mutável no resultado.

- Limite de 1–100, offset não negativo e soma protegida contra overflow.
- Página cheia fornece próximo offset; página curta termina a leitura.
  Página isolada não autoriza apagar um snapshot existente.
- Sucesso vazio é explícito. Offline, 401, 403, 429, 500 e respostas inesperadas
  são falhas tipadas. Não há retry automático nem logs de corpo ou exceções.
- JSON inválido, IDs vazios/duplicados, campos obrigatórios ausentes/tipos
  incorretos e páginas acima do limite falham integralmente.
- Status ausente/desconhecido não é inferido como offline.
- Cancelamento do transporte propaga ao chamador.
- Fake usa somente dados sintéticos e permite falha tipada e páginas online/offline.

## Regressões

`FriendsRepositoryTest` cobre doze cenários: vazio válido, matriz de falhas,
uma única chamada com query preservada, payload inválido, excesso de itens,
status desconhecido, paridade de paginação fake/legado, isolamento do input
do fake e falha tipada, cancelamento, query inválida, rejeição de sintaxe JSON
não padrão e isolamento de leituras após mutação de uma página retornada.

A revisão independente encontrou parsing leniente com `JsonParser.parseString`.
Uma regressão reproduziu sucesso indevido com aspas simples. O adapter passou
a usar Gson em `Strictness.STRICT`, com consumo integral do documento. Comentários,
aspas simples, nomes sem aspas e conteúdo extra após o documento são inválidos.

Os testes não usam rede, conta VRChat, sleeps ou dependências novas.

## Limites e próxima fatia

O adapter ainda não está ligado a `ApiManager`/`HttpClient` nem à tela.
O transporte legado usa flags globais para pular autorização e pode iniciar
recuperação de sessão e registrar payloads no modo de diagnóstico. Não adicionar
um novo consumidor autenticado antes de NO-003/NO-009 resolverem essas regras.
A leitura existente e a tela permanecem com o comportamento anterior.

Para concluir NO-007 no fluxo de amigos: injetar repository no ScreenModel,
remover sua dependência direta de managers globais e definir composição fake
explícita. Separar conteúdo, refresh e erro, preservando conteúdo no refresh;
testar recomendações lentas e erro parcial sem spinner global. A conexão real
exige transporte com autorização por requisição e política de logs revisada.
Não marcar NO-007 Done pela existência do contrato, nem declarar modo demo pronto.

### Refinamento após análise independente

A tela atual depende de `platform`, `location`, imagens e `FavoriteManager` para
filtrar/renderizar amigos. Não converter `FriendSummary` em `Friend` com valores
padrão: `platform` vazio faria os dados sintéticos parecerem offline. Definir uma
projeção de apresentação explícita antes de migrar a tela. O caminho normal de
`MainActivity` ainda exige login/cache; um modelo testado com fake não estabelece
uma entrada offline navegável.

A próxima fatia deve testar o estado do modelo por operações suspensas
controladas com `CompletableDeferred`: conteúdo preservado durante refresh,
erro inicial distinto de vazio, página posterior com falha, carga online
independente de recomendações e descarte de respostas antigas após cancelamento
ou carga mais recente. Só então ligar o estado à tela e à composição debug.

## Handoff

Artefatos: `data/friends/FriendsRepository.kt`, `LegacyFriendsRepository.kt` e
`FriendsRepositoryTest.kt` em seus source sets do módulo app. Nenhuma versão,
manifesto, credencial ou fluxo de login foi alterado. Validar com
`source /workspace/toolchains/activate.sh && make check` na raiz.
Consultar VALIDATION.md para o resultado efetivamente executado.
