from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import mysql.connector

app = Flask(__name__)

# Configuração do Banco de Dados MySQL
db_config = {
    "host": "db",
    "user": "root",
    "password": "root",
    "database": "alunos_db"
}

# Configuração do Swagger
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL,
    config={"app_name": "API de Cadastro de Alunos"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# Criar conexão com o banco de dados
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn


# Criar tabela de alunos se não existir
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# Rota para cadastrar aluno
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.get_json()
    nome = data.get("nome")

    if not nome:
        return jsonify({"error": "Nome é obrigatório"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome) VALUES (%s)", (nome,))
    conn.commit()
    aluno_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": aluno_id, "nome": nome}), 201


# Rota para listar alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()

    return jsonify(alunos)


if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000, debug=True)
