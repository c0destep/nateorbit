# NateOrbit — plano executivo v1.0

Data: 27/10/2026. Responsável pelo produto: Nate. Status: proposta pronta para refinamento e início da fundação; não representa software implementado, benchmark executado ou publicação autorizada.

## Decisão principal

Construir um derivado Android do VRCAA por refatoração incremental. Preservar a história Git e o conhecimento da integração; substituir gradualmente carga global, persistência de sessão, acesso a dados e experiência visual. Evitar reescrita integral e migração simultânea de todas as bibliotecas.

Base fixada: Nyabsi/VRCAA, commit `eb3978247d969e2c593837175fc7598e95f51b35`. A análise anterior examinou código, não executou o app. Os gargalos descritos são hipóteses apoiadas em fluxos observáveis; o primeiro marco mede o impacto real.

## Produto

NateOrbit: amigos e mundos, no seu ritmo. Assistente pessoal para consultar presença, organizar amigos e coleções de mundos, acompanhar eventos observados e decidir onde entrar. Não é cliente de jogo nem ferramenta para descobrir informações privadas.

Nome de trabalho selecionado para personalização e diferenciação. Busca web exata por “NateOrbit” em 27/10/2026 sem resultados; não é busca de marca, domínio ou disponibilidade em lojas. Identidade sujeita a validação antes de divulgação pública.

## Escopo da primeira entrega

- Android para telefone; uma conta por instalação; PT-BR e inglês.
- Amigos com busca, filtros, favoritos remotos e categorias locais claramente separadas.
- Mundos com detalhes progressivos, instâncias acessíveis, coleções e notas locais.
- Feed local paginado, indicador de atualização e intervalos sem observação.
- Persistência offline de leitura, tratamento de erros e sessão isolada.
- Identidade nova, acessibilidade, diagnósticos locais redigidos e testes de regressão.

Depois do MVP: alertas seletivos, modo de acompanhamento em segundo plano validado, backup/importação e favoritos remotos editáveis. Recomendações avançadas, integrações externas e suporte a headsets não entram no caminho crítico.

## Estrutura de entrega

1. G0: build base reproduzido, baseline de desempenho, inventário de licenças e decisão sobre autenticação/API.
2. G1: fundação local, sessão isolada e sincronização testável com dados sintéticos.
3. G2: amigos e mundos utilizáveis sem bloqueio por recursos secundários.
4. G3: beta pessoal com feed, acessibilidade, migrações e recuperação testadas.
5. G4: versão pessoal 1.0; publicação pública é decisão separada.

## Premissas e limites

Equipe de referência: dois desenvolvedores Android, QA dedicado e analista/design/lead em dedicação parcial. Planejamento de 12–16 semanas é faixa inicial, não compromisso: recalibrar após baseline e duas iterações. Sem servidor próprio ou telemetria remota no MVP; nenhuma taxa de API é presumida oficialmente permitida.

Nate decide prioridade, identidade e aceitação do produto; lead decide detalhes reversíveis dentro dos ADRs; segurança e QA produzem evidências, não apenas aprovação verbal. Acesso real à API depende da resolução do risco descrito em Segurança. O restante pode avançar com fixtures.

## Pacote

Documentos de produto, auditoria, arquitetura/dados, ADRs, UX, marca, backlog, equipe, QA, roadmap, segurança/release, migração e fontes. Templates para história, bug, PR, revisão e release. Backlog JSON é a fonte estruturada; CSV é intercâmbio, não planilha de cálculo. Conceito de logo é exploratório e não substitui vetor/adaptive icon validado.
