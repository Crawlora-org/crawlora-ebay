# Crawlora eBay API client for Java

The official Java client for Crawlora's hosted eBay API. It exposes 10 endpoints covering listing search, item details, seller profiles, feedback and shops, and eBay Live streams. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-ebay</artifactId>
  <version>0.1.1</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-java-console) to get an API key.

```java
import net.crawlora.ebay.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.seller(Map.ofEntries(Map.entry("seller", "musicmagpie")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported eBay API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-ebay/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-ebay)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=ebay-java-api-docs)
