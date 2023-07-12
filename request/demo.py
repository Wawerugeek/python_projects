#!/usr/bin/python3

import requests 

page = {'username': "steve", 'password': 'testing'}

r = requests.post('http://httpbin.org/post', data=page)

# with open('nft.png', 'wb') as f:
#     f.write(r.content)

r_dict = r.json()

print(r_dict['form'])
