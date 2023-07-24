import requests
API_KEY = 'f1bce7c831ec6549766efef105ce79fb'
lat = 37.56
lon = 126.97
url =f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

# API 요청 보내기
response = requests.get(url).json()
response