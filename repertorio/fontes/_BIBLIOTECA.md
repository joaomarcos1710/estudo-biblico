# Biblioteca de Fontes

Todo material que entra no repertório (comentário, verbete, vídeo, artigo) recebe um **código de fonte** aqui, e esse código acompanha o trecho onde for usado (formato `*Fonte: [CÓDIGO]*`). As referências seguem a norma **ABNT NBR 6023:2025** (Informação e documentação — Referências — Elaboração).

## Como funciona

1. Nova fonte chega → cadastro aqui com código, tipo, autor/instituição, país/idioma de origem, **referência ABNT completa** e link (se houver).
2. Todo trecho extraído dela, em qualquer arquivo do repertório, leva `*Fonte: [CÓDIGO]*` logo abaixo.
3. Códigos são curtos e estáveis (ex: `MOODY`, `NVI`, `SCOFIELD`, `TIME-BÍBLIA`) — não mudam depois de criados.
4. **Fonte em outro idioma → sempre traduzida pro português** no conteúdo salvo no repertório. A referência ABNT registra o idioma/edição original pra rastreabilidade, mas o texto usado em `livros/`, `temas/`, `assuntos/` e nos resumos de `fontes/comentarios/` é sempre em português.
5. **Dado bibliográfico que não temos → não inventar.** A ABNT tem convenção própria pra isso: `[S. l.]` (sem local), `[s. n.]` (sem editora), `[19--?]` (data aproximada/desconhecida). Usamos esses colchetes em vez de chutar editora, cidade ou ano.

## Fontes cadastradas

| Código | Tipo | Origem | Referência ABNT (NBR 6023:2025) |
|---|---|---|---|
| `NVI` | Tradução bíblica | Brasil/EUA (compilação, trad. português) | BÍBLIA. Português. Nova Versão Internacional. In: AMARAL, Daniel. *biblias*: coletânea de traduções bíblicas em formato aberto. [S. l.]: GitHub, 2022-2026. Disponível em: https://github.com/damarals/biblias. Acesso em: 25 ago. 2026. |
| `MOODY` | Comentário bíblico | EUA (trad. português) | MOODY BIBLE INSTITUTE OF CHICAGO. *Gênesis*: comentário bíblico Moody. [S. l.: s. n.], [19--?]. |
| `KIDNER` | Comentário bíblico | Inglaterra (trad. Edições Vida Nova, Brasil) | KIDNER, Derek. *Gênesis*: introdução e comentário. Tradução: Odayr Olivetti. São Paulo: Vida Nova, [1979 ou post.]. Título original: Genesis: An Introduction and Commentary. (Tyndale Old Testament Commentaries). |
| `GRACA-SOBERANA` | Coletânea de sermões | Holanda/Inglaterra/EUA (trad. português) | HARINCK, C.; SPURGEON, C. H.; EDWARDS, J.; WHITEFIELD, G. *Graça soberana*. Compilado por W. Chr. Hammink. [S. l.]: Dutch Reformed Tract Society, [20--?]. |
| `GARRETT` | Comentário bíblico (verse-by-verse) | EUA (original em inglês) | GARRETT, Charlie. *Genesis*: a verse-by-verse study. [S. l.: s. n.], 2021. |
| `BEACON` | Comentário bíblico (coleção) | EUA (trad. CPAD, Brasil) | COMENTÁRIO BÍBLICO BEACON: Gênesis. Tradução: Luís Aron de Macedo. 4. impr. Rio de Janeiro: CPAD, 2012. ISBN 85-263-0685-5. Título original: Beacon Bible Commentary (10 Volume Set). Kansas City: Beacon Hill Press of Kansas City / Nazarene Publishing House, 1969. |

*Campos entre colchetes (`[S. l.]`, `[s. n.]`, `[19--?]`) indicam dado que a fonte recebida não informou — não foi inventado. Se você tiver a edição/ano exatos de algum desses materiais, me manda que eu atualizo a referência.*

## Como montar a referência ABNT de um tipo novo de fonte

### Livro / comentário impresso (monografia no todo)
```
AUTOR. Título: subtítulo. Edição. Local: Editora, ano.
```

### Capítulo/parte de um livro (com autor próprio)
```
AUTOR. Título da parte. In: AUTOR DA OBRA. Título da obra. Local: Editora, ano. p. inicial-final.
```

### Vídeo do YouTube (documento audiovisual em meio eletrônico)
```
AUTOR ou TÍTULO EM CAIXA ALTA (se autoria não individual). Título. [S. l.: s. n.], ano. 1 vídeo (duração min). Publicado pelo canal [nome do canal]. Disponível em: [link]. Acesso em: [data].
```

### PDF / e-book consultado online
```
AUTOR. Título: subtítulo. Local: Editora, ano. E-book. Disponível em: [link]. Acesso em: [data].
```

### Site / página de internet
```
TÍTULO DA PÁGINA. Local: Instituição responsável, ano. Disponível em: [link]. Acesso em: [data].
```

Sempre que eu cadastrar uma fonte nova, preencho o modelo certo acima e adiciono a linha na tabela — sem precisar você pedir.

## Formato de citação nos arquivos

```markdown
> Trecho ou citação aqui.

*Fonte: [MOODY]*
```

Para um versículo (a tradução já é a fonte do texto):

```markdown
### Gênesis 1:1
> No princípio, Deus criou os céus e a terra.
*Fonte: [NVI]*
```
