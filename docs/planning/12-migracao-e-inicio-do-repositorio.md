# Migração e preparação do repositório

## Estado deste pacote

Nenhum fork remoto foi criado, nenhuma issue publicada e nenhum código do app alterado. O pacote define a execução para um repositório de destino ainda não informado. O commit upstream é conhecido e deve ser preservado; o planejamento não é um clone completo do VRCAA.

## Sequência para o time

1. Criar fork ou repositório derivado preservando histórico; configurar remoto upstream para Nyabsi/VRCAA e origin para destino de Nate. Não substituir remotos de um checkout desconhecido.
2. Fixar branch de baseline no SHA do plano; registrar build/versões e tag interna de referência.
3. Importar `docs/`, `brand/` e templates deste pacote. Revisar cada política antes de ativá-la; não copiar placeholders para CODEOWNERS.
4. Manter licença e avisos; inventariar third-party e recursos de marca upstream.
5. Criar branch de bootstrap: applicationId próprio, app_name, canais, links de suporte e chave debug; release signing separado.
6. Adicionar fixtures e gateway de compatibilidade; manter build funcionando antes de mover módulos.
7. Introduzir Room e repository de amigos; adaptar eventos para escritor único; UI nova por feature flag local.
8. Migrar Amigos e depois Mundos; desativar caminho antigo só após testes de paridade.
9. Extrair módulos quando fronteiras estiverem estáveis; remover dependências legadas sem consumidores.
10. Revisar commits upstream semanalmente; cherry-pick seletivo com licença e testes. Não fazer merge cego de mudanças de auth/modelos.

## Dados existentes do VRCAA

Outro applicationId significa outro sandbox: NateOrbit não pode ler diretamente os dados privados do VRCAA. Não prometer migração automática de senha, cookie ou banco. Primeira versão pode começar vazia e carregar dados permitidos da conta após autenticação validada.

Importador pós-MVP: identificar formato real do export upstream em spike; usuário seleciona arquivo pelo Storage Access Framework; validar versão, tamanho e schema; pré-visualizar contagens; importar apenas histórico/coleções compatíveis em staging; resolver colisões por IDs e origem; transação atômica e relatório. Nunca importar sessão. Na ausência de formato suportado, comunicar isso e não pedir root ou acesso ao sandbox.

## Migrações internas do NateOrbit

Schema próprio começa em v1, independente do DATABASE_VERSION do VRCAA. Para updates do mesmo app, versões Room e testes de todos os caminhos suportados. Nada de fallbackToDestructiveMigration em dados pessoais. Backup pré-migração exclui segredos; testar interrupção, disco insuficiente e versão futura recusada.

## Política de paridade

Classificar cada função upstream: manter, adaptar, ocultar ou remover. MVP precisa cumprir RF-01–RF-11, não replicar todos os recursos VRCAA. Tela retirada deve ter decisão no changelog do derivado. Não listar como “nova” uma função já existente sem explicar a diferença.

## Questões ainda abertas e donos

Repositório/organização e identidade técnica definitiva — Nate. Autenticação/API — lead + analista + Nate. Disponibilidade de marca — Nate/design. Versão real do aparelho e baseline — QA. Formato de backup upstream — dev dados. Equipe/capacidade real — Nate. Licenças dos ativos finais — designer/release. Essas respostas refinam o plano; não impedem trabalho com fixtures e design.
