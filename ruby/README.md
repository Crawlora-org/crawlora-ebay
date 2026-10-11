# Crawlora eBay API client for Ruby (`crawlora-ebay`)

This Ruby gem calls Crawlora's hosted eBay API at `https://api.crawlora.net/api/v1`. It exposes 10 endpoints covering listing search, item details, seller profiles, feedback and shops, and eBay Live streams; it does not call or scrape eBay directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-ebay"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/ebay"

client = Crawlora::Ebay::Client.new
result = client.request("ebay-item", JSON.parse("{\"item_id\": \"sample-id\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 10 API operations.

```ruby
client = Crawlora::Ebay::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported eBay API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-ebay/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-ebay) for account setup, the API operation reference, and release history.
