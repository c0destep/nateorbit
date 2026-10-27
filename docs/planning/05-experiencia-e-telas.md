# Experiência e especificação de telas

## Navegação

Quatro destinos inferiores: Amigos, Mundos, Atividade e Você. Coleções ficam dentro de Mundos; categorias dentro de Amigos. Configurações acessíveis em Você. Amigos é a abertura padrão; destino inicial configurável depois do MVP. Busca contextual preserva filtro e posição ao voltar de detalhes.

| Tela | Hierarquia / ações | Carregamento / falhas |
|---|---|---|
| Amigos | Título + busca; resumo da atualização; chips Online/Favoritos/Categorias/Plataforma; pins; lista compacta | Cache primeiro; skeleton só sem cache; refresh não apaga lista; erro parcial em faixa |
| Amigo | Avatar/nome; status textual; mundo/instância quando disponíveis; nota; categoria; favoritos | Localização privada exibida como privada; nunca substituir por último mundo como se atual |
| Mundos | Busca; coleções; recentes; “com amigos”; resultados | Imagens com placeholder; busca remota cancelável; estado vazio distinto de offline |
| Mundo | Capa contida; nome/autor; guardar; descrição; instâncias; detalhes técnicos | Conteúdo principal primeiro; spinner apenas nas instâncias; erros recuperáveis por seção |
| Instância | Nome do mundo; tipo/região; amigos visíveis; ações permitidas | Botão indisponível explica motivo; confirmação antes de ação remota sensível |
| Coleção | Nome/contagem; ordenar; editar; adicionar/remover mundo | Funciona offline; exclusão local com desfazer |
| Atividade | Data; filtros por amigo/tipo; eventos agrupados; carregar mais | Linha de lacuna quando desconectado; sem “histórico completo” |
| Você | Sessão, tema, idioma, privacidade, armazenamento, diagnóstico e licenças | Logout explica destino dos dados; erro de rede não impede limpeza local |

## Fluxos e critérios

Amigos → busca local → detalhe → mundo → instância. Preservar estado ao voltar; no máximo três ações após selecionar amigo para visualizar a instância. Ação de entrar pode ser link oficial/self-invite somente se validada; aplicativo não inicia jogo nem garante elegibilidade.

Mundo → guardar → selecionar/criar coleção → confirmação discreta com desfazer. Guardar em coleção local não chama API de favoritos. Edição remota futura deve dizer “Favoritos do VRChat”.

Offline → lista persistida → faixa “Sem conexão — dados de ...” → reconectar → atualização por seção. Nunca substituir toda a tela por diálogo bloqueante para uma falha de recurso secundário.

Sessão expirada → preservar contexto visual sem revelar segredos → reautenticação pelo método validado → retomar destino. Falha de MFA permite correção; não repetir silenciosamente credenciais inválidas.

## Componentes e acessibilidade

- Alvos de toque pelo menos 48 dp; texto base 16 sp; escala de fonte até 200% sem cortar ações essenciais.
- Contraste alvo WCAG AA: 4,5:1 para texto normal, 3:1 para texto grande e componentes relevantes; medir tokens e estados reais.
- Status por texto/ícone além da cor; TalkBack anuncia nome, status e ação, sem ler cada decoração.
- Layout compacto e confortável; largura 360 dp e paisagem testadas. Cores dinâmicas opcionais sem alterar semântica de status.
- Animações curtas e discretas, respeitar redução/desativação do sistema; nada de shimmer contínuo em conteúdo já disponível.
- Imagens remotas dimensionadas para o slot; fallback e descrição útil; sem bloquear texto por download.

## Microcopy definida

“Atualizado há 2 min”; “Reconectando”; “Não foi possível atualizar. Seus dados anteriores continuam disponíveis”; “Localização privada”; “Categoria neste dispositivo”; “Favoritos do VRChat”; “Este período não foi acompanhado”.

## Entrega do designer

Protótipo navegável de Amigos, detalhe de amigo, Mundo, Coleções e falha/offline; variantes claro/escuro e fonte ampliada; especificação de tokens e estados. A prancha de marca deste pacote não é protótipo de UI. Fazer teste de tarefas com Nate antes de implementar todas as telas. Registrar problemas e critério de sucesso em UX-01.
