# Origem e rastreabilidade

Upstream: https://github.com/Nyabsi/VRCAA
Base: eb3978247d969e2c593837175fc7598e95f51b35
Data desta preparação: 27/10/2026
Licença: Apache-2.0. Copyrights originais preservados.

O checkout de preparação preserva o histórico Git completo obtido do upstream.
Destino do projeto: https://github.com/c0destep/nateorbit. Remoto `origin` aponta
para esse destino; `upstream` é opcional em novos clones. A importação inicial no
GitHub uniu a base fixada e o commit de preparação com dois pais, preservando
rastreabilidade sem force push. Commit de importação confirmado:
`d9902091568c9be990ff466271ba97d3031d4623`. A árvore remota contém 510 arquivos
e não contém o workflow de importação nem a publicação nightly herdada.

README e workflow nightly originais estão em docs/upstream. O nightly foi retirado de .github/workflows para impedir publicação agendada herdada. O CI novo apenas compila/testa/linta debug e publica relatórios de job; não faz release de APK.

Acompanhar upstream semanalmente. Revisar correções de API/modelos e aplicar seletivamente com testes. Não mesclar mudanças de credenciais ou marca automaticamente.
