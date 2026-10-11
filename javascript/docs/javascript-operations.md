# Crawlora eBay JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `10`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ebay | `ebay.item` | `ebay-item` | `GET /ebay/item/{item_id}` | `item_id` (path string required) | `ApiKeyAuth` | `EbayItemResponse` |  |
| ebay | `ebay.liveStreams` | `ebay-live-streams` | `GET /ebay/live/streams` | `category` (query "explore" \| "IPqZx79LNuwFcSVt" \| "oHjQFTlZ5cYgWkjB" \| "l68DJtBAVZge4x4n" \| "2Nk3OYiOJHfXqpWG" \| "5quuEnjO3axyz46U" \| "nGpMTpm13Q86Eaoo" \| "sYRxeaskGmNC6xaB" \| "iYaYo88zN2vtQorh" \| "GYAbsFw6onSNloAb" \| "WJ9zLwYjK8njaBtN" \| "rALkRyk8gXHzIBR6" \| "DNta0sJ8Y6NXZsC9" \| "GU4UfBzZSF4jiteS" \| "IO7Oih07PtNJSWhU" \| "cF4xtF8z9riubmLh" \| "bywKDIdtxhi4hUSO")<br>`request_number` (query number)<br>`session_id` (query string) | `ApiKeyAuth` | `EbayLiveStreamsResponse` |  |
| ebay | `ebay.liveStreamsBatch` | `ebay-live-streams-batch` | `GET /ebay/live/streams/batch` | `ids` (query string required) | `ApiKeyAuth` | `EbayLiveStreamsBatchResponse` |  |
| ebay | `ebay.liveStream` | `ebay-live-stream` | `GET /ebay/live/streams/{id}` | `id` (path string required) | `ApiKeyAuth` | `EbayLiveStreamResponse` |  |
| ebay | `ebay.liveStreamItems` | `ebay-live-stream-items` | `GET /ebay/live/streams/{id}/items` | `id` (path string required) | `ApiKeyAuth` | `EbayLiveStreamItemsResponse` |  |
| ebay | `ebay.search` | `ebay-search` | `POST /ebay/search` | `option` (body string required) | `ApiKeyAuth` | `EbaySearchResponse` |  |
| ebay | `ebay.seller` | `ebay-seller` | `GET /ebay/seller/{seller}` | `seller` (path string required) | `ApiKeyAuth` | `EbaySellerResponse` |  |
| ebay | `ebay.sellerAbout` | `ebay-seller-about` | `GET /ebay/seller/{seller}/about` | `seller` (path string required) | `ApiKeyAuth` | `EbaySellerAboutResponse` |  |
| ebay | `ebay.sellerFeedback` | `ebay-seller-feedback` | `GET /ebay/seller/{seller}/feedback` | `seller` (path string required)<br>`page` (query number)<br>`per_page` (query "24" \| "48" \| "72") | `ApiKeyAuth` | `EbaySellerFeedbackResponse` |  |
| ebay | `ebay.sellerShop` | `ebay-seller-shop` | `GET /ebay/seller/{seller}/shop` | `seller` (path string required)<br>`page` (query number) | `ApiKeyAuth` | `EbaySellerShopResponse` |  |
