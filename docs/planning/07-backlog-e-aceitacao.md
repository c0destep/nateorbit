# Backlog de execução

36 itens ordenados por fundação e dependências. P0: necessário para entrega central; P1: importante dentro da fase indicada; P2/P3: pós-MVP/futuro. Tamanho S/M/L é relativo, não dias ou promessa. Papel responsável não é atribuição a pessoa. Todos começam Backlog.

RF e RNF remetem a Produto; “QA matriz” remete ao plano de testes. Dependências são gates de conclusão, não proibição de prototipar com fake. NO-003 bloqueia autenticação real, mas não o desenvolvimento com fixtures.

## NO-001 — Reproduzir baseline do VRCAA

Fundação · P0 · G0 · tamanho M · responsável: Lead.

Dependências: nenhuma.

Aceitação: Build debug do SHA fixado reproduzido com versões e comandos registrados; APK identificado por hash; falhas do ambiente separadas de falhas do código.

Validação: Build smoke.

## NO-002 — Medir fluxos críticos

Fundação · P0 · G0 · tamanho M · responsável: QA.

Dependências: NO-001.

Aceitação: 30 execuções controladas de startup e retorno; p50/p95, requests e jank registrados; dados sintéticos e mesmo aparelho para comparação.

Validação: RNF-01,03.

## NO-003 — Resolver viabilidade de autenticação/API

Fundação · P0 · G0 · tamanho M · responsável: Analista/Lead.

Dependências: nenhuma.

Aceitação: Decisão escrita com fontes atuais e mecanismo aceitável; ausência de solução mantém integração real bloqueada e fixtures funcionando; não assumir OAuth.

Validação: RF-01.

## NO-004 — Inventariar licenças e origem

Fundação · P0 · G0 · tamanho S · responsável: Release.

Dependências: NO-001.

Aceitação: LICENSE/copyrights preservados; dependências e ativos classificados; links de suporte upstream listados para substituição.

Validação: Licenças.

## NO-005 — Validar tarefas e protótipo

UX · P0 · G0 · tamanho M · responsável: Designer/Analista.

Dependências: nenhuma.

Aceitação: Nate executa três tarefas com dados fictícios; dificuldades registradas; estados offline, vazio, erro e parcial especificados.

Validação: RF-02,05,07.

## NO-006 — Preparar identidade e CI do fork

Fundação · P0 · G1 · tamanho M · responsável: Lead.

Dependências: NO-001, NO-004.

Aceitação: ID próprio, debug separado e PR checks funcionando; nenhum segredo de release acessível em PR; build permanece utilizável.

Validação: CI smoke.

## NO-007 — Encapsular gateway legado

Dados · P0 · G1 · tamanho M · responsável: Android A.

Dependências: NO-001.

Aceitação: UI não chama cliente global diretamente; fake e gateway real usam mesmo contrato; erros tipados distinguem falha e vazio.

Validação: Contrato.

## NO-008 — Criar fixtures e servidor simulado

QA · P0 · G1 · tamanho M · responsável: QA/Android A.

Dependências: NO-007.

Aceitação: Cenários 0/100/1000/5000 amigos, paginação, 401/429/500 e eventos inválidos reproduzíveis sem credenciais reais.

Validação: Integração.

## NO-009 — Isolar sessão e remover senha persistida

Sessão · P0 · G1 · tamanho L · responsável: Android A.

Dependências: NO-003, NO-007.

Aceitação: Método validado implementado; nenhuma senha em disco; logs/backup sem segredo; falha Keystore ou sessão expirada pede recuperação explícita.

Validação: RF-01,RNF-06.

## NO-010 — Criar schema Room e repositories

Dados · P0 · G1 · tamanho L · responsável: Android A.

Dependências: NO-007, NO-008.

Aceitação: IDs pessoais escopados por conta; DAO observado por Flow; migração inicial testada; sem destructive fallback.

Validação: RNF-05.

## NO-011 — Sincronizar snapshots por recurso

Dados · P0 · G1 · tamanho L · responsável: Android A.

Dependências: NO-008, NO-010.

Aceitação: Páginas parciais não apagam snapshot válido; online é publicado antes do offline completo; recomendações não bloqueiam amigos.

