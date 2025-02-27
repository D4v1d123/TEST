from http.server import SimpleHTTPRequestHandler, HTTPServer
from time import sleep
import threading
import requests

PORT = 8000

def consultUser(id):
    while True:
        requests.get(f'https://api-ticktick.onrender.com/')
        print('Activated API')
        sleep(780)  # 13 minutos

# Configurar y ejecutar el servidor en un hilo separado
server = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)

# Iniciar el proceso de consulta en un hilo aparte
thread = threading.Thread(target=consultUser, args=(1,), daemon=True)
thread.start()

print(f"Starting server on port {PORT}...")
server.serve_forever()
