# Sistema Visual do Estudo Bíblico

## Versão 1.0

> Sistema visual para organizar, estudar e representar o conhecimento bíblico de forma clara, consistente, rastreável e visualmente reconhecível.

Deriva da identidade visual pessoal ([`guia-de-marca.md`](guia-de-marca.md)), mas tem linguagem própria pra representar conhecimento bíblico — a marca pessoal representa João Marcos; este sistema representa conhecimento bíblico organizado.

---

## Propósito

Estabelece as regras de representação visual do `estudo-biblico`: textos, estudos, comentários, personagens, genealogias, famílias, tribos, reis, sacerdotes, lugares, mapas, cronologias, temas teológicos, referências cruzadas, divergências, aplicações pastorais, fontes.

**Princípio central:** a estética deve servir à compreensão do texto. A decoração nunca compete com o conteúdo.

## Princípios fundamentais

1. **Clareza antes da estética** — se uma escolha visual deixa o material mais bonito mas menos compreensível, é rejeitada.
2. **Cor deve ter significado** — nunca decorativa.
3. **Uma cor, um significado** — vermelho é *exclusivamente* Cristo/Messias/elementos diretamente relacionados a Jesus. Nunca usar vermelho para divergência, alerta ou erro interpretativo.
4. **A Bíblia não se confunde com a interpretação** — visualmente distinguíveis: texto bíblico, observação, interpretação, comentário, síntese, aplicação, reconstrução, divergência.
5. **Fontes rastreáveis** — toda informação externa é identificável.
6. **Incerteza visível** — divergência acadêmica/interpretativa aparece claramente, nunca escondida atrás de uma leitura só.
7. **Menos é mais** — sem gradientes, sombras pesadas, 3D, ícones em excesso, estética religiosa genérica.

## Paleta principal (herdada da marca pessoal)

| Nome | Hex | Função |
|---|---|---|
| Ink | `#0E0E0E` | Texto principal, títulos, linhas |
| Paper | `#FFFFFF` | Fundo principal |
| Off-white | `#F5F4F2` | Áreas secundárias |
| Hairline | `#E4E4E2` | Bordas e divisórias |
| Muted | `#6B6B68` | Texto secundário |
| João Red | `#E5341E` | Cristo, Messias e destaque da identidade |

A maior parte do sistema permanece em preto, branco e off-white.

## Paleta semântica (própria do conteúdo bíblico)

| Categoria | Cor | Hex |
|---|---|---|
| **Cristo / Messias** | Vermelho | `#E5341E` |
| **Divergência / debate** | Azul profundo | `#315A72` |
| **Contexto histórico / arqueologia** | Terracota | `#8A5A44` |
| **Mapas / água** | Azul claro | `#DCE7EA` |
| **Sacerdócio / linhagem sacerdotal** | Ocre | `#A67C32` |

**Regra de exclusividade semântica:** uma cor não representa duas categorias. Vermelho nunca é divergência; azul profundo nunca é Jesus; ocre nunca é mapa; terracota nunca é interpretação; azul claro nunca é debate teológico. Sem necessidade semântica, usa-se preto/branco/off-white.

### Vermelho: Cristo e Messias

Representa Jesus, Cristo, Messias, palavras diretas de Jesus, linhagem messiânica, profecias messiânicas, eventos da obra de Cristo. Pode destacar falas diretas de Jesus em citação (a referência permanece em preto/muted). **Não** representa importância genérica, erro, alerta ou divergência.

### Azul profundo: divergência e debate

Reservado para interpretações alternativas, questões acadêmicas debatidas, hipóteses concorrentes. Formato de bloco de divergência:

```
DIVERGÊNCIA INTERPRETATIVA
INTERPRETAÇÃO A / INTERPRETAÇÃO B
PONTO DE CONSENSO / PONTO DE DIVERGÊNCIA
```

### Terracota: contexto histórico

História, arqueologia, cultura, costumes, contexto político/social/econômico — mapas históricos, linhas do tempo, fichas de contexto.

### Azul claro: mapas e água

Rios, mares, lagos, elementos aquáticos em mapas. Discreto, nunca usado pra interpretação/divergência.

### Ocre: sacerdócio

Sacerdotes, levitas em função sacerdotal, Arão, linhagens sacerdotais. Em genealogias: linha ocre = linhagem sacerdotal.

## Tipografia

- **League Gothic** — títulos, capítulos, nomes de livros/personagens, títulos de genealogias, cronologias, números grandes. Caixa alta, condensada.
- **Hanken Grotesk** — corpo, subtítulos, legendas, referências, tabelas, notas, fontes, metadados. Pesos: 400 corpo, 500 secundário, 600 destaque, 700 subtítulo, 800 destaque forte.
- Nunca uma terceira família tipográfica.

## Separação texto × interpretação (visual)

