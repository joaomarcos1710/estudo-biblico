# Design de Interface — Estudo Bíblico Repertório

## 1. Visão geral

Interface web/mobile que permite buscar, visualizar e explorar o repertório bíblico:
- **Busca** por versículo, tema, assunto, pessoa, lugar, acontecimento
- **Visualização** de verso com contexto, comentários, tags, aplicação pastoral
- **Navegação** entre temas, assuntos, genealogias, mapas
- **Referências cruzadas** entre textos e entidades

Toda interface herda do [`sistema-visual.md`](sistema-visual.md).

---

## 2. Estrutura da página

### 2.1 Header
```
[Logo] Estudo Bíblico     [Search Bar________________]  [Favorites]  [Settings]
```
- Logo: João Red (`#E5341E`) + marca pessoal
- Search bar: placeholder "Versículo, tema, pessoa, lugar..."
- Sem navegação por abas — busca é o foco principal

### 2.2 Busca (landing page)

**Layout:** uma coluna, campo grande de busca, abaixo sugestões de categorias.

```
┌─────────────────────────────────────────────┐
│  Estudo Bíblico Repertório                  │
│                                             │
│  [____ Busque um verso, tema, assunto ____] │
│                                             │
│  Sugestões de busca:                        │
│  • Gênesis 12:1-9 (verso)                   │
│  • Chamado & Obediência (tema)              │
│  • Torre de Babel (assunto)                 │
│  • Abraão (pessoa)                          │
│  • Canaã (lugar)                            │
└─────────────────────────────────────────────┘
```

**Categorias visuais:** cada categoria com ícone pequeno (Lucide) + label em Hanken 500.

### 2.3 Resultado de busca

Quando o usuário digita, a página exibe resultados em **tempo real**:

```
┌────────────────────────────────────────────────────┐
│  Versículos (3)                                    │
│  • Gênesis 12:1-9 — Chamada de Abraão             │
│  • Gênesis 11:1-9 — Torre de Babel                │
│  • Gênesis 11:27-32 — Genealogia de Terá          │
│                                                    │
│  Temas (2)                                         │
│  • Chamado & Obediência                            │
│  • Orgulho & Auto-suficiência                      │
│                                                    │
│  Pessoas (4)                                       │
│  • Abraão                                          │
│  • Sarai / Sara                                    │
│  • Terá                                            │
│  • Ló                                              │
│                                                    │
│  Lugares (2)                                       │
│  • Ur dos Caldeus                                  │
│  • Harã                                            │
└────────────────────────────────────────────────────┘
```

**Espaçamento:** generoso entre categorias, altura do texto normal. Sem cards — simples lista com bordas finas.

---

## 3. Página de verso

### Layout principal: 3 colunas

```
┌───────────────────────────────────────────────────────────────┐
│ Gênesis 12:1-9 — A Chamada de Abraão                       ❤️ │
└───────────────────────────────────────────────────────────────┘

┌──────────────────────┬────────────────────────┬────────────────┐
│ METADATA             │ CONTEÚDO (PRINCIPAL)   │ REFERÊNCIAS    │
│ (sidebar esq)        │                        │ (sidebar dir)  │
│                      │                        │                │
│ Livro: Gênesis       │ **Texto bíblico**      │ **Temas**      │
│ Capítulo: 12         │ > Ora disse o SENHOR.. │ • Chamado      │
│ Versículos: 1-9      │ *Fonte: [NVI]*         │ • Fé           │
│                      │                        │ • Obediência   │
│ **Leitura estimada** │                        │                │
│ 3 minutos            │ **Observação**         │ **Assuntos**   │
│                      │ O texto apresenta...   │ • Abraão       │
│                      │                        │ • Promessa     │
│                      │ **O que dizem as       │   Abraâmica    │
│                      │ fontes**               │ • Canaã        │
│                      │ - Moody: ...           │                │
│                      │ - Beacon: ...          │ **Vídeos**     │
│                      │                        │ • [Título]     │
│                      │ **Nossa interpretação**│   (link)       │
│                      │ 1. Fé sem promessa...  │                │
│                      │                        │ **Genealogia** │
│                      │ **Aplicação pastoral** │ • Terá         │
│                      │ - Para quem ouve...    │ • Abrão        │
│                      │                        │ • Isaque       │
│                      │ **Questões em aberto** │                │
│                      │ - Cronologia do...     │ **Relacionado**│
│                      │                        │ • Gen. 11:1-9  │
│                      │                        │ • Gen. 11:27.. │
│                      │                        │ • Gen. 13:1-9  │
└──────────────────────┴────────────────────────┴────────────────┘
```

