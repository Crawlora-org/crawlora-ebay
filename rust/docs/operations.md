# Crawlora eBay Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `10`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ebay | `ebay.item` | `ebay-item` | `GET /ebay/item/{item_id}` | `item_id` (path String required) | `ApiKeyAuth` | `EbayItemResponse` |  |
| ebay | `ebay.live_streams` | `ebay-live-streams` | `GET /ebay/live/streams` | `category` (query String enum{explore, IPqZx79LNuwFcSVt, oHjQFTlZ5cYgWkjB, l68DJtBAVZge4x4n, 2Nk3OYiOJHfXqpWG, 5quuEnjO3axyz46U, nGpMTpm13Q86Eaoo, sYRxeaskGmNC6xaB, iYaYo88zN2vtQorh, GYAbsFw6onSNloAb, WJ9zLwYjK8njaBtN, rALkRyk8gXHzIBR6, DNta0sJ8Y6NXZsC9, GU4UfBzZSF4jiteS, IO7Oih07PtNJSWhU, cF4xtF8z9riubmLh, bywKDIdtxhi4hUSO})<br>`request_number` (query i64)<br>`session_id` (query String) | `ApiKeyAuth` | `EbayLiveStreamsResponse` |  |
| ebay | `ebay.live_streams_batch` | `ebay-live-streams-batch` | `GET /ebay/live/streams/batch` | `ids` (query String required) | `ApiKeyAuth` | `EbayLiveStreamsBatchResponse` |  |
| ebay | `ebay.live_stream` | `ebay-live-stream` | `GET /ebay/live/streams/{id}` | `id` (path String required) | `ApiKeyAuth` | `EbayLiveStreamResponse` |  |
| ebay | `ebay.live_stream_items` | `ebay-live-stream-items` | `GET /ebay/live/streams/{id}/items` | `id` (path String required) | `ApiKeyAuth` | `EbayLiveStreamItemsResponse` |  |
| ebay | `ebay.search` | `ebay-search` | `POST /ebay/search` | `option` (body ModelEbaySearchOption required) | `ApiKeyAuth` | `EbaySearchResponse` |  |
| ebay | `ebay.seller` | `ebay-seller` | `GET /ebay/seller/{seller}` | `seller` (path String required) | `ApiKeyAuth` | `EbaySellerResponse` |  |
| ebay | `ebay.seller_about` | `ebay-seller-about` | `GET /ebay/seller/{seller}/about` | `seller` (path String required) | `ApiKeyAuth` | `EbaySellerAboutResponse` |  |
| ebay | `ebay.seller_feedback` | `ebay-seller-feedback` | `GET /ebay/seller/{seller}/feedback` | `seller` (path String required)<br>`page` (query i64)<br>`per_page` (query String enum{24, 48, 72}) | `ApiKeyAuth` | `EbaySellerFeedbackResponse` |  |
| ebay | `ebay.seller_shop` | `ebay-seller-shop` | `GET /ebay/seller/{seller}/shop` | `seller` (path String required)<br>`page` (query i64) | `ApiKeyAuth` | `EbaySellerShopResponse` |  |
