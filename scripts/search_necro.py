import urllib.request
import urllib.parse
import re

def search_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        snippets = re.findall(r'<a class="result__snippet[^>]*>(.*?)</a>', html, re.I | re.S)
        for s in snippets:
            print(re.sub(r'<[^>]+>', '', s).strip())
            print('-'*40)
    except Exception as e:
        print("Error:", e)

search_ddg('site:necrocanada.com "Lionel Deschenes" Gemma')
search_ddg('site:nosorigines.qc.ca "Lionel Deschenes" Gemma')
search_ddg('"Lionel Deschenes" Gemma "ile"')