### 3.1 Componente "Texto bíblico"

```
┌──────────────────────────────────────────────┐
│ **Texto bíblico**                            │
│                                              │
│ > Ora disse o SENHOR a Abrão: "Sai da tua  │
│   terra, da tua parentela e da casa de teu  │
│   pai, para a terra que te mostrarei...     │
│ *Fonte: [NVI]*                              │
│                                              │
│ **Tradução alternativa (opcional)**          │
│ ◄ Mostrar outras traduções                  │
└──────────────────────────────────────────────┘
```

**Estilo:**
- Fundo branco, borda hairline `#E4E4E2`
- Citação em preto `#0E0E0E`, itálico
- Fonte: Hanken 400, line-height 1.6
- Fonte em muted `#6B6B68`, tamanho menor

### 3.2 Componente "Observação"

```
┌──────────────────────────────────────────────┐
│ **Observação**                               │
│                                              │
│ O texto apresenta seis movimentos distintos: │
│ 1. Chamado verbal (v.1-3)...                │
│ 2. Desprendimento material...               │
│                                              │
└──────────────────────────────────────────────┘
```

**Estilo:**
- Fundo branco
- Sem cor semântica obrigatória
- Títulos em Hanken 600

### 3.3 Componente "O que dizem as fontes"

```
┌──────────────────────────────────────────────┐
│ **O que dizem as fontes**                    │
│                                              │
│ - Moody (alt): Tripla renúncia como        │
│   teste de fé...                            │
│   [Nível confiança: ⭐⭐⭐]                   │
│                                              │
│ - Beacon (alt): A promessa abraâmica        │
│   abrange Cristo...                         │
│   [Nível confiança: ⭐⭐⭐]                   │
│                                              │
│ *Fonte: [MOODY]*, *Fonte: [BEACON]*         │
│                                              │
└──────────────────────────────────────────────┘
```

**Estilo:**
- Borda hairline, fundo branco
- Nível de confiança como ⭐ (stars) — 1 baixo, 2 médio, 3 alto
- Fonte sempre identificada em muted

### 3.4 Componente "Nossa interpretação"

```
┌──────────────────────────────────────────────┐
│ **Nossa interpretação**                      │
│                                              │
│ (fundo off-white #F5F4F2)                   │
│                                              │
│ O texto sugere que:                          │
│ 1. Unidade não é o problema; rebelião é.    │
│ 2. A linguagem é instrumento de comunhão... │
│                                              │
│ [i] Esta é nossa leitura, não "o que a      │
│     Bíblia diz" automaticamente.             │
│                                              │
└──────────────────────────────────────────────┘
```

**Estilo:**
- Fundo off-white `#F5F4F2`
- Borda hairline
- Info box com ícone — esclarece que é interpretação nossa, não texto

### 3.5 Componente "Aplicação pastoral"

```
┌──────────────────────────────────────────────┐
│ **Aplicação pastoral**                       │
│                                              │
│ (fundo off-white)                           │
│                                              │
│ - Para quem ouve chamado radical...          │
│ - Para quem questiona "Deus sabe o que      │
│   faz?"...                                   │
│ - Para comunidades cristãs...                │
│                                              │
└──────────────────────────────────────────────┘
```

**Estilo:** mesmo da interpretação (off-white), mas claramente distinto pelo título.

### 3.6 Componente "Questões em aberto"

```
┌──────────────────────────────────────────────┐
│ **Questões em aberto**                       │
│                                              │
│ ◆ Cronologia do chamado: Atos 7:2 diz que  │
│   Deus chamou Abrão em Ur antes de sair... │
│                                              │
│ ◆ "Terra que te mostrarei" vs conhecimento  │
│   prévio...                                  │
│                                              │
│ [!] Estas questões permanecem em            │
│     debate entre comentaristas.              │
│                                              │
└──────────────────────────────────────────────┘
```

**Estilo:**
- Fundo branco ou ligeiramente off-white
- Borda em azul profundo `#315A72` (divergência)
- ◆ como marker visual
- Ícone info (!) indicando debate

---

## 4. Página de tema ou assunto

Layout similar, mas focado em referências cruzadas:

```
┌────────────────────────────────────────────────────┐
│ Chamado & Obediência                           ❤️ │
│ Tema de emocional/situação: quando alguém...    │
└────────────────────────────────────────────────────┘

Versículos relacionados:
• Gênesis 12:1-9 — Abrão chamado a sair
• Hebreus 11:8-10 — "Abrão obedeceu..."
• 1 Pedro 1:3-7 — Fé testada = ouro refinado

Dinâmica:
- Fé sem garantia geográfica
- Renúncia tripla
- Obediência imediata
- Revelação progressiva

Assuntos associados:
• Promessa Abraâmica
• Fé
• Confiança
```

