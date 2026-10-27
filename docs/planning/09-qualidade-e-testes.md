# Estratégia de qualidade

## Camadas

Unitários: reducers de presença, filtros/categorias, política de frescor, backoff com relógio virtual, deduplicação e erros tipados. Integração: DAO/Room com migrações reais, MockWebServer, gateway e reconciliação de snapshot/eventos. UI: Compose nos fluxos críticos, acessibilidade e persistência de navegação. Instrumentação/performance: Macrobenchmark, profiling de jank e memória, medição de bateria em aparelho físico.

Não usar conta real em CI. Fixtures com IDs e pessoas sintéticas, metadados mínimos e nenhum cookie. Testes live só no spike autorizado, controlados e sem carga artificial contra VRChat. Teste de stress usa servidor simulado.

## Matriz mínima

| Cenário | Resultado esperado | Camada |
|---|---|---|
| 0/100/1.000/5.000 amigos sintéticos | Estado vazio correto, paginação e busca estáveis; 5.000 é stress, não promessa de limite VRChat | Unidade/UI/perf |
| Página 3 retorna 500 após duas válidas | Snapshot anterior mantido; progresso parcial identificado; ausentes não removidos | Integração |
| 429 com e sem Retry-After | Fila pausa; backoff limitado; sem tempestade de requests | Integração |
| Mundo responde antes das instâncias | Cabeçalho e coleção utilizáveis imediatamente | UI |
| Evento durante snapshot | Evento reaplicado; ausência de reversão silenciosa para estado velho | Integração |
| Eventos duplicados/desconhecidos/malformados | Dedupe limitado, evento desconhecido ignorado com diagnóstico seguro, sem crash | Unidade/integração |
| Logout durante rede e reconexão pendente | Jobs cancelados; callback antigo não repovoa banco | Integração |
| Dois startService consecutivos | Uma conexão e um job por recurso | Instrumentação |
| Rede Wi-Fi → móvel → offline | Cache permanece; conexão recupera sem duplicar feed | Dispositivo |
| Morte de processo / reinício | Estado local íntegro; lacuna de observação explícita | Dispositivo |
| Timeout após ação remota | Estado desconhecido recuperável; não repetir convite automaticamente | Integração/UI |
| Backup/exportação | Sem segredo; importação rejeita formato inválido, tamanho excessivo e path traversal | Integração |
| Migração interrompida | Transação íntegra e recuperação documentada, sem destructive fallback | Integração |
| Token inválido/Keystore indisponível | Sessão expirada, recuperação explícita, sem senha salva | Instrumentação |
| Fonte 200%, TalkBack e contraste | Ações acessíveis, status não depende apenas de cor | QA/UI |
| Notificação negada/silêncio/cooldown | App funciona; não insistir em permissão nem duplicar alertas | Dispositivo, pós-MVP |

## Dispositivos e versões

Manter minSdk 27 no primeiro ciclo para evitar mudança gratuita; emuladores API 27, 33, 34 e 36, ajustando versões ao SDK real de G0. Aparelhos: Samsung S23 com versão real registrada por QA; um Android intermediário com 4–6 GB RAM; pelo menos um segundo fabricante se houver beta externo. Não presumir versão do Android apenas pelo nome One UI.

Testar portrait/landscape, 60/120 Hz quando disponível, bateria restrita e modo econômico. Não exigir validação completa de Quest/Pico no MVP de telefone.

## Medições

Baseline upstream e derivado no mesmo aparelho/build release, mesma fixture/cache/rede simulada, 30 repetições de startup com warmup separado; reportar p50/p95 e dispersão. Medir tempo até conteúdo utilizável, não só primeira Activity. Feed com 10 mil eventos sintéticos, paginação sem carregar tudo. Bateria: sessões pareadas de 60 minutos, tela ligada/desligada e taxa de eventos fixada; resultado inicial define orçamento, não inventar ganho.

## Severidade e gates

S0: exposição de credenciais, perda de dados ou ação remota indevida — interrompe release. S1: login/fluxo central inutilizável, crash reproduzível frequente — bloqueia. S2: função degradada com alternativa — PO/QA decidem explicitamente. S3: cosmético. Prioridade é separada da severidade.

Gates: todos os cenários críticos aprovados, zero S0/S1 abertos, migração com evidência, métricas contra baseline, acessibilidade crítica verificada. Cobertura numérica não substitui cenários; meta inicial 80% de branches nos reducers/políticas novos, sem exigir percentual global artificial no legado. Não prometer “99,9% crash-free” sem população e observabilidade suficientes.

Relatório: commit/APK, hash, dispositivo/OS, dados de teste, passos, esperado/obtido, evidências redigidas, testes não executados e motivo. Este pacote fornece plano, não resultados executados do app.
