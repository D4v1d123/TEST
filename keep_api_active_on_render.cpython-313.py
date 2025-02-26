from time import sleep
import requests

def consultUser(id):
    requests.get(f'https://api-ticktick.onrender.com/api/v1/users/{id}/')
    print('Updated API')
    
while True:
    consultUser(1)
    sleep(780) # 13 minutes
    