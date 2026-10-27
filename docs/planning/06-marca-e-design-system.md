# NateOrbit — identidade proposta

## Nome e posicionamento

Nome de trabalho: **NateOrbit**. Pronúncia sugerida: “Nêit Órbit”. Assinatura: “Amigos e mundos, no seu ritmo.” Usar NateOrbit sem “oficial”, sem reproduzir logo VRChat e sem insinuar parceria. Descrição curta: “Seu assistente pessoal para organizar amigos e mundos no VRChat”.

Racional: Nate personaliza a origem; Orbit comunica proximidade e circulação entre mundos. O nome é provisório para distribuição pública. Busca exata na web em 27/10/2026 sem resultados; INPI, lojas, domínios e perfis não foram verificados/registrados. Não comprar nem registrar nada automaticamente. Alternativa se desejar marca menos pessoal: conduzir nova rodada de naming com os mesmos critérios, mantendo o símbolo independente do texto.

## Logo

Conceito entregue em `brand/nateorbit-brand-concept.png`: duas órbitas cruzadas e um ponto de presença, wordmark e demonstrações de ícone/monocromia. Arte gerada por imagem para direção visual. É raster e não um pacote final de lançamento; pequenas diferenças entre as miniaturas não são especificação geométrica.

Designer deve redesenhar o símbolo escolhido em vetor único; produzir SVG/PDF vetorial, versão monocromática, foreground/background/monochrome do adaptive icon e PNGs de distribuição. Validar máscaras Android, recorte, contraste, legibilidade a 24/48 dp e espaço de proteção. Não recortar a prancha e chamar o resultado de ícone final.

Regras propostas: margem de proteção equivalente ao diâmetro do ponto; não deformar nem girar a marca; sem brilho pesado, bevel ou detalhes finos; wordmark não aparece no launcher. Em fundo claro, texto em Ink e símbolo com variante escurecida testada. No app, preferir símbolo discreto à repetição do nome em cada tela.

## Tokens iniciais

| Token | Escuro | Claro | Uso |
|---|---|---|---|
| background | #0B1020 | #F7F8FC | Fundo |
| surface | #151C30 | #FFFFFF | Superfícies |
| text | #F4F7FF | #111827 | Texto principal |
| muted | #B5C0D6 | #475569 | Texto secundário |
| primary | #A78BFA | #6D28D9 | Ação principal |
| accent | #67E8F9 | #0E7490 | Acentos |
| danger | #FDA4AF | #BE123C | Erro |

Valores exatos estão em `brand/tokens.json`; a arte exploratória pode variar. Status VRChat mantém rótulos de domínio, sem deduzir significado de cor. Paleta semântica de status será testada separadamente, não herdada da cor da marca.

Tipografia de UI: fonte padrão Android/Roboto para reduzir ativos e favorecer legibilidade; títulos 24/20 sp, corpo 16 sp, legenda 12–14 sp. Wordmark final deve usar fonte com licença documentada ou desenho original em curvas. Espaçamento 4/8/12/16/24/32 dp; raios 12/16/24 dp. Ícones Material Symbols com licença incluída quando efetivamente incorporados; não adicionar dependência só por esta especificação.

## Entregáveis de marca antes do beta público

Nome validado, master vetorial, ícones adaptativos, tema claro/escuro, tela Sobre com atribuições, screenshots com dados sintéticos e textos de loja não enganosos. A assinatura do APK, applicationId e domínio não são escolhidos só porque o nome está escolhido.

## Proveniência

Conceito produzido com ferramenta integrada de geração de imagens; prompt reproduzido em `brand/prompt.txt`. Não houve certificação de exclusividade, registro de marca ou validação de loja. Uso público exige revisão visual e de direitos pelo responsável.
