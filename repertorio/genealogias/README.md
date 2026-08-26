# Genealogias

Repertório de genealogias bíblicas — linhagens, famílias, tribos, linhagens reais e sacerdotais — com dados estruturados e diagramas visuais (SVG).

## Como funciona

- Cada genealogia é uma pasta aqui, com um `README.md` (a ficha completa) e os diagramas (`.svg`/`.png`).
- Os **dados estruturados** (a mesma informação, em formato que a busca/app consegue cruzar) ficam em [`../dados/genealogias.json`](../dados/genealogias.json).
- As **relações de parentesco** (pai, mãe, filhos, cônjuges, irmãos) ficam nas próprias pessoas em [`../dados/entidades.json`](../dados/entidades.json) — uma genealogia aqui é um "recorte" nomeado e visual dessas relações, não uma fonte de dados paralela. Isso evita ter duas versões da mesma informação.

## Regra de ouro: texto x reconstrução

Toda ficha separa duas coisas:
- **O que o texto diz** — só o que está explícito na Bíblia, com referência.
- **Reconstrução / lacunas** — inferência, tradição extrabíblica, ou leitura acadêmica, sempre identificada como tal. Onde há buraco (ex: nome de esposa não citado), registramos "não informado pela Bíblia" — não inventamos.

## Formato da ficha (`README.md` de cada genealogia)

```markdown
# Nome da genealogia

**Tipo:** linhagem | família | tribos | linhagem-real | linhagem-sacerdotal | genealogia-de-jesus
**Status:** rascunho | completo

## O que o texto diz
- Personagem principal:
- Origem da linhagem:
- Destino da linhagem:
- Passagens bíblicas: Livro Capítulo:Versículos
- Pessoas relacionadas: (ids de `entidades.json`)
- Tribos / Reis / Sacerdotes relacionados:
- Eventos importantes:

## Reconstrução / lacunas
- (o que não está explícito no texto, e de onde vem a inferência, se houver)

## Observações

## Fontes
*Fonte: [CÓDIGO]* — ver `../fontes/_BIBLIOTECA.md`

## Imagens disponíveis
- `diagrama.svg`
```

## Genealogias no repertório

| Genealogia | Tipo | Status |
|---|---|---|
| [Linhagem de Adão a Noé](linhagem-adao-noe/README.md) | linhagem | rascunho |
| [Família de Abraão](familia-abraao/README.md) | família | rascunho |
| [As 12 Tribos de Jacó](tribos-de-jaco/README.md) | tribos | rascunho |
| [Linhagem Real de Davi](linhagem-real-de-davi/README.md) | linhagem-real | rascunho |
| [Linhagem Sacerdotal de Arão](linhagem-sacerdotal-de-arao/README.md) | linhagem-sacerdotal | rascunho |
| [Genealogia de Jesus (Mateus x Lucas)](genealogia-de-jesus/README.md) | genealogia-de-jesus | rascunho |

`rascunho` = estrutura criada, aguardando conteúdo (texto do capítulo genealógico correspondente ainda não recebido/processado).

## Sobre imagens externas de referência

Se usarmos alguma imagem de terceiros como referência visual (não pra copiar pro repositório, só pra registrar onde vimos algo), ela entra num `fontes-visuais.md` dentro da pasta da genealogia, com: título, autor, fonte, URL, data de acesso, licença/direitos, o que representa, e observações. Nunca copiamos imagem protegida pro repositório — só a referência e o link.
