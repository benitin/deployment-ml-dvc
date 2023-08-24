import os 
from base64 import b64decode, b64encode
import sys

def main():
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    with open('credential.json', 'w') as json_file:
        json_file.write(b64decode(key).decode())
        print(os.path.realpath('credential.json'))

def encode(path):
    with open(path, 'r') as json_file:
        encoded = b64encode(json_file.read().encode())
    print(encoded)

if __name__ == '__main__':
    main()
    #encode(sys.argv[1])
