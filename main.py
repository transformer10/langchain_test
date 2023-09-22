import requests
from util import conf

data = requests.get('http://localhost:8080/api/v1/weather/today').text
print(data)