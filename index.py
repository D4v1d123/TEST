import threading
import time
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configuración de la API externa
API_URL = "https://api-ticktick.onrender.com/api/v1/users/1/"  # Reemplaza con la API real
INTERVALO_SEGUNDOS = 60  # Cada cuánto tiempo hacer la consulta

# Función que consulta la API
def consultar_api():
    while True:
        try:
            print("Consultando API...")
            respuesta = requests.get(API_URL)
            if respuesta.status_code == 200:
                print("Respuesta:", respuesta.json())
            else:
                print("Error en la consulta:", respuesta.status_code)
        except Exception as e:
            print("Error en la solicitud:", e)

        time.sleep(INTERVALO_SEGUNDOS)  # Espera antes de la siguiente consulta

# Clase para el servidor HTTP (necesario para Render)
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Servicio corriendo correctamente")

# Función para iniciar el servidor HTTP
def iniciar_servidor():
    server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
    print("Servidor corriendo en el puerto 8000...")
    server.serve_forever()

# Crear e iniciar hilos para consulta API y servidor web
if __name__ == "__main__":
    # Hilo para la consulta a la API
    hilo_consulta = threading.Thread(target=consultar_api, daemon=True)
    hilo_consulta.start()

    # Iniciar el servidor HTTP en el hilo principal
    iniciar_servidor()
