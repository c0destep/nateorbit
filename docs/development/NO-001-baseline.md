# NO-001 — baseline reproduzida

Data: 27/10/2026. Status: Done para o aceite de build smoke; revisão humana pendente.
Código validado: `5761edde7f135efcecfdeba876396de0ea141b23`, checkout limpo em
`/workspace/nateorbit`, derivado da base upstream fixada em UPSTREAM.md.
Esta é a baseline do fork nesse SHA, não uma recompilação isolada do upstream.

## Ambiente e reprodução

Linux x86_64, JDK completo Temurin 21.0.9+10, Python 3, Gradle wrapper 9.3.1
com checksum preservado, AGP 9.0.1 e Kotlin 2.3.10. Android API 36 revisão 2,
Build-Tools 36.0.0, Platform-Tools 37.0.1, Command-line Tools 19.0.

No ambiente cloud preparado:

```bash
source /workspace/toolchains/activate.sh
cd /workspace/nateorbit
make doctor
bash scripts/check.sh --max-workers=4
sha256sum app/build/outputs/apk/standard/debug/app-standard-debug.apk
```

Em outra máquina, seguir LINUX.md com essas versões. Os caminhos acima são
locais ao ambiente cloud. O script de instalação e as instruções de ativação
foram salvos no rascunho do ambiente; publicação/restauração não foram verificadas.

## Evidências

- [Execução Android](evidence/no-001/android-check.log): BUILD SUCCESSFUL,
  7m47s, 55 tarefas executadas; assembleStandardDebug, testStandardDebugUnitTest
  e lintStandardDebug concluídos.
- `make verify`: dois verificadores aprovados e sete testes dos scripts aprovados.
- [JUnit](evidence/no-001/unit-test.xml): um teste aritmético herdado, zero falhas,
  zero erros e zero ignorados. Não cobre domínio ou integração.
- Lint: 137 avisos, zero erros. Relatórios completos locais em
  `app/build/reports/lint-results-standardDebug.{html,xml}`.
- [Repetição do setup](evidence/no-001/repeat-setup.log): sucesso em 19s,
  uma tarefa executada e 54 atualizadas; valida reaproveitamento, não build limpo.

APK local: `app/build/outputs/apk/standard/debug/app-standard-debug.apk`.
SHA-256: `0b1dfc9fcd307c42041da2a137beada2cf3a67c39a5bf2412e84adb88ea473dd`.
O [registro do hash](evidence/no-001/apk.sha256) permite identificar esse binário;
não implica build bit a bit reproduzível, pois assinatura debug e metadados Git
podem variar. O APK não foi adicionado ao Git nem publicado como release.

## Diagnóstico e limites

As falhas iniciais eram do ambiente: runtime sem javac, SDK ausente, Java sem
proxy e diretório pessoal protegido. Resolvidas com ferramentas/caches graváveis
em `/workspace/toolchains`, proxy fornecido e truststore do sistema, sem desligar
TLS ou checksum. O usuário aceitou explicitamente a licença do SDK.

Houve um erro do helper de instalação após os checks aprovados porque ele foi
editado durante a execução. O helper final passou na verificação de sintaxe e
na repetição integral, com saída zero. Não foi erro do app.

Persistem avisos de métricas locais, integração AboutLibraries, APIs obsoletas e
assinatura release ausente; não impediram as tasks debug. Instrumentação, UI,
login real, desempenho e bateria não foram testados. NO-002 exige aparelho e
protocolo; NO-003/NO-009 seguem bloqueando validação autenticada. G0 não está concluído.
