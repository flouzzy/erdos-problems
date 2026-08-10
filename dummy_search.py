import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time

url = 'http://export.arxiv.org/api/query?search_query=all:erdos+sos&start=0&max_results=3'
for attempt in range(5):
    try:
        response = urllib.request.urlopen(url)
        xml_data = response.read()
        root = ET.fromstring(xml_data)

        namespace = {'atom': 'http://www.w3.org/2005/Atom'}
        for entry in root.findall('atom:entry', namespace):
            title = entry.find('atom:title', namespace).text
            summary = entry.find('atom:summary', namespace).text
            authors = [author.find('atom:name', namespace).text for author in entry.findall('atom:author', namespace)]
            print(f"Title: {title.strip()}")
            print(f"Authors: {', '.join(authors)}")
            print(f"Summary: {summary.strip()[:200]}...")
            print("-" * 40)
        break
    except Exception as e:
        print(f"Attempt {attempt+1} failed: {e}")
        time.sleep(2)