Validação: RF-02,09.

## NO-012 — Reconciliar eventos e snapshot

Dados · P0 · G2 · tamanho L · responsável: Android A.

Dependências: NO-008, NO-010, NO-011.

Aceitação: Evento durante carga não se perde no commit do snapshot; duplicatas não duplicam feed; ordem incerta marca necessidade de reconciliação.

Validação: RNF-04.

## NO-013 — Controlar requests e retentativas

Dados · P0 · G2 · tamanho M · responsável: Android A.

Dependências: NO-007, NO-008.

Aceitação: Chamadas iguais compartilham operação; concorrência limitada; 429 pausa fila; tentativa de escrita ambígua não repete automaticamente.

Validação: Rate-limit.

## NO-014 — Cancelar no logout e no lifecycle

Sessão · P0 · G2 · tamanho M · responsável: Android A.

Dependências: NO-009, NO-012.

Aceitação: Logout invalida callbacks; start repetido não cria segunda conexão; reconexão pendente é cancelada; dados de conta não se misturam.

Validação: Lifecycle.

## NO-015 — Finalizar identidade e ícones

Marca · P1 · G2 · tamanho M · responsável: Designer.

Dependências: NO-005.

Aceitação: Conceito revisado por Nate; vetor único, adaptive icon e monocromia entregues; legibilidade/máscaras e licenças testadas.

Validação: Brand QA.

## NO-016 — Criar componentes e estados de UI

UI · P0 · G1 · tamanho M · responsável: Android B.

Dependências: NO-005.

Aceitação: Lista/cartão/chips/banner suportam tema claro/escuro, font scale e TalkBack; estados parciais não bloqueiam conteúdo existente.

Validação: RF-10.

## NO-017 — Entregar lista local-first

Amigos · P0 · G2 · tamanho L · responsável: Android B.

Dependências: NO-010, NO-011, NO-016.

Aceitação: Lista cacheada utilizável sem rede; IDs estáveis e posição preservada; zero spinner global para atraso de recomendação.

Validação: RF-02,RNF-01.

## NO-018 — Adicionar busca e filtros

Amigos · P0 · G2 · tamanho M · responsável: Android B.

Dependências: NO-017.

Aceitação: Nome/status/plataforma combináveis; clear funciona; busca local mede meta RNF-02; retorno do detalhe preserva filtros.

Validação: RF-03.

## NO-019 — Categorias, pins e notas locais

Amigos · P0 · G2 · tamanho M · responsável: Android B.

Dependências: NO-010, NO-017.

Aceitação: CRUD offline persiste; categoria não dispara chamada remota; mudança aparece sem depender de evento de presença.

Validação: RF-04.

## NO-020 — Detalhe de amigo e localização

Amigos · P0 · G2 · tamanho M · responsável: Android B.

Dependências: NO-017, NO-018.

Aceitação: Localização privada/ausente distinguida; estado antigo não parece ao vivo; navegação recebe IDs e preserva origem.

Validação: RF-06,09.

## NO-021 — Detalhe progressivo de mundo

Mundos · P0 · G2 · tamanho L · responsável: Android B.

Dependências: NO-010, NO-013, NO-016.

Aceitação: Cabeçalho e guardar disponíveis antes das instâncias; falha de proprietário não bloqueia mundo; chamadas iguais deduplicadas.

Validação: RF-05.

## NO-022 — Agrupar amigos por instância

Mundos · P0 · G2 · tamanho M · responsável: Android A/B.

Dependências: NO-012, NO-020, NO-021.

Aceitação: ID completo evita misturar instâncias; prioriza instâncias com amigos; não afirma acesso quando não confirmado.

Validação: RF-06.

## NO-023 — Coleções de mundos

Mundos · P0 · G2 · tamanho M · responsável: Android B.

Dependências: NO-010, NO-021.

Aceitação: Criar/renomear/excluir e ordenar offline; remoção com desfazer; claramente distintas dos favoritos VRChat.

Validação: RF-07.

## NO-024 — Busca remota de mundos

Mundos · P1 · G3 · tamanho M · responsável: Android B.

Dependências: NO-013, NO-021.

Aceitação: Debounce e cancelamento de consulta antiga; resultado tardio não sobrescreve consulta nova; cache/erro/vazio explícitos.

