# eBay API endpoint reference and client usage

This reference lists all 10 public eBay API endpoints exposed by the `@crawlora-org/ebay` and `crawlora-ebay` packages, covering listing search, item details, seller profiles, feedback and shops, and eBay Live streams. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape eBay locally; Crawlora is independent from and not endorsed by eBay or its owners.

The package tracks the public API contract revision `sha256:e8514c916185f6508e01cf9bf5e07d3d39d49886c8da797ec56300d167e65268` bundled with release `0.1.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 10 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `ebay` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `item` / `item` | `GET /ebay/item/{item_id}` | `item_id` (path, required) | Get eBay item details |
| `liveStream` / `live_stream` | `GET /ebay/live/streams/{id}` | `id` (path, required) | Get an eBay Live stream |
| `liveStreamItems` / `live_stream_items` | `GET /ebay/live/streams/{id}/items` | `id` (path, required) | List an eBay Live stream's featured items |
| `liveStreams` / `live_streams` | `GET /ebay/live/streams` | `category` (query, optional; values: `explore`, `IPqZx79LNuwFcSVt`, `oHjQFTlZ5cYgWkjB`, `l68DJtBAVZge4x4n`, `2Nk3OYiOJHfXqpWG`, `5quuEnjO3axyz46U`, `nGpMTpm13Q86Eaoo`, `sYRxeaskGmNC6xaB`, `iYaYo88zN2vtQorh`, `GYAbsFw6onSNloAb`, `WJ9zLwYjK8njaBtN`, `rALkRyk8gXHzIBR6`, `DNta0sJ8Y6NXZsC9`, `GU4UfBzZSF4jiteS`, `IO7Oih07PtNJSWhU`, `cF4xtF8z9riubmLh`, `bywKDIdtxhi4hUSO`), `request_number` (query, optional), `session_id` (query, optional) | List eBay Live streams |
| `liveStreamsBatch` / `live_streams_batch` | `GET /ebay/live/streams/batch` | `ids` (query, required) | Get multiple eBay Live streams |
| `search` / `search` | `POST /ebay/search` | `option` (body, required) | Search eBay listings |
| `seller` / `seller` | `GET /ebay/seller/{seller}` | `seller` (path, required) | Get eBay seller profile |
| `sellerAbout` / `seller_about` | `GET /ebay/seller/{seller}/about` | `seller` (path, required) | Get eBay seller about details |
| `sellerFeedback` / `seller_feedback` | `GET /ebay/seller/{seller}/feedback` | `seller` (path, required), `page` (query, optional), `per_page` (query, optional; values: `24`, `48`, `72`) | Get eBay seller feedback |
| `sellerShop` / `seller_shop` | `GET /ebay/seller/{seller}/shop` | `seller` (path, required), `page` (query, optional) | Get eBay seller shop listings |

## Client forms

- JavaScript: import `EbayClient` (also exported as `Client`) from `@crawlora-org/ebay`; use `new EbayClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `EbayClient` (also exported as `Client`) from `crawlora_ebay`; use `with EbayClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncEbayClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
