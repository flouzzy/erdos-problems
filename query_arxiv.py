import urllib.request
import urllib.parse
import json

query = urllib.parse.quote_plus("Erdos Straus conjecture")
url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"

try:
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    with open('arxiv_results.txt', 'w') as f:
        f.write(data)
    print("Success")
except Exception as e:
    print(f"Error: {e}")
