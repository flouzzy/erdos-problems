import arxiv

client = arxiv.Client()
search = arxiv.Search(
  query = "Erdos-Straus",
  max_results = 2,
  sort_by = arxiv.SortCriterion.Relevance
)

for result in client.results(search):
    print(f"Title: {result.title}")
    print(f"Authors: {[author.name for author in result.authors]}")
    print(f"Summary: {result.summary}")
    print("-" * 40)
