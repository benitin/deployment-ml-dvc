import os
from base64 import b64decode

def main(json_file_name):
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    
    with open(json_file_name, 'w') as json_file:
        json_file.write(b64decode(key).decode())

if __name__=='__main__':
    main('credentials.json')    