import os

from crawlora_ebay import EbayClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with EbayClient(api_key=api_key) as client:
    seller = client.seller(seller='musicmagpie')
    print('seller', seller)
    search = client.search(option={'keyword': 'vintage camera'})
    print('search', search)
