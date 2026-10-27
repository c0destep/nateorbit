# Segurança, licenças e distribuição

## Duas autorizações diferentes

A Apache 2.0 do código permite derivação sob suas condições. Isso não define os direitos de acesso à plataforma VRChat. As Creator Guidelines consultadas em 27/10/2026, atualizadas em 06/10/2026, dizem que a API pode mudar sem aviso e apresentam restrições a solicitar/armazenar credenciais, incluindo tokens e dados de sessão. Não presumir que uso local ou criptografia elimina essa questão. Registrar uma decisão antes de acesso real e, especialmente, distribuição para outras pessoas. A existência do VRCAA não é prova de autorização para um novo app.

Planejamento segue com fixtures e contratos isolados. Nenhum OAuth oficial é presumido; não capturar cookies de navegador, não adicionar fluxo de token manual como atalho de conformidade. Proprietário e lead devem validar um mecanismo aceitável ou redefinir o escopo conectado. Este é um risco concreto identificado na fonte, não uma condição para produzir a documentação.

## Modelo de ameaças

Ativos: sessão, lista de amigos, localização observada, notas pessoais, chaves de assinatura e backups. Fronteiras: dispositivo, VRChat, CI e exportação voluntária. Ameaças: log contendo segredo, dump de dados enviado a issue, exportação excessiva, mistura de contas, replay de eventos, corrida de logout, dependência comprometida e vazamento do keystore de release.

Controles: senha só em memória se método permitido; segredo de sessão cifrado com chave não exportável do Keystore se persistência autorizada; exclusão de backup automático de sessão; logout cancela jobs e impede callbacks antigos por geração de sessão; logs sem cabeçalhos Cookie/Authorization, query auth e payloads pessoais; fixture sintética em CI. Room não é automaticamente banco criptografado. MVP confia no sandbox e criptografia do dispositivo para dados comuns; necessidade de criptografia adicional de notas deve ser decidida no threat model.

Acesso bloqueado/privado revoga apresentação de localização atual; não usar histórico para contornar privacidade. Retenção de feed padrão 30 dias, configurável para 7/30/90, desligável; limpeza automática local. Não calcular “tempo exato online” a partir de amostragem incompleta. Exportação nunca contém segredos e exige ação explícita.

## Licença do derivado

Proposta: manter Apache 2.0 para o código próprio também. Preservar LICENSE original, copyrights pertinentes e avisos destacados nos arquivos alterados. Se a distribuição upstream incluir NOTICE, reproduzir avisos pertinentes. Inventariar licenças de dependências, fontes e imagens; a licença raiz não resolve automaticamente materiais de terceiros. A cópia em `legal/VRCAA-LICENSE.txt` é referência do upstream, não declaração de que toda arte do pacote é coberta por ela.

Exemplo de anotação para arquivo alterado: “Modified for NateOrbit, 2026: separated friend loading from global initialization.” Não apagar copyright Nyabsi; adicionar aviso das alterações próprias. Criar tela Sobre/Licenças e THIRD_PARTY_NOTICES com origem e commit. Não dizer que o projeto original endossa o derivado.

## Identidade técnica

Usar applicationId próprio e estável antes do beta; proposta temporária de desenvolvimento `dev.nateorbit.app`, sem alegar propriedade de domínio. PO decide namespace definitivo antes de distribuição. Debug com sufixo `.debug`, assinatura própria. Não reutilizar assinatura, links de doação, suporte, analytics, canais Discord ou atualização do autor original.

## CI proposta — não instalada neste pacote

PR: checkout com SHA de action fixado, JDK 21 conforme base, validação Gradle/lockfiles, compilação debug, unitários, lint, testes de migração e detector de segredos. Instrumentados em job apropriado; benchmarks só em aparelho estável, sem comparar runners compartilhados como se fossem equivalentes. Permissão padrão contents:read; publish isolado e só para tag autorizada. Nunca expor segredo de assinatura em PR de fork.

G0 descobre os nomes de tasks reais; comando candidato do upstream `./gradlew assembleStandardDebug testStandardDebugUnitTest lintStandardDebug` deve ser validado antes de virar workflow. O pacote não afirma ter executado esse build.

Release: versão SemVer do derivado começando 0.1.0-dev e versionCode próprio monotônico; tag assinada quando disponível; APK/AAB conforme canal; checksum SHA-256, notas de versão, inventário de licenças, relatório QA e assinatura protegida. APK pessoal por canal privado escolhido pelo PO. Play Store/F-Droid exigem revisão adicional própria; nenhum envio automático.

## Recuperação e suporte

Guardar último APK estável, migrações e backup de dados não secretos. Android não aceita downgrade arbitrário de versionCode e schema; estratégia padrão é forward-fix com código novo e versão maior. Desinstalar para voltar pode apagar dados: não oferecer como rollback simples. Se migração falhar, preservar original e abrir modo de recuperação; nunca apagar banco silenciosamente.

Incidente: interromper distribuição, avaliar exposição, orientar revogação da sessão quando aplicável, corrigir e publicar versão maior após QA. Logs de suporte voluntários, redigidos e com retenção explícita; nenhum dado da conta em issue pública.
