from flask import Flask, request, render_template, jsonify
import sqlite3
import os
import subprocess

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), "database.db")

def init_db():
    """
    Inicializa la base de datos y crea la tabla 'data' si no existe.
    """
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                executable_name TEXT,
                data TEXT
            )
        """)

@app.route("/", methods=["GET"])
def index():
    """
    Muestra la página principal con el menú de opciones.
    """
    return render_template("index.html")

@app.route("/api/data", methods=["GET"])
def get_data():
    """
    Devuelve los datos recibidos desde la base de datos.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data")
        rows = cursor.fetchall()
    return jsonify(rows)

@app.route("/api/command", methods=["POST"])
def execute_command():
    """
    Ejecuta un comando en el servidor y devuelve la salida.
    """
    command = request.json.get("command")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({"output": result.stdout, "error": result.stderr})
    except Exception as e:
        return jsonify({"error": str(e)})

# Inicializar la base de datos antes de iniciar el servidor
init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)