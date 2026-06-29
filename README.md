# MVP API Principal

API REST desenvolvida com FastAPI para autenticação de usuários e gerenciamento de veículos, servindo como backend do projeto Garage FIPE.

A API consome uma API externa de dados FIPE e realiza o cache dos dados coletados
em um banco próprio, reduzindo sobrecarga e aumentando a disponibilidade das informações.

## Tecnologias

- Python
- FastAPI
- SQLModel
- Uvicorn

## Pré-requisitos

Antes de iniciar, instale:

- Python 3.11 ou superior
- pip
- virtualenv (opcional, mas recomendado)
- Instância PostgreSQL no AWS RDS
- Docker (opcional, para execução em container)

## Instalação e configuração local

1. Entre na pasta da API:

	cd mvp-api-principal

2. Crie o ambiente virtual:

	python -m venv venv

3. Ative o ambiente virtual:

	Windows (PowerShell):

	.\venv\Scripts\Activate

	Linux/Mac:

	source venv/bin/activate

4. Instale as dependências:

	pip install -r requirements.txt

5. Configure a conexão com o AWS RDS:

	Linux/Mac:

	export DATABASE_URL="postgresql+psycopg://usuario:senha@seu-endpoint-rds.amazonaws.com:5432/garage?sslmode=require"

	Windows (PowerShell):

	$env:DATABASE_URL="postgresql+psycopg://usuario:senha@seu-endpoint-rds.amazonaws.com:5432/garage?sslmode=require"

	Alternativa com variáveis separadas (sem URL completa):

	RDS_HOSTNAME, RDS_PORT, RDS_DB_NAME, RDS_USERNAME, RDS_PASSWORD, DB_SSLMODE

## Executando a aplicação

Com o ambiente virtual ativo, execute:

uvicorn main:app --reload

A API ficará disponível em:

- http://localhost:8000

Documentação automática:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Executando com Docker

1. Crie o arquivo de ambiente:

	cp .env.example .env

2. Suba API + PostgreSQL:

	docker compose up --build

	Observação: com esta configuração, o `docker-compose` sobe apenas a API e usa o banco no AWS RDS.

## Estrutura resumida

- routes: definição das rotas da API.
- models: modelos de dados e criação de tabelas.
- schemas: esquemas de validação e serialização.
- services: integrações e regras de negócio.
- utils: utilitários compartilhados.

## Observações

- O backend está configurado para aceitar requisições do frontend em http://localhost:5173.
- Para RDS, libere acesso ao Security Group da instância para o IP/rede onde a API executa.


## Fluxograma

![alt text](image.png)
