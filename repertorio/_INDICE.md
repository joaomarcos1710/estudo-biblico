# Índice do Repertório

Repertório de textos, vídeos e comentários para consulta em emocionais (aconselhamentos, apoio pastoral, conversas de cuidado).

## Como está organizado

- `livros/` — um arquivo por livro bíblico. Dentro dele, organizado por capítulo, com os versículos-chave, vídeos e comentários.
- `temas/` — um arquivo por tema/emoção (ex: ansiedade, luto, medo, culpa). Cada entrada aponta de volta para a referência bíblica em `livros/`.
- `assuntos/` — um arquivo por assunto/entidade (ex: Deus, Jesus, Fé, Nínive). Mesma lógica dos temas, mas para pessoas, lugares e doutrinas em vez de emoções/situações.
- `visuais/` — links para diagramas visuais (árvores genealógicas, mapas, linhas do tempo) montados no Figma, referenciando os versículos/assuntos relacionados.
- `fontes/` — texto bíblico completo em JSON por tradução (hoje: NVI), comentários e outros materiais de origem. Veja [`fontes/README.md`](fontes/README.md).
- `fontes/_BIBLIOTECA.md` — **registro de todas as fontes** (traduções, comentários, autores, instituições, país de origem). Toda citação usada no repertório carrega um código daqui (`*Fonte: [CÓDIGO]*`), pra sempre dar pra rastrear de onde veio.
- `dados/` — versículos e entidades (personagens, lugares, eventos, temas) em JSON, interligados entre si. É a base que alimenta a página de busca.
- `design/guia-de-marca.md` — identidade visual pessoal (cores, tipografia, forma) usada em qualquer peça nova do repertório (páginas de busca, artifacts, exports).
- `design/sistema-visual.md` — **sistema visual do estudo bíblico** (v1.0), que estende o guia de marca com paleta semântica própria (vermelho = só Cristo/Messias, azul = divergências, terracota = contexto histórico, ocre = sacerdócio), regras de genealogia, ícones e separação visual entre texto bíblico/interpretação/aplicação. Usar sempre que criar um diagrama, genealogia, mapa ou peça visual nova.
- `genealogias/` — linhagens, famílias, tribos, linhagens reais e sacerdotais, com diagramas (SVG) e dados estruturados em `dados/genealogias.json`. Ver [`genealogias/README.md`](genealogias/README.md).

## Formato de cada entrada (em `livros/`)

Seis blocos fixos — a ideia é nunca deixar ambíguo o que é texto bíblico, o que é observação, o que é conclusão de uma fonte, e o que é nossa própria leitura:

```markdown
### Livro Capítulo:Versículo

**Texto bíblico**
> Texto do versículo
*Fonte: [NVI]*

**Tags:** #tema1 #assunto1

**Observação**
O que o texto diz literalmente — personagens, ação, palavras que se repetem, contraste. Sem interpretar ainda.

**O que dizem as fontes**
- Resumo do que cada comentário diz, atribuído por nome.
*Fonte: [CÓDIGO]*

**Nossa interpretação**
O que concluímos a partir do texto + fontes — deixando claro que é leitura nossa, não "o que a Bíblia diz" automaticamente.

**Aplicação pastoral**
Pra que situação/emocional isso serve, o que dizer, pra quem indicar.

**Vídeos**
- [Título do vídeo](link) — breve nota do que aborda

**Questões em aberto**
Pontos que ainda precisam de mais fonte, ou onde há divergência entre comentaristas — sem fingir consenso que não existe.
```

Nem toda entrada precisa preencher os seis blocos completos (um versículo simples pode não ter "questões em aberto"), mas a ordem e os títulos ficam padronizados.

## Formato de cada entrada (em `temas/` e `assuntos/`)

```markdown
## Nome do tema/assunto

- [Livro Capítulo:Versículo](../livros/livro.md#capítulo) — breve nota
```

## Livros já iniciados

- [Gênesis](livros/genesis.md) — Capítulos 1-2, 3, 4, 5, 6-8, 9-10, **11** (Torre de Babel + genealogia)

## Temas já iniciados

- [Ira](temas/ira.md)
- [Orgulho & Auto-suficiência](temas/orgulho.md) — *novo*

## Assuntos já iniciados

- [Graça](assuntos/graca.md)
- [Casamento](assuntos/casamento.md)
- [A Queda](assuntos/a-queda.md)
- [Torre de Babel](assuntos/torre-de-babel.md) — *novo*
- [Abrão / Abraão](assuntos/abraao.md) — *novo*
- [Genealogia](assuntos/genealogia.md) — *novo*

## Visuais já iniciados

*(atualizado conforme formos adicionando — árvores genealógicas, mapas, linhas do tempo no Figma)*

## Como adicionar

Me manda o texto (referência + versículo), e se tiver, vídeo, comentário, tema e/ou assunto. Eu:
1. Crio/atualizo o arquivo do livro em `livros/`
2. Crio/atualizo o(s) arquivo(s) de tema em `temas/` e de assunto em `assuntos/`, com link de volta
3. Se pedir um visual (árvore genealógica, mapa, linha do tempo), monto no Figma e registro o link em `visuais/`
4. Atualizo este índice
