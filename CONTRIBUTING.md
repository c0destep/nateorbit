# Desenvolvimento em equipe

Use [Sprint 01](planning/sprint-01.md) e os templates em docs/templates. Branches curtas: feat/NO-xxx-resumo ou fix/NO-xxx-resumo. Commits semânticos em inglês ou português consistente; não incluir segredo nem arquivo de configuração local.

PR deve explicar problema, resultado e evidências. Um revisor independente verifica comportamento; QA registra ambiente e critérios. Sessão, migração e release requerem revisão adicional do lead/segurança. CODEOWNERS será criado quando houver identidades reais do time.

Antes da PR: python3 scripts/verify_bootstrap.py; para alterações Android: bash scripts/check.sh. Benchmarks e testes físicos seguem docs/planning/09-qualidade-e-testes.md. Informe comandos que falharam e limites do ambiente; não marcar Android validado apenas porque checks estruturais passaram.

Definition of Done e RACI: docs/planning/08-equipe-e-processo.md. Sobre origem e manutenção do fork: UPSTREAM.md.
