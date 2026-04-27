import json
import os


def load_portfolio():
    with open("data/portfolio.json") as f:
        return json.load(f)


def load_news():
    news = []
    for file in os.listdir("data/news"):
        with open(f"data/news/{file}", encoding="utf-8") as f:
            news.append(f.read())
    return news