- **Texto bíblico** — tratamento neutro: referência (League Gothic ou Hanken bold) → texto → tradução (muted). Prioridade: legibilidade > referência > tradução > destaque semântico.
- **Observação** ("o que o texto apresenta?") — fundo branco, texto preto, sem cor semântica obrigatória.
- **Interpretação** ("o que o texto significa?") — fundo off-white. Nunca parece uma citação bíblica.
- **Comentário** — sempre com fonte identificada (`Fonte: Autor, Obra, capítulo/página`), priorizando síntese própria.
- **Síntese** — reúne texto+contexto+interpretação+comentários+referências; deixa claro que é conclusão do estudo, não texto bíblico.
- **Aplicação** ("o que significa pra vida cristã?") — fundo off-white, vermelho só se houver relação direta com Cristo. Nunca apresentada como o significado original do texto.
- **Divergência** — sempre em azul profundo, nunca vermelho.

### Níveis de evidência (textual, não colorido)

Texto explícito / Inferência / Reconstrução / Interpretação / Debate — classificados por rótulo em texto, **não** por cores diferentes (isso já é o que fazemos com `nivelConfianca` em `dados/versiculos.json` e os blocos "Nossa interpretação" / "Questões em aberto" em `livros/`).

## Genealogias

Priorizar clareza, gerações, relações, referências, distinção entre explícito e reconstrução. Evitar árvores ornamentadas.

**Cores:**
- Linhagem messiânica confirmada → vermelho `#E5341E`
- Linhagem principal (geral, não necessariamente messiânica) → preto `#0E0E0E`
- Relações secundárias → muted `#6B6B68`
- Linhagem sacerdotal → ocre `#A67C32`

**Linhas:**
- Contínua → relação explicitamente bíblica
- Pontilhada → reconstrução/inferência
- Seta → quando a direção importa; sem seta quando bidirecional

**Genealogia de Jesus:** Mateus 1 e Lucas 3 são representadas **separadamente**, nunca fundidas automaticamente — com uma seção de comparação à parte, e as diferenças tratadas com o bloco de divergência (azul), não resolvidas silenciosamente.

## Ícones

**Lucide** para conceitos bíblicos (traço simples e consistente). **Simple Icons** só para plataformas/serviços externos — nunca pra conceitos bíblicos.

| Conceito | Ícone |
|---|---|
| Texto bíblico | BookOpen |
| Referência | BookMarked |
| Genealogia | GitBranch |
| Pessoa | User |
| Família | Users |
| Lugar | MapPin |
| Mapa | Map |
| Cronologia | Clock |
| Referência cruzada | Link |
| Comentário | MessageCircle |
| Observação | Eye |
| Interpretação | Search |
| Aplicação | Heart |
| Fonte | Library |
| Divergência | AlertTriangle |
| Informação | Info |

Ícones são auxiliares — nunca substituem títulos importantes.

## Cards e componentes

Radius 2-10px, borda `#E4E4E2`, sombra mínima/inexistente, fundo branco ou off-white, espaçamento generoso. Sem glassmorphism, gradiente, 3D, arredondamento excessivo.

## Direitos autorais e imagens

Priorizar síntese própria, referências (formato ABNT — ver [`../fontes/_BIBLIOTECA.md`](../fontes/_BIBLIOTECA.md)), citações breves. Nunca reproduzir trechos extensos de traduções/comentários protegidos. Imagem externa com restrição de uso → guardar só a referência, nunca copiar pro repositório. Reconstrução artística de personagem bíblico sempre rotulada como "RECONSTRUÇÃO ARTÍSTICA", nunca como retrato histórico.

Fonte produzida por IA nunca é tratada como fonte primária — é ferramenta de análise; sempre que possível, registra-se a fonte original por trás.

## Repertório genealógico visual

```
genealogias/
└── nome-da-genealogia/
    ├── README.md
    ├── genealogia.svg   (formato preferencial)
    ├── genealogia.png   (pré-visualização, opcional)
    └── fontes-visuais.md (imagens externas de referência, se houver)
```

## Checklist antes de publicar qualquer material visual

- [ ] Hierarquia clara?
- [ ] Informação bíblica separada da interpretação?
- [ ] Fontes identificadas?
- [ ] Cada cor usada tem significado, e só o seu?
- [ ] Vermelho reservado a Cristo/Messias?
- [ ] Divergências em azul, não vermelho?
- [ ] Tipografia correta (League Gothic + Hanken Grotesk só)?
- [ ] Sem excesso decorativo?
- [ ] Reconstruções e divergências identificadas como tal?
- [ ] Datas aproximadas marcadas como aproximadas?
- [ ] Imagens externas com fonte/licença verificadas?
- [ ] Legível em tela pequena?

## Regra de ouro

> Visualizar não é inventar. Toda representação respeita a diferença entre o que a Bíblia afirma, o que podemos inferir, o que os estudiosos interpretam, o que reconstruímos, e o que aplicamos.
