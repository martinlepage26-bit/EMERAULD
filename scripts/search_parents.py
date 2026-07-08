import urllib.request
import urllib.parse
import re

def search_geneanet(query):
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        snippets = re.findall(r'<p[^>]*>(.*?)</p>', html, re.I | re.S)
        for s in snippets:
            clean = re.sub(r'<[^>]+>', '', s).strip()
            if "Normand" in clean or "Deschenes" in clean or "Deschênes" in clean or "Deschesnes" in clean:
                print(clean)
    except Exception as e:
        pass

search_geneanet('site:geneanet.org "Martin-Léonard" "Deschênes" "Gemma Normand"')
search_geneanet('site:mesaieux.com "Martin-Léonard" "Deschênes"')
search_geneanet('site:mesaieux.com "Léonard Deschesnes" "Gemma Normand"')
