import requests

api_url = "https://newsdata.io/api/1/latest?"

API_KEY = "pub_a61c222719a249448aefe51db7bc0e7b"

arg = {
    "apikey": API_KEY,
    "country": "in",
    "language": "en"
}

response = requests.get(api_url,arg) 
data = response.json()

for article in data.get("results", []):
    print(article.get("title"))
