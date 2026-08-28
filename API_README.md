# Task Management API v2.0

Uma API REST moderna e segura para gerenciar tarefas, construída com FastAPI. Inclui autenticação JWT, rate limiting e logging estruturado.

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

Copie o arquivo `.env.example` para `.env` e configure as variáveis:

```bash
cp .env.example .env
```

**Variáveis de ambiente:**
- `SECRET_KEY` - Chave secreta para assinar tokens JWT (mín. 32 caracteres)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Tempo de expiração do token em minutos (padrão: 30)
- `LOG_LEVEL` - Nível de logging (padrão: INFO)

## Executar a API

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

## Documentação Interativa

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Autenticação

### Registro de novo usuário

```bash
POST /auth/register
Content-Type: application/json

{
  "username": "joao",
  "password": "senha_segura",
  "email": "joao@example.com"
}
```

**Resposta (201):**
```json
{
  "id": 1,
  "username": "joao",
  "email": "joao@example.com"
}
```

### Login

```bash
POST /auth/login
Content-Type: application/json

{
  "username": "joao",
  "password": "senha_segura"
}
```

**Resposta (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

### Usar o token

Inclua o token no header `Authorization` de todas as requisições autenticadas:

```bash
Authorization: Bearer {access_token}
```

---

## Endpoints

### Health Check

#### Verificar status da API
```bash
GET /health
```

**Resposta (200):**
```json
{
  "status": "healthy",
  "version": "2.0.0"
}
```

### Tarefas (CRUD) - Requer autenticação

#### Listar todas as tarefas
```bash
GET /tasks
Authorization: Bearer {token}
```

**Query Parameters:**
- `completed` (boolean, opcional) - Filtrar por status de conclusão

**Resposta (200):**
```json
[
  {
    "id": 1,
    "title": "Estudar FastAPI",
    "description": "Aprender os conceitos básicos",
    "completed": false,
    "created_at": "2024-08-28T10:00:00",
    "updated_at": "2024-08-28T10:00:00",
    "user_id": 1
  }
]
```

#### Criar nova tarefa
```bash
POST /tasks
Content-Type: application/json
Authorization: Bearer {token}

{
  "title": "Minha tarefa",
  "description": "Descrição da tarefa (opcional)"
}
```

**Resposta (201):**
```json
{
  "id": 1,
  "title": "Minha tarefa",
  "description": "Descrição da tarefa",
  "completed": false,
  "created_at": "2024-08-28T10:00:00",
  "updated_at": "2024-08-28T10:00:00",
  "user_id": 1
}
```

#### Obter tarefa específica
```bash
GET /tasks/{id}
Authorization: Bearer {token}
```

**Resposta (200):** (veja formato acima)

#### Atualizar tarefa
```bash
PUT /tasks/{id}
Content-Type: application/json
Authorization: Bearer {token}

{
  "title": "Título atualizado",
  "description": "Nova descrição",
  "completed": true
}
```

Todos os campos são opcionais.

**Resposta (200):** (veja formato acima)

#### Deletar tarefa
```bash
DELETE /tasks/{id}
Authorization: Bearer {token}
```

**Resposta (204 No Content)**

#### Obter estatísticas
```bash
GET /tasks/stats/summary
Authorization: Bearer {token}
```

**Resposta (200):**
```json
{
  "total": 10,
  "completed": 3,
  "pending": 7
}
```

---

## Exemplos com cURL

```bash
# Registrar novo usuário
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"joao","password":"senha123","email":"joao@example.com"}'

# Login
TOKEN=$(curl -s -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"joao","password":"senha123"}' | jq -r '.access_token')

# Criar uma tarefa
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"title":"Aprender FastAPI","description":"Estudar a documentação"}'

# Listar todas as tarefas
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/tasks

# Listar apenas tarefas pendentes
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/tasks?completed=false

# Obter tarefa específica
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/tasks/1

# Atualizar tarefa
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"completed":true}'

# Deletar tarefa
curl -X DELETE http://localhost:8000/tasks/1 \
  -H "Authorization: Bearer $TOKEN"

# Obter estatísticas
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/tasks/stats/summary

# Health check (sem autenticação)
curl http://localhost:8000/health
```

---

## Rate Limiting

A API implementa rate limiting por endpoint:

| Endpoint | Limite |
|----------|--------|
| `/` | 100 req/min |
| `/health` | 100 req/min |
| `/auth/register` | 5 req/min |
| `/auth/login` | 10 req/min |
| `/tasks` (GET) | 30 req/min |
| `/tasks` (POST) | 20 req/min |
| `/tasks/{id}` | 30 req/min (GET), 20 req/min (PUT), 20 req/min (DELETE) |
| `/tasks/stats/summary` | 30 req/min |

**Resposta quando limite excedido (429):**
```json
{
  "error": "Rate limit exceeded",
  "detail": "Too many requests. Please try again later."
}
```

---

## Logging Estruturado

Todos os eventos são registrados em formato JSON para facilitar análise:

```json
{
  "timestamp": "2024-08-28T10:00:00",
  "level": "INFO",
  "message": "Login successful",
  "user_id": 1,
  "username": "joao",
  "endpoint": "/auth/login",
  "method": "POST"
}
```

**Eventos registrados:**
- Requisições autenticadas
- Tentativas de login (sucesso/falha)
- Registro de usuários
- Criação/atualização/deleção de tarefas
- Tentativas de acesso não autorizado
- Erros de validação
- Limite de taxa excedido

---

## Modelos de Dados

### User
```python
{
  "id": int,
  "username": str (3-50 caracteres),
  "email": str (email válido)
}
```

### UserCreate
```python
{
  "username": str (3-50 caracteres),
  "password": str (6-100 caracteres),
  "email": str (email válido)
}
```

### Token
```python
{
  "access_token": str,
  "token_type": str (sempre "bearer"),
  "expires_in": int (segundos)
}
```

### Task
```python
{
  "id": int,
  "title": str (1-200 caracteres),
  "description": str (opcional, até 1000 caracteres),
  "completed": bool (padrão: false),
  "created_at": datetime,
  "updated_at": datetime,
  "user_id": int
}
```

### TaskCreate
```python
{
  "title": str (1-200 caracteres),
  "description": str (opcional, até 1000 caracteres)
}
```

### TaskUpdate
```python
{
  "title": str (opcional, 1-200 caracteres),
  "description": str (opcional, até 1000 caracteres),
  "completed": bool (opcional)
}
```

---

## Códigos de Status HTTP

- `200 OK` - Requisição bem-sucedida
- `201 Created` - Recurso criado com sucesso
- `204 No Content` - Recurso deletado com sucesso
- `400 Bad Request` - Dados inválidos ou username já registrado
- `401 Unauthorized` - Token ausente, inválido ou expirado
- `403 Forbidden` - Acesso negado (recurso de outro usuário)
- `404 Not Found` - Recurso não encontrado
- `422 Unprocessable Entity` - Erro de validação de dados
- `429 Too Many Requests` - Limite de taxa excedido

---

## Features

✅ Autenticação com JWT  
✅ Registro e login de usuários  
✅ Rate limiting por endpoint  
✅ Logging estruturado em JSON  
✅ CRUD completo de tarefas  
✅ Isolamento de dados por usuário  
✅ Validação de dados com Pydantic  
✅ Armazenamento em memória  
✅ Filtragem por status  
✅ Estatísticas de tarefas  
✅ Timestamps automáticos  
✅ Documentação automática (Swagger & ReDoc)  
✅ Tratamento de erros robusto  
✅ Health check endpoint  

---

## Segurança

- **Senhas**: Hasheadas com bcrypt
- **Tokens**: Assinados com HMAC-SHA256
- **Isolamento**: Cada usuário só acessa suas tarefas
- **Rate limiting**: Protege contra abuso
- **Logging**: Rastreia acessos não autorizados

---

## Desenvolvimento Futuro

- [ ] Armazenamento em banco de dados (PostgreSQL)
- [ ] Refresh tokens
- [ ] Revogar tokens
- [ ] Compartilhamento de tarefas entre usuários
- [ ] Categorias/projetos para tarefas
- [ ] Datas de vencimento e prioridades
- [ ] Paginação
- [ ] Busca avançada
- [ ] Testes de integração
- [ ] Docker support
- [ ] CI/CD pipeline
