import urllib.request
import xml.etree.ElementTree as ET
import urllib.parse

query = urllib.parse.quote_plus("all:Erdos AND all:Moser")
url = f'http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=3'
response = urllib.request.urlopen(url)
xml_data = response.read()
root = ET.fromstring(xml_data)
for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
    title = entry.find('{http://www.w3.org/2005/Atom}title').text
    summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
    authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
    print(f"Title: {title.strip()}")
    print(f"Authors: {', '.join(authors)}")
    print(f"Summary: {summary.strip()[:200]}...\n")
