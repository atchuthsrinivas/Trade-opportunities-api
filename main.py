from fastapi import FastAPI, Depends, Request
from fastapi.responses import PlainTextResponse
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from auth import verify_api_key
from rate_limiter import limiter
from services.service import fetch_market_data
from services.ai_analysis import analyze_market
from services.report import generate_markdown

app = FastAPI(title="Trade Opportunities API")

# Rate Limiter
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc):
    return PlainTextResponse("Rate limit exceeded", status_code=429)

@app.get("/analyze/{sector}", response_class=PlainTextResponse)
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: str,
    api_key: str = Depends(verify_api_key)
):
    market_data = fetch_market_data(sector)

    analysis = analyze_market(market_data, sector)

    report = generate_markdown(sector, analysis, market_data)

    return report
