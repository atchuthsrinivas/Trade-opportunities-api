import requests

def fetch_market_data(sector: str) -> list[str]:
    """
    Fetches recent market-related info for the given sector
    """
    query = f"{sector} sector India market news"
    url = f"https://api.duckduckgo.com/?q={query}&format=json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json().get("RelatedTopics", [])
        results = []

        for item in data:
            if isinstance(item, dict) and "Text" in item:
                results.append(item["Text"])

        return results[:5]

    except Exception:
        return []
