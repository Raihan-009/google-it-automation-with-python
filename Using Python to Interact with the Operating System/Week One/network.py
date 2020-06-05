import requests
import socket


#localhost = socket.gethostbyname('localhost')
#print(localhost)
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
        return True
    else :
        return False

#request = requests.get('http://www.google.com')
#print(request)

#response = request.status_code
#print(response)
def check_connectivity():
    request = requests.get('http://www.google.com')
    response = request.status_code
    if response == 200:
        return True
    else :
        return False
