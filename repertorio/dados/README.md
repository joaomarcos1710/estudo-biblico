# Dados estruturados

Esta pasta é a camada de dados por trás da busca e das interligações — o que os arquivos `.md` em `livros/`, `temas/` e `assuntos/` são para leitura humana, estes `.json` são para o app/busca poder cruzar informação.

## Arquivos

- **`entidades.json`** — todo personagem, lugar, evento ou tema recorrente vira uma entidade com identidade própria (id, nome, apelidos/nomes alternativos, resumo, quais versículos fala dela, e com quais outras entidades se relaciona). É isso que permite navegar de "Nínive" pra "Jonas" pra "arrependimento" sem precisar ir e voltar em arquivos soltos.
- **`versiculos.json`** — cada versículo-chave cadastrado, com texto, fonte da tradução, tags, comentários (com fonte) e a lista de entidades que aparecem nele.

## Regra de ouro

**Todo `id` é permanente.** Uma vez criado (ex: `"deus"`, `"gen-1-1"`, `"ninive"`), não muda nunca — é o que garante que os links entre arquivos não quebrem conforme o repertório cresce.

## Convenção de IDs

- Entidades: nome em minúsculo, sem acento, com hífen (`espirito-santo`, `joao-batista`, `mar-vermelho`).
- Versículos: `<livro>-<capítulo>-<versículo(s)>` (ex: `gen-1-26-28`, `jon-2-1`).

## Tipos de entidade

`pessoa` (bíblica, ex: Jonas), `pessoa-divina` (Deus, Jesus, Espírito Santo), `lugar` (ex: Nínive), `evento` (ex: A Criação, O Dilúvio), `tema` (ex: Fé, Arrependimento — mais abstrato, se sobrepõe com `temas/` e `assuntos/` em Markdown).

## Como isso se relaciona com os arquivos `.md`

Os `.md` em `livros/`, `temas/` e `assuntos/` continuam existindo — são a forma de leitura corrida, fácil de abrir e ler no GitHub. Os `.json` aqui são a mesma informação em formato que a página de busca ([artifact](../../README.md)) consegue carregar e cruzar automaticamente. Ao adicionar um versículo novo, ele entra nos dois lugares.
