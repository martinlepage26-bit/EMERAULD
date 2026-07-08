import urllib.request
import urllib.parse
import re

def search_bing(query):
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        # Extract snippets from Bing
        snippets = re.findall(r'<div class="b_caption"><p[^>]*>(.*?)</p>', html, re.I | re.S)
        print(f"--- Results for {query} ---")
        for s in snippets:
            clean = re.sub(r'<[^>]+>', '', s).strip()
            if clean:
                print(clean)
    except Exception as e:
        print("Error:", e)

search_bing('"Lionel Deschenes" "Gemma"')
search_bing('"Lionel Deschesnes" "Gemma"')
search_bing('"Martin-Léonard Deschesnes"')
search_bing('"Martin-Leonard Deschenes"')
search_bing('"Léonard Deschenes" "Gemma"')
