import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_market(data: list[str], sector: str) -> str:
    """
    Uses Gemini API to analyze market data and return trade insights
    """

    if not data:
        return f"No sufficient market data found for {sector} sector."

    prompt = f"""
You are a market analyst.

Analyze the Indian {sector} sector using the following information.
Provide:
- Current market overview
- Trade opportunities
- Risk factors
- Short-term outlook

Market data:
{chr(10).join(data)}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI analysis failed: {str(e)}"
