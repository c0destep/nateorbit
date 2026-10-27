# Início do desenvolvimento

## Ambiente

JDK 21 completo (java e javac), Python 3, Git e Android SDK. O wrapper fixa Gradle 9.3.1 com checksum; AGP 9.0.1, Kotlin/Compose 2.3.10 e SDK 36 vêm do upstream. Não atualizar versões para resolver problemas sem primeiro registrar a causa.

No Android Studio, abrir a raiz deste projeto. Em Settings > Build, Execution, Deployment > Build Tools > Gradle, selecionar JDK 21 em Gradle JDK. Em SDK Manager instalar Android API 36, Android SDK Build-Tools 36.0.0 e Android SDK Platform-Tools. Os nomes podem variar com a versão instalada.

No terminal Linux, configurar JAVA_HOME para o JDK 21 instalado e ANDROID_HOME para o SDK real. O script doctor também aceita sdk.dir em local.properties, que é ignorado pelo Git. Não copiar caminho de outra máquina. Java 17 presente no ambiente desta preparação é insuficiente para a toolchain definida.

Comandos na raiz:

```bash
python3 scripts/verify_bootstrap.py
python3 scripts/doctor.py
bash scripts/check.sh
```

No Windows com PowerShell, executar os dois scripts Python e depois:

```powershell
.\gradlew.bat assembleStandardDebug testStandardDebugUnitTest lintStandardDebug --no-daemon
```

As tasks da variante standardDebug passaram no CI inicial; veja VALIDATION.md para commit e evidência. O teste aritmético herdado não substitui a suíte de domínio planejada.

## Rede

É necessário alcançar services.gradle.org, os mirrors de distribuição Gradle, Google Maven e Maven Central. Não guardar caches nem SDK no repositório. Neste ambiente o download do Gradle retornou Network is unreachable; isso ocorreu antes da configuração/compilação Android.

## Linux e Codex

Seguir [LINUX.md](LINUX.md) para JDK/SDK e [CODEX.md](CODEX.md) para as skills do
repositório e exemplos de tarefas. `make verify` funciona sem SDK; `make check`
executa os checks Android completos.

## Destino GitHub

Repositório de trabalho: https://github.com/c0destep/nateorbit.
`origin` deve apontar para esse destino. `upstream`, se configurado localmente,
aponta para https://github.com/Nyabsi/VRCAA.git apenas para acompanhamento.
Nunca enviar alterações ao upstream. A branch main será a base das novas tarefas.

## Trabalho inicial

Leia planning/sprint-01.md, AGENTS.md e CONTRIBUTING.md. Nomeie pessoas reais nos papéis e ative proteção de branch após o primeiro CI. Não criar regras para checks que ainda não foram executados. Sessão e background do legado continuam pendentes de refatoração; a base não é um APK novo pronto para uso conectado.
