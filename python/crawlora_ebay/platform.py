"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class EbayClient(CrawloraClient):
    """Synchronous eBay API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-ebay-python/0.1.2')
        super().__init__(*args, **kwargs)

    def item(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-item', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_streams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-live-streams', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_streams_batch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-live-streams-batch', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_stream(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-live-stream', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_stream_items(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-live-stream-items', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def seller(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-seller', params, response_type=response_type, timeout=timeout, headers=headers)

    def seller_about(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-seller-about', params, response_type=response_type, timeout=timeout, headers=headers)

    def seller_feedback(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-seller-feedback', params, response_type=response_type, timeout=timeout, headers=headers)

    def seller_shop(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('ebay-seller-shop', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncEbayClient(AsyncCrawloraClient):
    """Asynchronous eBay API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-ebay-python/0.1.2')
        super().__init__(*args, **kwargs)

    async def item(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-item', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_streams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-live-streams', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_streams_batch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-live-streams-batch', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_stream(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-live-stream', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_stream_items(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-live-stream-items', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def seller(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-seller', params, response_type=response_type, timeout=timeout, headers=headers)

    async def seller_about(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-seller-about', params, response_type=response_type, timeout=timeout, headers=headers)

    async def seller_feedback(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-seller-feedback', params, response_type=response_type, timeout=timeout, headers=headers)

    async def seller_shop(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('ebay-seller-shop', params, response_type=response_type, timeout=timeout, headers=headers)
