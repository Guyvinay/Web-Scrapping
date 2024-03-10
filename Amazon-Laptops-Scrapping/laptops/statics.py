
#Base Laptop Seach Url
SEARCH_URL = "https://www.amazon.in/s?k=laptops"

SCRAP_DATA_UPTO_PAGES = 20

# Pin codes
PINCODES = {
    "Delhi": "110001",
    "Bangalore": "560001"
}

# PINCODES = {
#     "Delhi": "110001"
# }

AGENTS = {
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/97.0.1072.50 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/96.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/605.1.15"
    }

#Headers containing User-Agent to bypass: 503 Service Unavailable Error.
HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
        }

# Minimum cart value
MIN_CART_VALUE = 100
