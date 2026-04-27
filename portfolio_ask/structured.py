from portfolio_ask.loader import load_portfolio
from collections import defaultdict


def calculate_sector_exposure():
    portfolio = load_portfolio()

    total_value = sum(p["quantity"] * p["current_price"] for p in portfolio)

    sector_totals = defaultdict(float)

    for p in portfolio:
        value = p["quantity"] * p["current_price"]
        sector_totals[p["sector"]] += value

    result = []
    for sector, value in sector_totals.items():
        result.append({
            "sector": sector,
            "weight_pct": round((value / total_value) * 100, 2)
        })

    return result