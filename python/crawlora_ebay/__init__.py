"""Typed eBay client for the Crawlora hosted API."""

from .platform import EbayClient, AsyncEbayClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = EbayClient
AsyncClient = AsyncEbayClient
__version__ = '0.1.0'
DISPLAY_NAME = 'eBay'
PLATFORM = 'ebay'
CONTRACT_REVISION = 'sha256:e8514c916185f6508e01cf9bf5e07d3d39d49886c8da797ec56300d167e65268'

__all__ = [
    "EbayClient", "AsyncEbayClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
