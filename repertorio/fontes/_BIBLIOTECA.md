# Biblioteca de Fontes

Todo material que entra no repertório (comentário, verbete, vídeo, artigo) recebe um **código de fonte** aqui, e esse código acompanha o trecho onde for usado (formato `*Fonte: [CÓDIGO]*`).

## Como funciona

1. Nova fonte chega → cadastro aqui com código, tipo, autor/instituição, país/idioma de origem e link (se houver).
2. Todo trecho extraído dela, em qualquer arquivo do repertório, leva `*Fonte: [CÓDIGO]*` logo abaixo.
3. Códigos são curtos e estáveis (ex: `MOODY`, `NVI`, `SCOFIELD`, `TIME-BÍBLIA`) — não mudam depois de criados.

## Fontes cadastradas

| Código | Tipo | Título / Obra | Autor / Instituição | Origem | Link |
|---|---|---|---|---|---|
| `NVI` | Tradução bíblica | Nova Versão Internacional | Biblica | Brasil/EUA (trad. português) | — |
| `MOODY` | Comentário bíblico | Comentário Bíblico Moody | Moody Bible Institute of Chicago | EUA (trad. português) | — |

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
