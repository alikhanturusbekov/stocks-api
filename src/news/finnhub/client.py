import os
import finnhub

api_key = os.environ.get("FINNHUB_API_KEY")
finnhub_client = finnhub.Client(api_key=api_key)
