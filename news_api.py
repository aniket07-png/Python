import requests

def news_api():
    api_url = "https://newsdata.io/api/1/latest"

    API_KEY = "pub_a61c222719a249448aefe51db7bc0e7b"

    arg = {
        "apikey": API_KEY,
        "country": "in",
        "language": "en"
    }

    response = requests.get(api_url, params=arg)
    data = response.json()

    with open("output.txt", "w") as f:
        for article in data.get("results", []):
            title = article.get("title", "No Title")
            print(title)
            f.write(title + "\n")

news_api()
