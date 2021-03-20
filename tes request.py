from pip._vendor import requests

import requests

com = 'https://detik.com'
try:
    response = requests.get(com)
    if response.status_code == 200:
        print(f'success! Response= {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'oopsy daisy ada kesalahan ente {response.status_code}')
except Exception as e:
    print('There is an error', e)
print('Program ended')