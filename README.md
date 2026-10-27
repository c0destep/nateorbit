# NateOrbit

Assistente Android pessoal para amigos e mundos do VRChat, derivado de [Nyabsi/VRCAA](https://github.com/Nyabsi/VRCAA).

**Estado: bootstrap de desenvolvimento.** Código funcional herdado do VRCAA, nova identidade de desenvolvimento e planejamento incorporado. A nova arquitetura e as funcionalidades planejadas ainda serão implementadas. A compilação Android desta branch está pendente de validação em ambiente com JDK 21, Android SDK e acesso aos repositórios Gradle.

## Começar

[Linux](docs/development/LINUX.md) · [Codex e skills](docs/development/CODEX.md)


1. Leia [START-HERE](docs/development/START-HERE.md).
2. Execute `python3 scripts/verify_bootstrap.py` e `python3 scripts/doctor.py`.
3. Com o ambiente preparado, execute `bash scripts/check.sh`.
4. Selecione a próxima tarefa na [Sprint 01](planning/sprint-01.md).

[Planejamento completo](docs/planning/00-plano-executivo.md) · [Backlog JSON](planning/backlog.json) · [Contribuição](CONTRIBUTING.md) · [Origem](UPSTREAM.md) · [Estado da validação](docs/development/VALIDATION.md)

## Identidade e limites atuais

- Nome de trabalho: NateOrbit. applicationId de desenvolvimento: `dev.nateorbit.app`; debug recebe `.dev` por configuração herdada.
- Namespace Kotlin permanece `cc.sovellus.vrcaa` para manter referências de código/manifesto durante a preparação.
- Ícones launcher, recursos e diversas telas ainda são do upstream. A arte em `brand/` é conceito e não substitui ícones de produção.
- Links de suporte/doação e integração de conta herdados continuam no código; não distribuir esta base como produto final antes da revisão prevista.
- A primeira entrega trabalhará com dados sintéticos. O fluxo de login herdado ainda precisa da decisão de NO-003 e da correção de sessão NO-009 antes de validação conectada.

## Licença

Código upstream sob [Apache 2.0](LICENSE), com atribuições preservadas. Veja [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Arquivos de origem modificados nesta preparação contêm avisos. Planejamento e conceito visual não equivalem a verificação de marca ou inventário completo de dependências.
