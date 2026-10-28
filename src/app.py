from flask import Flask
import pymysql
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        connection = pymysql.connect(
            host=os.environ.get('DB_HOST', 'db'),
            user=os.environ.get('DB_USER', 'victor'),
            password=os.environ.get('DB_PASSWORD', 'secreto'),
            database=os.environ.get('DB_NAME', 'holamundo_db')
        )
        return """
        <h1>¡Hola Mundo!</h1>
        <h2>Práctica 7: Web App con Dockerfile y Docker Compose</h2>
        <p>¡Conexión a MySQL exitosa! 🚀</p>
        <p>Víctor Núñez - Matrícula: 2012-0048</p>
        """
    except Exception as e:
        return f"""
        <h1>¡Hola Mundo!</h1>
        <h2>Práctica 7: Web App con Dockerfile y Docker Compose</h2>
        <p>Error conectando a MySQL: {e}</p>
        <p>Víctor Núñez - Matrícula: 2012-0048</p>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
