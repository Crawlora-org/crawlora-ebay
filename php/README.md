# Crawlora eBay API client for PHP (`crawlora/ebay`)

This PHP package calls Crawlora's hosted eBay API at `https://api.crawlora.net/api/v1`. It exposes 10 endpoints covering listing search, item details, seller profiles, feedback and shops, and eBay Live streams. It does not call or scrape eBay directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/ebay
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Ebay\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("ebay-item", ['item_id' => 'sample-id']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 10 API operations.

## Supported eBay API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-ebay/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-ebay). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-ebay/blob/main/docs/usage.md).
