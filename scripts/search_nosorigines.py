import urllib.request
import urllib.parse
import re

def search_nosorigines(first, last):
    url = f"https://www.nosorigines.qc.ca/genealogielistfirstname.aspx?Family={urllib.parse.quote(last)}&lng=fr"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {e}"
    
    matches = re.findall(r'<a href="(GenealogieQuebec\.aspx\?pid=\d+&lng=fr)">(.*?)</a>', html)
    results = []
    for href, text in matches:
        if first.lower() in text.lower():
            results.append((text.strip(), "https://www.nosorigines.qc.ca/" + href))
    return results

print("Gerard Lepage:")
for res in search_nosorigines("Gerard", "Lepage"):
    print(res)

print("Lionel Deschenes:")
for res in search_nosorigines("Lionel", "Deschenes"):
    print(res)
