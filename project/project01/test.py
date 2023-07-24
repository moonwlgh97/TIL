import requests

url = 'http://fakestoreapi.com/carts'
response = requests.get(url)

print(response.json())