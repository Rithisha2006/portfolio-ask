from portfolio_ask.loader import load_portfolio, load_news
from portfolio_ask.embeddings import get_embeddings
from portfolio_ask.vector_store import VectorStore


def build_store():
    # Load data
    portfolio = load_portfolio()
    news = load_news()

    # Convert portfolio into text
    portfolio_texts = [
        f"{item['ticker']} in {item['sector']} sector price {item['current_price']}"
        for item in portfolio
    ]

    # Combine all data
    all_texts = portfolio_texts + news

    # Create embeddings
    embeddings = get_embeddings(all_texts)

    # Build vector store
    store = VectorStore(len(embeddings[0]))
    store.add(embeddings, all_texts)

    return store


def retrieve(query):
    # Build vector store
    store = build_store()

    # Convert query to embedding
    query_embedding = get_embeddings([query])[0]

    # Search
    results = store.search(query_embedding, k=5)

    # Create sources mapping (IMPORTANT FIX)
    sources = {
        f"[{i+1}]": results[i]
        for i in range(len(results))
    }

    return results, sources