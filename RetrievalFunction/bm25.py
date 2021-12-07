import metapy

idx = metapy.index.make_inverted_index('config.toml')

ranker = metapy.index.OkapiBM25()

query = metapy.index.Document()
query.content('Text mining')    # Enter your query here (Ex: "PLSA" or "How to compute precision and recall?")

top_docs = ranker.score(idx, query, num_results=5)

# d_id corresponds to the line number of the document
# Note that d_id starts at 0, so we increment by 1 to get the real line number
for num, (d_id, _) in enumerate(top_docs):
    content = idx.metadata(d_id).get('content')
    print("{}. {}\n".format(d_id + 1, content))
