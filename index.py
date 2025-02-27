from http.server import SimpleHTTPRequestHandler, HTTPServer
from time import sleep
import requests
    
PORT = 8000

def consultUser(id):
    requests.get(f'https://api-ticktick.onrender.com/api/v1/users/{id}/')
    print('Activated API')

with HTTPServer(('https://test-sbgp.onrender.com', PORT), SimpleHTTPRequestHandler) as httpd:
    while True:
        consultUser(1)
        sleep(780) # 13 minutes
        httpd.serve_forever()