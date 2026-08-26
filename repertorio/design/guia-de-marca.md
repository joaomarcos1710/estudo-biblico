# Guia de Marca — João Marcos

Referência de cor, tipografia e uso visual. Aplicar em qualquer peça nova do repertório (páginas de busca, artifacts, banners, exports) a partir de agora.

## Paleta de cores

| Nome | Hex | Uso |
|---|---|---|
| Ink (preto) | `#0E0E0E` | Texto, fundo de seções de contraste |
| Paper (branco) | `#FFFFFF` | Fundo principal |
| Off-white | `#F5F4F2` | Fundo alternado (seções secundárias) |
| Linha (hairline) | `#E4E4E2` | Bordas finas, divisórias |
| Muted (cinza texto) | `#6B6B68` | Texto secundário / legendas |
| Vermelho (acento) | `#E5341E` | Único acento — CTA, números-chave, destaque |
| Vermelho hover | `#C72A16` | Hover/press do acento |
| Vermelho suave | `#FBE2DE` | Fundo tintado leve (tags, alertas leves) |

**Regra de ouro:** preto e branco + 1 vermelho. Nunca uma segunda cor de destaque. Vermelho com moderação — nunca como fundo grande, só em detalhes.

## Tipografia

- **Títulos e números grandes:** League Gothic — condensada, sempre CAIXA ALTA, tracking quase neutro (`0.005em`).
- **Todo o resto** (corpo, botões, formulários, legendas): Hanken Grotesk, pesos 400–800.
- Sem terceira fonte (sem mono).

```css
@import url('https://fonts.googleapis.com/css2?family=League+Gothic&family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap');
```

## Forma & espaçamento

- Cantos retos/afiados: radius 2–10px. Pill (arredondado total) só em tags/badges e botão de newsletter.
- Sombra quase inexistente — a marca se apoia em linha fina e cor, não em elevação.
- Bordas: linhas finas (`#E4E4E2`) separando seções, não cards com sombra pesada.
- Hover: botões escurecem ou invertem cor; escala ~0.97 no clique, sem bounce.

## Voz & tom

- Primeira pessoa, direta.
- CTAs em verbo + ação.
- Títulos em caixa alta; corpo em texto normal.
- Sem emoji na interface (ok em posts/legendas de redes).
- Vibe: performance, foco, autenticidade, fé — dados reais em vez de adjetivos vagos.

## Imagens

- Fotos reais, nunca ilustração, 3D ou banco de imagens genérico.
- Tratamento natural, sem filtro pesado.

## Ícones

- Redes sociais: Simple Icons.
- Interface (seta, envelope, check): Lucide, traço fino, 16–18px.
- Nunca ícone desenhado à mão.

## Checklist ao criar qualquer peça nova

- [ ] Fundo branco, off-white (`#F5F4F2`) ou preto (`#0E0E0E`) — nunca gradiente
- [ ] Título em League Gothic, caixa alta
- [ ] Corpo/botões em Hanken Grotesk
- [ ] Só o vermelho `#E5341E` como acento, com moderação
- [ ] Cantos retos (2–10px), sem sombra pesada
- [ ] Fotos reais, nunca stock genérico ou ilustração (quando houver imagem)

## Aplicações no repertório

- **Página de busca** (artifact): fundo branco/preto conforme tema do sistema, título em League Gothic, versículos com borda esquerda vermelha, comentários e tags em Hanken Grotesk, painel de entidade como bloco preto sólido com destaque vermelho.

## Referências

- Site ao vivo (mídia kit): https://joaomarcos1710.github.io/midia-kit/
