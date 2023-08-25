import os 
from base64 import b64decode, b64encode
import sys

def main(file_path):
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    with open(file_path, 'w') as json_file:
        json_file.write(b64decode(key).decode())
        print(os.path.realpath(file_path))

def encode(path):
    with open(path, 'r') as json_file:
        encoded = b64encode(json_file.read().encode())
    print(encoded)

def get_credentials(file_path):
    key = None
    with open(file_path, 'r') as json_file:
        key = json_file.read()
    
    key = b64decode(key.encode())

    print(key)

if __name__ == '__main__':
    get_credentials('credentials.json')
    #main(file_path='credentials.json')
    #encode(sys.argv[1])
