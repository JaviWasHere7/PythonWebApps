from requests import get

response = get('https://google.com')
print(response)
print(response.text)