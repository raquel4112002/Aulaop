# Microservices Demo (Frontend -> API -> Auth)

Projeto didatico para mostrar arquitetura distribuida com:

- servicos separados
- comunicacao entre servicos
- logs centralizados
- falhas parciais
- timeouts

## Estrutura

```text
microservices-demo/
├── docker-compose.yml
├── frontend/
│   └── index.html
├── api/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── auth/
    ├── app.py
    ├── requirements.txt
    └── Dockerfile
```

## Como correr

```bash
docker compose up --build
```

## Como testar

- Frontend: <http://localhost:8080>
- API: <http://localhost:5000>
- Auth: <http://localhost:5001>

## Logs

Todos os servicos:

```bash
docker compose logs -f
```

Servico especifico:

```bash
docker compose logs -f api
docker compose logs -f auth
```

## Demo de falha parcial

1. Para o auth:

```bash
docker compose stop auth
```

2. Faz login no frontend novamente.

Esperado: frontend e API continuam vivos, login falha por indisponibilidade do auth.

## Demo de timeout

No `auth/app.py`, adiciona `time.sleep(5)` no inicio de `validate()`.
A API usa timeout de 2s, logo deve devolver erro 504.

Depois:

```bash
docker compose up --build auth
```

## Fluxo para explicar em aula

`Frontend -> API -> Auth Service`
