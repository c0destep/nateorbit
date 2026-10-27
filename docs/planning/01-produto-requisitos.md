# Produto e requisitos

## Necessidade e personas

Usuário principal: Nate, que já usa VRChat e quer consultar sua rede social rapidamente pelo celular. Persona secundária: usuário com muitos amigos que precisa filtrar presença e organizar mundos. Não assumir interesse em analytics de terceiros ou administração de grupos.

Jobs: “quero saber quem está disponível”; “quero encontrar uma instância onde já tenho amigos”; “quero guardar um mundo para depois”; “quero entender o que mudou desde minha última consulta”.

## Requisitos funcionais

| ID | Requisito | Evidência de aceitação |
|---|---|---|
| RF-01 | Sessão com estados explícitos | Inicial, válida, expirada, aguardando MFA e erro recuperável distinguíveis; método de acesso condicionado ao spike de política/API |
| RF-02 | Listagem progressiva de amigos | Dados locais aparecem sem esperar rede; online não espera download completo de offline |
| RF-03 | Busca e filtros | Nome, status e plataforma combináveis; filtros persistem e podem ser limpos |
| RF-04 | Organização local | Categorias, pins e notas não alteram favoritos remotos sem ação explícita |
| RF-05 | Mundos | Detalhes principais independentes da busca de instâncias e proprietários |
| RF-06 | Instâncias | Amigos agrupados por ID completo da instância; acessibilidade não inferida só pela presença de amigos |
| RF-07 | Coleções | Adicionar/remover mundos, renomear coleção e operar offline |
| RF-08 | Feed | Paginação, filtro por amigo/evento, retenção e lacunas visíveis |
| RF-09 | Atualização | Estado por seção e horário da última observação; erro não equivale a lista vazia |
| RF-10 | Preferências | Tema do sistema/claro/escuro, densidade, idioma e dados locais |
| RF-11 | Diagnóstico | Exportação voluntária com versão, estado e latências sem credenciais ou payloads pessoais |
| RF-12 | Alertas, pós-MVP | Opt-in por amigo/tipo, silêncio e cooldown; sem prometer entrega com processo encerrado |

## Requisitos não funcionais — metas propostas

| ID | Meta | Método |
|---|---|---|
| RNF-01 | Primeira lista local utilizável em até 1 s p95 | Build release/profileable, S23 de referência, 30 partidas frias, 1.000 amigos sintéticos, imagens em cache; excluir primeiro login |
| RNF-02 | Busca local em até 100 ms p95 após debounce de 250 ms | 1.000 amigos, relógio monotônico; medir cálculo e atualização separadamente |
| RNF-03 | Rolagem com menos de 5% de frames janky | Macrobenchmark em lista de 1.000 amigos; medir em 60 Hz e 120 Hz; definir métrica pela ferramenta |
| RNF-04 | Um evento não dispara recarga geral | Teste de rede: atualização conhecida de amigo causa zero refetch integral |
| RNF-05 | Nenhuma perda em migração suportada | Comparar contagens, IDs e conteúdo em fixtures antes/depois |
| RNF-06 | Nenhum segredo em logs/backup | Inspeção automatizada e revisão de artefato |
| RNF-07 | Uso offline inequívoco | Presença histórica rotulada como desatualizada; não exibir como ao vivo |

Metas não são desempenho medido. Custo de rede, memória e bateria recebem orçamento após G0; não estabelecer percentual de ganho sem baseline. A latência do servidor não entra como promessa de abertura da UI.

## Fora de escopo

iOS/web, backend de coleta, dados privados inacessíveis, scraping massivo, descoberta de localização oculta, chatbot/IA, uploads de avatar/mundo, Discord com token pessoal, multiaccount, sincronização em nuvem e notificações garantidas 24/7. Recursos existentes no fork podem permanecer no histórico, mas não precisam estar expostos na primeira versão.

## Pesquisa curta antes de congelar UX

Analista observa três tarefas no VRCAA: achar um amigo, escolher uma instância e guardar um mundo. Registrar toques, esperas e confusão em dispositivo/versão conhecidos, sem copiar dados pessoais para tickets. Nate prioriza cinco faltas reais. Validar protótipo com essas mesmas tarefas; resultado vira alteração de backlog, não refaz toda a arquitetura.
