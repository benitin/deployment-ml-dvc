import os
from base64 import b64decode

def main(json_file_name):
    key = "eyJpbnN0YWxsZWQiOnsiY2xpZW50X2lkIjoiNzE5NjY5NjgwNjUtbmkxZzQyNnNqNTJibWphM2thYm1sMW9lbmtrNGwxZWouYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJwcm9qZWN0X2lkIjoiZHZjLW1sb3BzLXJlcG8iLCJhdXRoX3VyaSI6Imh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwidG9rZW5fdXJpIjoiaHR0cHM6Ly9vYXV0aDIuZ29vZ2xlYXBpcy5jb20vdG9rZW4iLCJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLCJjbGllbnRfc2VjcmV0IjoiR09DU1BYLW9PVWJaWlUxR21rWXRaYUcweE5xRlVIT2Z4RUIiLCJyZWRpcmVjdF91cmlzIjpbImh0dHA6Ly9sb2NhbGhvc3QiXX19" #os.environ.get('SERVICE_ACCOUNT_KEY')
    print("Key from environment:", key)
    
    with open(json_file_name, 'w+') as json_file:
        json_file.write(b64decode(key).decode())
        json_file.flush()

    #with open(json_file_name, 'r') as json_file:
    #    print('GDrive Credentials:', json_file.read())
    
    #print('realpath', os.path.realpath(json_file_name))

if __name__=='__main__':
    main('credentials.json')    