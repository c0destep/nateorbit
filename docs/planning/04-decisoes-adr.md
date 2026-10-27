# Registro de decisões

Status “adotada” significa decisão desta proposta, não implementação. Reabrir por ADR que descreva nova evidência, impacto e migração.

| ADR | Status | Decisão | Alternativa e consequência | Gatilho para revisão |
|---|---|---|---|---|
| 001 | Adotada | Fork incremental com commit base fixado | Reescrita completa perde conhecimento de API e aumenta prazo | Fronteiras legadas impedem duas entregas seguidas |
| 002 | Adotada | Android nativo Kotlin/Compose | Flutter/React Native/Tauri exigiriam reimplementar integração e lifecycle | Necessidade real e financiada de iOS |
| 003 | Adotada | Local-first e estados independentes | Cache global mantém telas dependentes de recursos irrelevantes | Evidência de complexidade maior que ganho em um recurso |
| 004 | Adotada | Sem backend/analytics remoto | Servidor simplifica alertas mas cria custódia de sessão e custo | Requisito explícito e revisão de política/privacidade |
| 005 | Adotada | Uma conta ativa; dados escopados | Multiaccount já aumenta superfície e testes | Caso validado após 1.0 |
| 006 | Condicional | Não persistir senha; SessionStore separado | Copiar prefs antigas mantém risco; método real depende de política | Resolução documentada da autenticação |
| 007 | Adotada | Manter Glide/Voyager no primeiro ciclo | Trocar rede, imagens, navegação e UI juntos atrapalha diagnóstico | Incompatibilidade reproduzida ou custo mensurado |
| 008 | Adotada | Room e migrações explícitas | SQL manual dificulta contratos; Room também exige testes reais | Schema/importador não puderem ser migrados com segurança |
| 009 | Adotada | Categorias locais distintas de favoritos VRChat | Sincronizar silenciosamente surpreende e altera conta | Usuário pedir sincronização com confirmação por ação |
| 010 | Adotada | Histórico observado, retenção padrão 30 dias | Histórico ilimitado amplia dados e não recupera lacunas | Necessidade pessoal explícita de retenção maior |
| 011 | Adotada | Branches curtas, PR e revisão independente | GitFlow pesado adiciona integração tardia | Várias versões de manutenção simultâneas |
| 012 | Proposta | NateOrbit, licença Apache 2.0 para o derivado | Nome ainda não liberado; outra licença para adições seria possível | Validação de marca ou preferência do proprietário |
| 013 | Adotada | Alertas contínuos ficam após MVP | Prometer 24/7 no celular ignora lifecycle e bateria | Spike mostra comportamento e limitações aceitáveis |
| 014 | Adotada | Biblioteca de API comunitária não substitui contrato testado | SDK gerado pode reduzir código, mas também quebrar modelos | Prova de compatibilidade e manutenção superior |

## ADR-006 detalhada: autenticação

Contexto: upstream armazena senha/tokens em preferências. Diretrizes atuais do VRChat apresentam restrições amplas para solicitar/guardar credenciais, incluindo tokens e sessão. Criptografar protege tecnicamente, mas não resolve permissão da plataforma.

Decisão: definir SessionProvider testável e usar fixtures no trabalho inicial. Não inventar OAuth, autorização via WebView, extração de cookies de navegador ou importação manual de token como “solução permitida”. Analista/lead registram viabilidade atual e, se necessário, buscam esclarecimento com VRChat antes de integração/distribuição a terceiros. Nenhuma mensagem externa foi enviada neste planejamento.

Consequência: UI, dados, testes, marca e sincronização simulada podem avançar; teste autenticado e release conectado ficam condicionados a essa decisão. Se não houver caminho aceitável, replanejar para organizador local com links oficiais ou adiar integração.
