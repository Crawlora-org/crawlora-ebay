# eBay clients for Crawlora

Official Crawlora client packages for the hosted eBay API. Access 10 API endpoints covering listing search, item details, seller profiles, feedback and shops, and eBay Live streams from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape eBay locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by eBay or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/ebay`](javascript/README.md)
- Python: [`crawlora-ebay`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-ebay`](go.mod)
- Ruby: [`crawlora-ebay`](ruby/README.md)
- Java: [`net.crawlora:crawlora-ebay:0.1.2`](java/README.md)
- PHP: [`crawlora/ebay`](php/README.md)
- Rust: [`crawlora-ebay`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 10 selected public eBay API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/ebay/item/{item_id}` | `ebay-item` | Get eBay item details |
| `GET` | `/ebay/live/streams` | `ebay-live-streams` | List eBay Live streams |
| `GET` | `/ebay/live/streams/batch` | `ebay-live-streams-batch` | Get multiple eBay Live streams |
| `GET` | `/ebay/live/streams/{id}` | `ebay-live-stream` | Get an eBay Live stream |
| `GET` | `/ebay/live/streams/{id}/items` | `ebay-live-stream-items` | List an eBay Live stream's featured items |
| `POST` | `/ebay/search` | `ebay-search` | Search eBay listings |
| `GET` | `/ebay/seller/{seller}` | `ebay-seller` | Get eBay seller profile |
| `GET` | `/ebay/seller/{seller}/about` | `ebay-seller-about` | Get eBay seller about details |
| `GET` | `/ebay/seller/{seller}/feedback` | `ebay-seller-feedback` | Get eBay seller feedback |
| `GET` | `/ebay/seller/{seller}/shop` | `ebay-seller-shop` | Get eBay seller shop listings |

## License

MIT. See [LICENSE](LICENSE).
