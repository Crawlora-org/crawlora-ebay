# eBay API endpoint reference and client usage

This reference lists all 10 public eBay API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/ebay`, `crawlora-ebay`, and `crawlora-ebay` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape eBay locally; Crawlora is independent from and not endorsed by eBay or its owners.

The package tracks the public API contract revision `sha256:50b2e34ad52f6fe505511c8f638f9d59682bc7dc9e4cf474f44b17feb2a6aaae` bundled with release `0.1.2`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `ebay`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `item` | `item` | `ebay.item` | `GET /ebay/item/{item_id}` | `item_id` (path, required) | Get eBay item details |
| `liveStream` | `live_stream` | `ebay.live_stream` | `GET /ebay/live/streams/{id}` | `id` (path, required) | Get an eBay Live stream |
| `liveStreamItems` | `live_stream_items` | `ebay.live_stream_items` | `GET /ebay/live/streams/{id}/items` | `id` (path, required) | List an eBay Live stream's featured items |
| `liveStreams` | `live_streams` | `ebay.live_streams` | `GET /ebay/live/streams` | `category` (query, optional; values: `explore`, `IPqZx79LNuwFcSVt`, `oHjQFTlZ5cYgWkjB`, `l68DJtBAVZge4x4n`, `2Nk3OYiOJHfXqpWG`, `5quuEnjO3axyz46U`, `nGpMTpm13Q86Eaoo`, `sYRxeaskGmNC6xaB`, `iYaYo88zN2vtQorh`, `GYAbsFw6onSNloAb`, `WJ9zLwYjK8njaBtN`, `rALkRyk8gXHzIBR6`, `DNta0sJ8Y6NXZsC9`, `GU4UfBzZSF4jiteS`, `IO7Oih07PtNJSWhU`, `cF4xtF8z9riubmLh`, `bywKDIdtxhi4hUSO`), `request_number` (query, optional), `session_id` (query, optional) | List eBay Live streams |
| `liveStreamsBatch` | `live_streams_batch` | `ebay.live_streams_batch` | `GET /ebay/live/streams/batch` | `ids` (query, required) | Get multiple eBay Live streams |
| `search` | `search` | `ebay.search` | `POST /ebay/search` | `option` (body, required) | Search eBay listings |
| `seller` | `seller` | `ebay.seller` | `GET /ebay/seller/{seller}` | `seller` (path, required) | Get eBay seller profile |
| `sellerAbout` | `seller_about` | `ebay.seller_about` | `GET /ebay/seller/{seller}/about` | `seller` (path, required) | Get eBay seller about details |
| `sellerFeedback` | `seller_feedback` | `ebay.seller_feedback` | `GET /ebay/seller/{seller}/feedback` | `seller` (path, required), `page` (query, optional), `per_page` (query, optional; values: `24`, `48`, `72`) | Get eBay seller feedback |
| `sellerShop` | `seller_shop` | `ebay.seller_shop` | `GET /ebay/seller/{seller}/shop` | `seller` (path, required), `page` (query, optional) | Get eBay seller shop listings |

## Client forms

- JavaScript: import `EbayClient` (also exported as `Client`) from `@crawlora-org/ebay`; use `new EbayClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `EbayClient` (also exported as `Client`) from `crawlora_ebay`; use `with EbayClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncEbayClient`, used with `async with` and `await`.
- Rust: add `crawlora-ebay` with Cargo; import `Client` and the generated operation parameter struct, then call `client.ebay.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-ebay/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
