import urllib.request
import json
url = 'https://api.github.com/users/naila-systemailabs/repos'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        repos = json.loads(response.read().decode())
        for r in repos:
            print(f"{r['name']}: {r['html_url']}")
except Exception as e:
    print('Error:', e)