---

## 5. Página de genealogia

**Render de SVG com interatividade:**

```
        Noé
       / | \
     /   |   \
   Sem  Cam  Jafé
    |    |
   Abrão Canaã
   / \
Isaque Ismael
```

**Codificação visual:**
- Linhagem principal: linha preta contínua
- Linhagem secundária: linha tracejada cinza
- Linhagem messiânica: linha vermelha (João Red)
- Linhagem sacerdotal: linha ocre
- Gênero: tag pequena no canto da caixa

**Interatividade:**
- Hover em pessoa = destaca linhagem inteira
- Click = abre página da pessoa
- Tooltip = datas, aliases, resumo curto

---

## 6. Componentes reutilizáveis

### 6.1 Card de verso (em resultados)

```
┌─────────────────────────────────────┐
│ Gênesis 12:1-9                  ❤️ │
│ A Chamada de Abraão                 │
│                                     │
│ Ora disse o SENHOR a Abrão...       │
│                                     │
│ 📖 Verso  👤 Abraão  📍 Canaã       │
│                                     │
│ #chamado #fé #promessa              │
└─────────────────────────────────────┘
```

**Estilo:**
- Radius 6px, borda hairline
- Branco, hover = fundo off-white
- Coração vermelho para favoritar

### 6.2 Card de pessoa

```
┌──────────────────────────┐
│ 👤 Abraão                │
│                          │
│ Patriarca central        │
│ Gênesis 12-25            │
│                          │
│ Nascimento: c. 2100 A.C. │
│ Família: Sarai, Isaque   │
│                          │
│ 🔗 5 versículos          │
└──────────────────────────┘
```

### 6.3 Indicador de nível de confiança

```
⭐ ⭐ ⭐  Alto
⭐ ⭐      Médio
⭐         Baixo
```

Renderizar como 1-3 ícones de Star (Lucide), cheios ou vazios.

---

## 7. Tipografia aplicada

| Uso | Fonte | Peso | Tamanho |
|---|---|---|---|
| Título página | League Gothic | 700 | 48px |
| Título seção | Hanken | 700 | 28px |
| Subtitle | Hanken | 600 | 18px |
| Corpo | Hanken | 400 | 16px |
| Secundário (fonte, meta) | Hanken | 400 | 14px muted |
| Legenda | Hanken | 400 | 12px muted |

---

## 8. Paleta de cores aplicada

| Elemento | Cor | Hex |
|---|---|---|
| Texto principal | Ink | `#0E0E0E` |
| Fundo | Paper | `#FFFFFF` |
| Fundo secundário | Off-white | `#F5F4F2` |
| Bordas | Hairline | `#E4E4E2` |
| Texto secundário | Muted | `#6B6B68` |
| Destaque (Cristo) | João Red | `#E5341E` |
| Divergência | Azul profundo | `#315A72` |
| Contexto histórico | Terracota | `#8A5A44` |
| Sacerdócio | Ocre | `#A67C32` |

---

## 9. Responsividade

### Desktop (1200px+)
- 3 colunas: sidebar esq, conteúdo central, sidebar dir

### Tablet (768px - 1199px)
- 2 colunas: conteúdo central, sidebar dir
- Sidebar esq fica em collapse

### Mobile (<768px)
- 1 coluna: conteúdo central
- Sidebar esq como drawer (menu hambúrguer)
- Sidebar dir como abas deslizáveis

---

## 10. Checklist de implementação

- [ ] Página de busca (landing)
- [ ] Busca em tempo real (autocomplete)
- [ ] Página de verso (6 blocos)
- [ ] Página de tema
- [ ] Página de assunto
- [ ] Página de pessoa
- [ ] Página de lugar
- [ ] Genealogia SVG interativa
- [ ] Timeline para cronologia
- [ ] Cards reutilizáveis
- [ ] Responsividade em 3 breakpoints
- [ ] Modo escuro (opcional, seguir `sistema-visual.md`)
- [ ] Favoritos (localStorage)
- [ ] Compartilhamento (vers link)

---

## 11. Referências

- [`sistema-visual.md`](sistema-visual.md) — paleta, tipografia, princípios
- [`guia-de-marca.md`](guia-de-marca.md) — identidade pessoal
- [`../_INDICE.md`](../_INDICE.md) — estrutura de conteúdo
