"""Typed eBay client for the Crawlora hosted API."""

from .platform import EbayClient, AsyncEbayClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = EbayClient
AsyncClient = AsyncEbayClient
__version__ = '0.1.2'
DISPLAY_NAME = 'eBay'
PLATFORM = 'ebay'
CONTRACT_REVISION = 'sha256:50b2e34ad52f6fe505511c8f638f9d59682bc7dc9e4cf474f44b17feb2a6aaae'

__all__ = [
    "EbayClient", "AsyncEbayClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
