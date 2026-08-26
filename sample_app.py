from flask import Flask
import os
import pymysql

sample = Flask(__name__)


@sample.route("/")
def home():
  try:
    conn = pymysql.connect(
        host="servidor-bd",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="082_db",
        MYSQL_PASSWORD = "super_secret_123"
    )
    conn.close()
    db_status = (
        "Conexión exitosa a la base de datos, prueba para CI/CD para"
        " despliegue continuo"
    )
  except Exception as e:
    db_status = f"Error al conectar a la base de datos: {e}"

  return f"<h1>Bienvenido a mi aplicación Sofia</h1><p>{db_status}</p>"


if __name__ == "__main__":
  modo_debug = os.getenv("FLASK_DEBUG", "True").lower() == "true"
  sample.run(host="0.0.0.0", port=5051, debug=True)  # nosec B104