# Task Management API

Uma API REST moderna para gerenciar tarefas, construída com FastAPI.

## Instalação

```bash
pip install -r requirements.txt
```

## Executar a API

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

## Documentação Interativa

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

### Raiz
- `GET /` - Informações da API

### Tarefas (CRUD)

#### Listar todas as tarefas
```bash
GET /tasks
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
    "updated_at": "2024-08-28T10:00:00"
  }
]
```

#### Criar nova tarefa
```bash
POST /tasks
Content-Type: application/json

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
  "updated_at": "2024-08-28T10:00:00"
}
```

#### Obter tarefa específica
```bash
GET /tasks/{id}
```

**Resposta (200):**
```json
{
  "id": 1,
  "title": "Minha tarefa",
  "description": "Descrição da tarefa",
  "completed": false,
  "created_at": "2024-08-28T10:00:00",
  "updated_at": "2024-08-28T10:00:00"
}
```

#### Atualizar tarefa
```bash
PUT /tasks/{id}
Content-Type: application/json

{
  "title": "Título atualizado",
  "description": "Nova descrição",
  "completed": true
}
```

Todos os campos são opcionais. Apenas os campos enviados serão atualizados.

**Resposta (200):**
```json
{
  "id": 1,
  "title": "Título atualizado",
  "description": "Nova descrição",
  "completed": true,
  "created_at": "2024-08-28T10:00:00",
  "updated_at": "2024-08-28T10:05:00"
}
```

#### Deletar tarefa
```bash
DELETE /tasks/{id}
```

**Resposta (204 No Content)**

### Estatísticas

#### Resumo de tarefas
```bash
GET /tasks/stats/summary
```

**Resposta (200):**
```json
{
  "total": 10,
  "completed": 3,
  "pending": 7
}
```

## Exemplos com cURL

```bash
# Criar uma tarefa
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Aprender FastAPI","description":"Estudar a documentação"}'

# Listar todas as tarefas
curl http://localhost:8000/tasks

# Listar apenas tarefas pendentes
curl http://localhost:8000/tasks?completed=false

# Obter tarefa específica
curl http://localhost:8000/tasks/1

# Atualizar tarefa (marcar como completa)
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'

# Deletar tarefa
curl -X DELETE http://localhost:8000/tasks/1

# Obter estatísticas
curl http://localhost:8000/tasks/stats/summary
```

## Modelos de Dados

### Task
```python
{
  "id": int,
  "title": str (1-200 caracteres),
  "description": str (opcional, até 1000 caracteres),
  "completed": bool (padrão: false),
  "created_at": datetime,
  "updated_at": datetime
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

## Códigos de Status HTTP

- `200 OK` - Requisição bem-sucedida
- `201 Created` - Recurso criado com sucesso
- `204 No Content` - Recurso deletado com sucesso
- `400 Bad Request` - Dados inválidos
- `404 Not Found` - Recurso não encontrado
- `422 Unprocessable Entity` - Erro de validação

## Features

✅ CRUD completo de tarefas  
✅ Validação de dados com Pydantic  
✅ Armazenamento em memória  
✅ Filtragem por status  
✅ Estatísticas de tarefas  
✅ Timestamps automáticos  
✅ Documentação automática (Swagger & ReDoc)  
✅ Tratamento de erros robusto  

## Desenvolvimento Futuro

- [ ] Armazenamento em banco de dados (PostgreSQL)
- [ ] Autenticação e autorização
- [ ] Categorias/projetos para tarefas
- [ ] Datas de vencimento e prioridades
- [ ] Paginação
- [ ] Busca avançada
- [ ] Testes unitários
- [ ] Docker support
