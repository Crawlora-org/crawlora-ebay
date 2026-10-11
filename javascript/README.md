# @crawlora-org/ebay — eBay API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted eBay API.
It exposes 10 API endpoints for listing search, item details, seller profiles, feedback and shops, and eBay Live streams through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-javascript-homepage). It does not run a browser or scrape eBay locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by eBay or its owners.

## Install

```sh
npm install @crawlora-org/ebay
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { EbayClient } from "@crawlora-org/ebay";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new EbayClient({ apiKey });
const result1 = await client.seller({ seller: "musicmagpie" });
console.log(result1);
const result2 = await client.search({ option: {"keyword": "vintage camera"} });
console.log(result2);
```

The client also exports `Client` as an alias for `EbayClient`. Operation
methods are available directly in camelCase and through the `ebay`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-ebay/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-ebay/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported eBay API endpoints

This package exposes each route below as a direct method and through the `ebay` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-ebay/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
