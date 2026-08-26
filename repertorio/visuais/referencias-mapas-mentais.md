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

---

# Referências — árvore genealógica

Duas imagens de exemplo recebidas mostrando árvores genealógicas de Gênesis (caixas com nomes, ligadas por linhas hierárquicas pai/mãe → filhos).

## O que os exemplos mostram (estrutura a reaproveitar)

- **Caixas de nome** ligadas por linhas retas indicando geração (pai/mãe no topo, filhos abaixo).
- Casais lado a lado (ex: Abrão + Sarai, Isaque + Rebeca) antes de descer pros filhos.
- Uniões secundárias/concubinas marcadas de forma diferenciada (ex: Agar como serva de Sara, ligada a Ismael).
- Anotações curtas ao lado de nomes-chave (ex: "pai dos árabes", "renomeado Israel", "morta por Caim").
- Blocos separados no canto pra eventos não-genealógicos que se cruzam com a árvore (Criação, Dilúvio, Torre de Babel), ligados por setas ao ponto da linhagem onde acontecem.
- Uma das referências é bem "rabiscada"/hand-drawn (estilo sketchnote); a outra mais limpa, com caixas retangulares e cor de destaque (amarelo) pros nomes centrais da linhagem escolhida (Adán, Abram, Isaac, Jacob).

## Adaptação pra nossa marca

- Caixas com cantos retos, borda fina preta, texto em Hanken Grotesk.
- Nome da pessoa central da linhagem (Abraão, Isaque, Jacó) destacado com o vermelho `#E5341E` no lugar do amarelo dos exemplos — mesmo princípio de "trilha principal" iluminada.
- Linhas de conexão retas, sem efeito rabiscado, no preto/cinza (`--rule`).
- Título do livro (GÊNESIS) em League Gothic, como nos exemplos, mas sem o traço decorativo à mão.
- Eventos cruzados (Criação, Dilúvio, Babel) como blocos à parte, ligados por linha reta ou seta fina — não ilustração fofa, ícone de linha ou nenhuma imagem.

## Fonte de dados

Mesma base: os relacionamentos de parentesco devem primeiro existir em [`../dados/entidades.json`](../dados/entidades.json) (campo de relação familiar) antes de virar árvore no Figma — a árvore é a visualização, não o dado original.

---

# Referência — BibleForge (leitor bíblico)

[bibleforge/BibleForge](https://github.com/bibleforge/BibleForge) — app de estudo bíblico open source (MIT), código de 2008, último commit 2022. Não vale portar o código (JS puro sem framework, servidor Node/DB próprio que não precisamos — nosso leitor é estático a partir de `dados/*.json`).

**Ideia a guardar pro futuro:** o diferencial do BibleForge é análise interlinear — clicar numa palavra do versículo e ver o termo original em hebraico/grego. Não é prioridade agora, mas é um recurso possível pro Leitor Bíblico (protótipo em Artifact) quando o conteúdo estiver mais maduro.

---

# Referência — OpenBible (danzuep)

[danzuep/OpenBible](https://github.com/danzuep/OpenBible) — app de estudo bíblico multiplataforma sério e ativo (C#/.NET MAUI + Blazor), com parsing de formatos bíblicos padrão (USX/USJ) e romanização de idiomas (japonês, cantonês etc.).

**Não adotar a stack** — é .NET, ecossistema diferente do nosso (HTML/JS estático + JSON). Mudar pra isso significaria abandonar a arquitetura atual por um projeto de programação C# de verdade. Fica só como referência de modelo de dados (`BibleVerse`, `BibleWord`, `BibleReference`, `BibleFootnote`) — já coberto, pro nosso propósito, por `dados/versiculos.json`.

---

# Referência — SharpSword

[sktzofrenic/sharpsword](https://github.com/sktzofrenic/sharpsword) — app bíblico Go (backend) + Vue + Tailwind (PWA mobile-first), foco em performance de busca (resultado a cada tecla digitada) e navegação por teclado entre livro/capítulo/versículo.

**Não adotar a stack** (Go/Vue é outro ecossistema). **Ideia de UX a aproveitar:** busca com resultado instantâneo (a cada tecla), sem precisar apertar enter — já é parcialmente o que a página de busca (Artifact) faz, vale reforçar isso no Leitor Bíblico também quando tiver mais conteúdo pra buscar.