Validação: RF-05.

## NO-025 — Feed paginado e retenção

Atividade · P0 · G3 · tamanho L · responsável: Android A/B.

Dependências: NO-010, NO-012, NO-016.

Aceitação: Paginar 10 mil eventos sintéticos sem carregar tudo; filtros; dedupe; limpeza 30 dias; lacunas de observação sinalizadas.

Validação: RF-08.

## NO-026 — Preferências e dados pessoais

Configurações · P0 · G3 · tamanho M · responsável: Android B.

Dependências: NO-014, NO-016.

Aceitação: Tema/idioma/densidade persistem; limpeza local e logout explicam efeito; texto de privacidade e licenças acessível.

Validação: RF-10.

## NO-027 — Diagnósticos locais redigidos

Diagnóstico · P0 · G3 · tamanho M · responsável: Android A.

Dependências: NO-006, NO-013.

Aceitação: Exportação voluntária contém commit e latências; nenhum token, cookie, URL auth ou payload de amigos.

Validação: RF-11,RNF-06.

## NO-028 — Validar acessibilidade e lifecycle

QA · P0 · G3 · tamanho L · responsável: QA.

Dependências: NO-017, NO-020, NO-022, NO-025, NO-026.

Aceitação: Matriz crítica executada com ambiente/evidências; fonte 200%, TalkBack, modo avião, rede trocada e process death aprovados.

Validação: QA matriz.

## NO-029 — Comparar performance e otimizar

Performance · P0 · G3 · tamanho L · responsável: Lead/QA.

Dependências: NO-002, NO-017, NO-021, NO-025.

Aceitação: Mesmo protocolo baseline/derivado; metas avaliadas; hot paths corrigidos; Baseline Profile se ganho confirmado.

Validação: RNF-01,02,03.

## NO-030 — Preparar beta pessoal e release

Release · P0 · G4 · tamanho M · responsável: Release/QA.

Dependências: NO-004, NO-009, NO-014, NO-015, NO-027, NO-028, NO-029.

Aceitação: APK assinado, checksum e notas; zero S0/S1; método API resolvido; recuperação testada; PO aceita uso pessoal.

Validação: Gate G4.

## NO-031 — Alertas seletivos

Alertas · P2 · Pós-MVP · tamanho M · responsável: Android A/B.

Dependências: NO-025, NO-030.

Aceitação: Opt-in, permissão, silêncio e cooldown testados; eventos de snapshot não geram tempestade; sem promessa de 24/7.

Validação: RF-12.

## NO-032 — Spike de acompanhamento contínuo

Background · P2 · Pós-MVP · tamanho L · responsável: Lead/QA.

Dependências: NO-014, NO-030.

Aceitação: Tipo de serviço e política validados; notificação/stop visíveis; consumo físico medido; resultado decide implementar ou rejeitar.

Validação: Background.

## NO-033 — Backup e importação controlada

Portabilidade · P2 · Pós-MVP · tamanho L · responsável: Android A/QA.

Dependências: NO-010, NO-030.

Aceitação: Formato upstream investigado; importação pré-visualizada/transacional; arquivos maliciosos rejeitados; nunca importar sessão.

Validação: Migração.

## NO-034 — Editar favoritos remotos explicitamente

Favoritos · P2 · Pós-MVP · tamanho M · responsável: Android A/B.

Dependências: NO-013, NO-019, NO-023, NO-030.

Aceitação: UI separa remoto/local; confirma ações; reconcilia erro ambíguo; operação não apaga coleções locais.

Validação: RF-04,07.

## NO-035 — Reavaliar recomendações

Descoberta · P3 · Futuro · tamanho M · responsável: Analista/Android A.

Dependências: NO-023, NO-030.

Aceitação: Validar utilidade com Nate; processamento fora do startup; orçamento de requisições e dados locais explícitos.

Validação: Discovery.

## NO-036 — Avaliar distribuição pública

Publicação · P3 · Futuro · tamanho L · responsável: PO/Release.

Dependências: NO-030.

Aceitação: Marca, licenças de ativos, privacidade, API e requisitos do canal revisados; decisão separada de publicação registrada.

Validação: Release externo.
