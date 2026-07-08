import urllib.request
import urllib.parse
import json

def search_banq():
    url = 'https://collections.banq.qc.ca/api/bna/search?text="Lionel Deschênes" Gemma'
    # Try different search text variations
    queries = [
        '"Lionel Deschênes" Gemma',
        '"Lionel Deschenes" Gemma',
        'Lionel Gemma Deschênes'
    ]
    for q in queries:
        try:
            req = urllib.request.Request(
                f"https://adv-api.banq.qc.ca/api/explore/v2.1/catalog/datasets/bna/records?select=*&where=search(text, '{urllib.parse.quote(q)}')",
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            data = urllib.request.urlopen(req).read().decode('utf-8')
            print(data)
        except Exception as e:
            print("API error or endpoint not found:", e)

search_banq()
