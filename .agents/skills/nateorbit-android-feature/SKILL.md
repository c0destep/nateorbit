---
name: nateorbit-android-feature
description: Implementar funcionalidades Kotlin/Compose no NateOrbit por refatoração incremental do VRCAA. Usar para uma fatia de UI, estado ou repository.
---

# Implementar uma fatia Android

Ler AGENTS.md, a história e docs/planning/03-arquitetura-e-dados.md.
Inspecionar Screen/ScreenModel e managers envolvidos no fluxo legado.

- Manter namespace e variante standardDebug. Reutilizar Voyager/ScreenModel e Glide
  quando suficientes. Não introduzir módulos/frameworks só para atender a um desenho.
- Definir o contrato mínimo de repository, injetável por construtor. Implementar
  fake determinístico antes da integração remota quando ela estiver bloqueada.
- Representar conteúdo, refresh e erro recuperável separadamente. Preservar conteúdo
  visível e permitir sucesso de amigos antes de recomendações/detalhes secundários.
- Mover filtros/ordenação caros para o modelo de tela; fornecer keys por ID às listas.
  Prever vazio, cache antigo, offline e erro parcial. Usar recursos de strings e
  semântica acessível; status não depende somente da cor.
- Adicionar regressão que falhe no comportamento anterior. Para coroutines/tempo,
  usar relógio/dispatcher controlável; não usar sleep para sincronizar testes.
- Rodar make check e testes pertinentes. Para UI, conferir tema claro/escuro, fonte
  grande e TalkBack quando houver aparelho; declarar o que não foi verificado.

Entregar diff limitado à história, evidência de aceite e handoff com limitações.
