import urllib.request, urllib.parse, xml.etree.ElementTree as ET

query = urllib.parse.quote_plus('all:"Erdos-Gyarfas conjecture"')
url = f'http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=5'
try:
    response = urllib.request.urlopen(url)
    tree = ET.parse(response)
    root = tree.getroot()
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
        print(f"Title: {title}")
        print(f"Authors: {', '.join(authors)}")
        print(f"Summary: {summary.strip()}")
        print("-" * 40)
except Exception as e:
    print(f"Error: {e}")
