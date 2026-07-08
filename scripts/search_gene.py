import urllib.request
import urllib.parse
import json
import re

def search_findagrave():
    # Attempting to search findagrave for any Lionel Deschenes who died 1989-1992
    # FindAGrave uses a complex AJAX/API but we can try duckduckgo specifically restricted to findagrave.com
    
    queries = [
        'site:findagrave.com "Lionel Deschenes"',
        'site:findagrave.com "Lionel Deschene"',
        'site:findagrave.com "Lionel DeChene"',
        'site:findagrave.com "Lionel Deschênes"',
        'site:echovita.com "Lionel Deschenes"',
        'site:genealogiequebec.com "Lionel Deschenes" "Gemma"',
        'site:nosorigines.qc.ca "Lionel Deschenes" "Gemma"',
        'site:peancestry.com "Lionel"'
    ]
    
    for q in queries:
        url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(q)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
            snippets = re.findall(r'<a class="result__snippet[^>]*>(.*?)</a>', html, re.I | re.S)
            print(f"--- Results for {q} ---")
            for s in snippets:
                clean = re.sub(r'<[^>]+>', '', s).strip()
                if clean:
                    print(clean)
        except Exception as e:
            pass # ignore block or errors

search_findagrave()
