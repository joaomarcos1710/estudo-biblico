# Índice do Repertório

Repertório de textos, vídeos e comentários para consulta em emocionais (aconselhamentos, apoio pastoral, conversas de cuidado).

## Como está organizado

- `livros/` — um arquivo por livro bíblico. Dentro dele, organizado por capítulo, com os versículos-chave, vídeos e comentários.
- `temas/` — um arquivo por tema/emoção (ex: ansiedade, luto, medo, culpa). Cada entrada aponta de volta para a referência bíblica em `livros/`.
- `assuntos/` — um arquivo por assunto/entidade (ex: Deus, Jesus, Fé, Nínive). Mesma lógica dos temas, mas para pessoas, lugares e doutrinas em vez de emoções/situações.
- `visuais/` — links para diagramas visuais (árvores genealógicas, mapas, linhas do tempo) montados no Figma, referenciando os versículos/assuntos relacionados.
- `fontes/` — texto bíblico completo em JSON por tradução (hoje: NVI), usado como fonte pra copiar os versículos certinhos ao criar entradas em `livros/`. Veja [`fontes/README.md`](fontes/README.md).

## Formato de cada entrada (em `livros/`)

```markdown
### [Livro Capítulo:Versículo](#)
> Texto do versículo (versão utilizada)

**Tags:** #tema1 #assunto1

**Vídeos:**
- [Título do vídeo](link) — breve nota do que aborda

**Comentários:**
- Observação pessoal, contexto de uso, para quem indicar, etc.
```

## Formato de cada entrada (em `temas/` e `assuntos/`)

```markdown
## Nome do tema/assunto

- [Livro Capítulo:Versículo](../livros/livro.md#capítulo) — breve nota
```

## Livros já iniciados

*(atualizado conforme formos adicionando)*

## Temas já iniciados

*(atualizado conforme formos adicionando)*

## Assuntos já iniciados

*(atualizado conforme formos adicionando)*

## Visuais já iniciados

*(atualizado conforme formos adicionando — árvores genealógicas, mapas, linhas do tempo no Figma)*

## Como adicionar

Me manda o texto (referência + versículo), e se tiver, vídeo, comentário, tema e/ou assunto. Eu:
1. Crio/atualizo o arquivo do livro em `livros/`
2. Crio/atualizo o(s) arquivo(s) de tema em `temas/` e de assunto em `assuntos/`, com link de volta
3. Se pedir um visual (árvore genealógica, mapa, linha do tempo), monto no Figma e registro o link em `visuais/`
4. Atualizo este índice
