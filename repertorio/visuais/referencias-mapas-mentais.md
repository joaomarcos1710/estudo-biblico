# Referências visuais — mapas mentais de livros

Estilo de referência pra quando formos montar os mapas mentais/árvores de cada livro no Figma. Duas imagens de exemplo recebidas (mapas mentais de Gênesis, estilo infográfico/educacional) — não são a identidade final, servem só de referência de **estrutura de conteúdo**, adaptada à [marca preto/branco/vermelho](../design/guia-de-marca.md).

## O que os exemplos mostram (estrutura a reaproveitar)

- **Título do livro** em destaque, no topo.
- **Quando foi escrito** e **quem escreveu** (autoria/data).
- **Personagens principais** (lista).
- **Temas centrais** (lista curta).
- **Linha do que acontece no livro** (bullets em ordem, com referência de capítulo).
- **Versículos-chave** (lista de referências rápidas).
- **O que o livro ensina hoje** (aplicação).
- **Um versículo de destaque** citado por completo no rodapé.

## Adaptação pra nossa marca

- Sem ilustrações de banco de imagens / clip-art infantil — se usar imagem, só foto real ou ícone de linha (Lucide), nunca desenho fofo.
- Título do livro em **League Gothic**, caixa alta.
- Resto do texto em **Hanken Grotesk**.
- Paleta preto/branco/off-white + vermelho `#E5341E` como único acento (nada de verde, laranja, azul como nos exemplos recebidos).
- Cantos retos, sem sombra pesada, linhas finas em vez de setas curvas ilustradas.

## Fonte de dados

O conteúdo (personagens, versículos-chave, eventos) já está sendo estruturado em [`../dados/entidades.json`](../dados/entidades.json) e [`../dados/versiculos.json`](../dados/versiculos.json) — o mapa mental do Figma deve puxar dali, não ser preenchido do zero.

## Status

Ainda não montado no Figma. Próximo passo: gerar o mapa mental de Gênesis nessa estrutura, com a marca, quando o conteúdo do livro estiver mais completo em `dados/`.
