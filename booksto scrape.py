import requests


s = requests.Session()

url = 'http://quotes.toscrape.com/login'
payload = {
'username':'a',
'password': 'a'
}
res = s.post(url, data=payload)
print(res.text)