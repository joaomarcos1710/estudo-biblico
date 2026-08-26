# Dados estruturados

Esta pasta é a camada de dados por trás da busca e das interligações — o que os arquivos `.md` em `livros/`, `temas/` e `assuntos/` são para leitura humana, estes `.json` são para o app/busca poder cruzar informação.

## Arquivos

- **`entidades.json`** — todo personagem, lugar, evento ou tema recorrente vira uma entidade com identidade própria (id, nome, apelidos/nomes alternativos, resumo, quais versículos fala dela, e com quais outras entidades se relaciona). É isso que permite navegar de "Nínive" pra "Jonas" pra "arrependimento" sem precisar ir e voltar em arquivos soltos.
- **`versiculos.json`** — cada versículo-chave cadastrado, com texto, fonte da tradução, tags, comentários (com fonte) e a lista de entidades que aparecem nele. Campos que espelham os 6 blocos do formato em `livros/` (ver `_INDICE.md`): `observacao`, `comentarios` ("o que dizem as fontes"), `interpretacao` ("nossa interpretação" — sempre marcada como leitura nossa, não como texto bíblico), `aplicacaoPastoral`, `videos`, `referenciasCruzadas`, `questoesEmAberto`. Nem todo campo precisa estar preenchido em toda entrada.

### Campo `nivelConfianca`

Cada objeto dentro de `comentarios` pode ter `"nivelConfianca": "alto" | "medio" | "baixo"`:

- **alto** — leitura bem estabelecida, pouco controversa (ex: significado lexical de uma palavra hebraica/grega).
- **medio** — interpretação razoável mas debatida entre tradições/comentaristas (ex: se "dia" em Gênesis 1 é literal de 24h ou não).
- **baixo** — especulativo, uma leitura entre várias possíveis, ou ainda não conferido contra outras fontes.

Serve pra não apresentar tudo com o mesmo peso de certeza — uma leitura polêmica não deve soar tão definitiva quanto um fato lexical simples.

## Regra de ouro

**Todo `id` é permanente.** Uma vez criado (ex: `"deus"`, `"gen-1-1"`, `"ninive"`), não muda nunca — é o que garante que os links entre arquivos não quebrem conforme o repertório cresce.

## Convenção de IDs

- Entidades: nome em minúsculo, sem acento, com hífen (`espirito-santo`, `joao-batista`, `mar-vermelho`).
- Versículos: `<livro>-<capítulo>-<versículo(s)>` (ex: `gen-1-26-28`, `jon-2-1`).

## Tipos de entidade

`pessoa` (bíblica, ex: Jonas), `pessoa-divina` (Deus, Jesus, Espírito Santo), `lugar` (ex: Nínive), `evento` (ex: A Criação, O Dilúvio), `tema` (ex: Fé, Arrependimento — mais abstrato, se sobrepõe com `temas/` e `assuntos/` em Markdown).

## Como isso se relaciona com os arquivos `.md`

Os `.md` em `livros/`, `temas/` e `assuntos/` continuam existindo — são a forma de leitura corrida, fácil de abrir e ler no GitHub. Os `.json` aqui são a mesma informação em formato que a página de busca ([artifact](../../README.md)) consegue carregar e cruzar automaticamente. Ao adicionar um versículo novo, ele entra nos dois lugares.
