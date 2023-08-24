import os 
from base64 import b64decode, b64encode

def main():
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    with open('path.json', 'w') as json_file:
        json_file.write(b64decode(key).decode())
        print(os.path.realpath('path.json'))

def encode(path):
    with open(path, 'r') as json_file:
        encoded = b64encode(json_file.read().encode())
    print(encoded)

if __name__ == '__main__':
    main()
    #encode('my_credential_path')