# Desenvolvimento Android no Linux

## Pré-requisitos fixados

| Componente | Versão / origem |
|---|---|
| JDK completo | 21, com java e javac |
| Python | 3.10+; scripts usam somente biblioteca padrão |
| Ferramentas | Git, Bash, GNU Make, unzip para Command-line Tools |
| Gradle | 9.3.1 pelo ./gradlew, checksum no wrapper |
| Android Gradle Plugin / Kotlin | 9.0.1 / 2.3.10, build.gradle.kts |
| Android | API 36, Build-Tools 36.0.0, Platform-Tools |
| IDE | Android Studio opcional para build, recomendado para Compose/emulador |

scripts/android-env.json fixa os componentes do setup/doctor. Ao mudar versões,
alinhar esse arquivo, build, CI e documentação na mesma alteração. Não usar npm,
Composer, servidor web ou Docker para compilar este app. Nada aqui habilita serviços.

## 1. JDK e ferramentas

No Fedora, instalar o JDK **de desenvolvimento** 21 pelo gerenciador da distribuição
(pacote habitual java-21-openjdk-devel), além de git, make, python3 e unzip.
Em Debian/Ubuntu, o nome habitual é openjdk-21-jdk; verificar disponibilidade na versão
instalada. Não substituir o Java global se outros projetos dependem dele.

Selecionar o diretório real do JDK 21 em JAVA_HOME e adicionar seu bin ao PATH desta
sessão. Confirmar `java -version` **e** `javac -version`. O JBR da IDE pode ter outra
versão; em Settings > Build, Execution, Deployment > Build Tools > Gradle selecionar
um JDK 21 em Gradle JDK para alinhar IDE e terminal.

## 2. Android SDK

Pelo Android Studio: Tools > SDK Manager. Em SDK Platforms instalar Android API 36.
Em SDK Tools, ativar Show Package Details e instalar Android SDK Build-Tools 36.0.0,
Android SDK Platform-Tools e Android SDK Command-line Tools (latest).
Conferir o caminho em Android SDK Location; em Linux frequentemente ~/Android/Sdk.

Sem IDE: baixar Command line tools only para Linux da página oficial do Android
Studio, conferir o checksum publicado e extrair de modo que o executável fique em
`$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager` (evitar cmdline-tools aninhado).
Não fixamos uma URL de ZIP temporária. Fonte: https://developer.android.com/studio.

Na raiz do projeto:

```bash
mkdir -p local
cp scripts/linux-env.sh.example local/linux-env.sh
# Editar JAVA_HOME e ANDROID_HOME em local/linux-env.sh para seus caminhos reais.
source local/linux-env.sh
bash scripts/setup-linux.sh --install-sdk
make doctor
```

A instalação apresenta o prompt oficial de licenças e instala somente os componentes
listados em scripts/android-env.json. Não instala JDK, CLI Codex ou pacotes de sistema,
nem altera ~/.bashrc ou ~/.zshrc. Pode ser repetida após uma instalação parcial.
`bash scripts/setup-linux.sh --check` apenas diagnostica.

O doctor também lê sdk.dir de local.properties se ANDROID_HOME não estiver definido.
Evitar ANDROID_HOME e ANDROID_SDK_ROOT apontando para SDKs diferentes. Arquivos locais,
SDK, caches e segredos são ignorados pelo Git; nunca colocar senhas no exemplo.

## 3. Compilar e validar

```bash
make verify
make doctor
make check
```

Build/testes/lint: variante standardDebug. APK esperado após sucesso:
app/build/outputs/apk/standard/debug/app-standard-debug.apk.
Relatórios em app/build/reports e app/build/test-results. `make build`, `make test`
e `make lint` permitem ciclos direcionados. O primeiro build baixa Gradle/dependências;
rodar `--offline` só funciona após os artefatos necessários estarem em cache.

Hosts típicos: services.gradle.org e seu redirecionamento de distribuição,
plugins.gradle.org, dl.google.com, maven.google.com e repo.maven.apache.org.
Restrições do executor precisam permitir os downloads. Erro de rede não se resolve
alterando dependências. Proxy/TLS devem seguir a configuração legítima da organização.

## 4. Dispositivo ou emulador (opcional)

Build e testes unitários não exigem emulador. Para instrumentação local:

- Habilitar virtualização no firmware e verificar `/dev/kvm` e `emulator -accel-check`.
  Configurar acesso ao KVM conforme sua distribuição; não usar chmod 666 nem
  desativar Secure Boot. O Android Emulator não exige iniciar libvirtd.
- No Android Studio: Tools > Device Manager > Create Virtual Device; escolher
  imagem compatível com a arquitetura do host, preferencialmente API 36 para o smoke.
  A matriz de QA completa está em docs/planning/09-qualidade-e-testes.md.
- Alternativa: no aparelho, ativar Developer options > USB debugging, conectar e
  autorizar a chave da máquina. `adb devices` deve mostrar device, não unauthorized.
- Com um único destino pronto: `make connected-test`. Para vários, selecionar um
  destino no Android Studio ou reduzir aos dispositivos pretendidos antes de rodar.

`make install-debug` instala o APK no destino conectado. O app herdado ainda possui
login real e não tem modo demo pronto; não autenticar durante a preparação offline.
No S23, registrar a versão Android/API real em QA, sem inferir a partir da One UI.

## Problemas frequentes

| Sintoma | Ação |
|---|---|
| Java 17 ou javac ausente | Selecionar JDK completo 21 em JAVA_HOME e Gradle JDK |
| SDK não localizado | Corrigir ANDROID_HOME ou sdk.dir; conferir caminho real |
| Licenses not accepted | Rodar sdkmanager --licenses no SDK escolhido e ler os termos |
| Permission denied em gradlew | Conferir bit executável; usar chmod +x gradlew no clone |
| Network/TLS failure | Identificar host/etapa; não desligar validação TLS |
| Kotlin/AGP falha depois do download | Guardar stacktrace, SHA e versões; tratar como erro do projeto |
| Sem KVM/dispositivo | Rodar build/testes unitários/lint; declarar instrumentação pendente |

## Fontes

- https://developer.android.com/tools/sdkmanager
- https://developer.android.com/tools/variables
- https://developer.android.com/studio/run/emulator-acceleration
- [Codex neste projeto](CODEX.md)
