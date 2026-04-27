from portfolio_ask.retriever import retrieve

query = "What is happening in IT sector?"

results = retrieve(query)

print("\nTop Results:\n")

for r in results:
    print("-", r)