API de Cadastro de Alunos com Flask, Swagger, MySQL e Docker

Este é um projeto de API simples utilizando Flask, Swagger UI, MySQL e Docker para cadastrar e listar nomes de alunos.

🚀 Tecnologias Utilizadas

Python 3

Flask

Flask-Swagger-UI

MySQL

Docker e Docker-Compose

📂 Estrutura do Projeto

api-alunos/
│-- static/
│   ├── swagger.json  # Arquivo de documentação Swagger
│-- app.py  # Código principal da API
│-- Dockerfile  # Configuração do Docker
│-- docker-compose.yml  # Orquestração do Docker
│-- requirements.txt  # Dependências do projeto
│-- README.md  # Documentação do projeto

🔧 Instalação e Configuração

1️⃣ Clonar o Repositório

git clone https://github.com/yuri512w/Api-base-com-Swagger.git
cd Api-base-com-Swagger

2️⃣ Criar e Configurar o Banco de Dados MySQL com Docker

docker-compose up --build

Isso iniciará tanto a API Flask quanto o banco de dados MySQL.

3️⃣ Testar a API

Abra no navegador:

Swagger UI: http://127.0.0.1:5000/swagger

Testar GET /alunos:

curl -X GET http://127.0.0.1:5000/alunos

Testar POST /alunos:

curl -X POST http://127.0.0.1:5000/alunos -H "Content-Type: application/json" -d '{"nome": "João"}'

📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

Se precisar de ajuda, abra uma issue no repositório! 🚀

# api-alunos
