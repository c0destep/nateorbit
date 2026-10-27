# Trabalhar com Codex

O AGENTS.md da raiz contém as instruções comuns. As cinco skills ficam em
.agents/skills, localização de descoberta de skills de repositório do Codex.
Não é necessário copiar arquivos para a pasta pessoal de skills.
Não foi instalado nenhum plugin/MCP adicional nem alterado ~/.codex/config.toml.

## Primeira sessão no Linux

Preparar JDK/SDK em [LINUX.md](LINUX.md), clonar e iniciar na raiz:

```bash
git clone https://github.com/c0destep/nateorbit.git
cd nateorbit
make verify
make doctor
codex
```

O comando pressupõe Codex CLI já instalado e autenticado. Em IDE/app, abrir a mesma
pasta do clone. Verificar versão com `codex --version`; usar `codex --help` para a
sintaxe da instalação disponível. Instalação oficial: https://developers.openai.com/codex/cli.
Não instalar uma versão móvel do CLI ou fixar modelo em arquivos deste projeto.

Solicitar ao Codex: “Resuma as instruções deste repositório e liste as skills
nateorbit disponíveis antes de alterar arquivos.” Confirmar leitura do AGENTS.md
na raiz e das skills. Se não aparecerem, conferir diretório atual e versão do CLI;
abrir uma nova sessão na raiz se necessário. Detalhes de descoberta dependem do host.

## Pedidos prontos

| Objetivo | Prompt |
|---|---|
| Refinamento | Use $nateorbit-plan-task para refinar NO-007 com aceite e dependências. |
| Implementação | Use $nateorbit-android-feature para implementar a fatia aprovada de amigos com repository fake, sem login real. |
| Revisão | Use $nateorbit-sync-review para revisar o diff desta branch e apontar regressões verificáveis. |
| Testes | Use $nateorbit-verify para validar esta alteração e registrar o que foi executado. |
| Linux | Use $nateorbit-linux para diagnosticar JDK/SDK antes do primeiro build. |

Rodar a revisão em sessão independente, com o diff e o aceite disponíveis. Isso
pode ser feito por outra pessoa ou outra sessão; não depende de subagentes.

## Papéis e saída

Analista refina o item; implementador entrega uma fatia; revisor procura regressões;
QA reproduz os critérios. Papéis não são contas atribuídas automaticamente.
Usar docs/templates para história, PR, revisão e handoff. Não marcar Done sem evidência.

Modelo/esforço são escolhas da instalação/conta. Estas skills não selecionam modelos,
não criam agentes especialistas nem garantem que o CLI exponha os dados de um agente.
Se delegação for solicitada e disponível, registrar somente metadados observados.

## Codex remoto e rede

Com provisionamento de JDK 21 e Command-line Tools previamente disponível, configurar
JAVA_HOME/ANDROID_HOME e executar `bash scripts/setup-linux.sh --install-sdk` na etapa
de setup, aceitando as licenças conforme a política do executor. Depois executar
`make check`. Com rede indisponível, `make verify` continua útil, mas não valida Android.
Emulador/KVM e conta VRChat não são pré-requisitos de build/testes unitários.

## Referências verificadas em 27/10/2026

- Skills: https://developers.openai.com/codex/skills
- AGENTS.md: https://developers.openai.com/codex/guides/agents-md
- CLI: https://developers.openai.com/codex/cli
