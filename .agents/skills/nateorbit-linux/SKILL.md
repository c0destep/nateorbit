---
name: nateorbit-linux
description: Preparar ou diagnosticar o ambiente Android Linux do NateOrbit. Usar para JDK, SDK, Gradle, emulador ou onboarding local/Codex em Linux.
---

# Preparar Linux

Ler docs/development/LINUX.md, scripts/android-env.json e scripts/doctor.py.
Executar make verify e make doctor antes de mudar o ambiente.

- Identificar se é máquina local ou executor remoto, arquitetura, java/javac ativos,
  JAVA_HOME, ANDROID_HOME e presença de sdkmanager. Não imprimir ambiente completo.
- Usar JDK 21 e Gradle wrapper do projeto. Resolver JAVA_HOME no shell e Gradle JDK
  no Android Studio; não instalar um Gradle global nem atualizar versões do app.
- Seguir o procedimento Linux para instalar Command-line Tools e os componentes
  fixados. bash scripts/setup-linux.sh --install-sdk altera somente o SDK escolhido
  e apresenta a aceitação de licenças oficial; --check apenas diagnostica.
- Manter local.properties, SDK, caches e keystores fora do Git. Não alterar perfis
  de shell globais, desabilitar Secure Boot nem iniciar serviços automaticamente.
- Build headless dispensa emulador. Para emulador local, verificar KVM e usar Device
  Manager. Para dispositivo, exigir conexão já autorizada. Não iniciar app legado
  com conta real para validar ambiente.
- Rede bloqueada: registrar host/etapa e continuar checks offline; não contornar
  restrições de rede ou confundir cache pré-existente com build reproduzido.

Concluir com make doctor e, se possível, make check; relatar limites reais.
