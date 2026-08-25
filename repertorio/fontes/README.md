# Fontes de texto bíblico

Textos das traduções usadas no repertório, em JSON (um arquivo por livro), para consulta rápida e cópia dos versículos.

## NVI (Nova Versão Internacional)

Origem: [damarals/biblias](https://github.com/damarals/biblias) (compilação em JSON, licença MIT do projeto).

O **texto da NVI em si é copyright da Biblica**, não domínio público — a licença MIT cobre apenas a compilação/formato do projeto de origem. Uso aqui é pessoal, para preparo de estudos e aconselhamento, não redistribuição pública.

Formato de cada arquivo (`fontes/NVI/<CÓDIGO>.json`):

```json
{
  "code": "JON",
  "name": "Jonas",
  "chapters": [
    { "number": 1, "verses": [ { "number": 1, "text": "..." } ] }
  ]
}
```

Códigos seguem abreviação em inglês (ex: `GEN`, `JON`, `MAT`, `JHN`, `REV`).
