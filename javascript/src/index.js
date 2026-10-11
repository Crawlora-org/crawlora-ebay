import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class EbayClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-ebay-js/0.1.0" });
    this["item"] = (...args) => this.request("ebay-item", ...args);
    this["liveStreams"] = (...args) => this.request("ebay-live-streams", ...args);
    this["liveStreamsBatch"] = (...args) => this.request("ebay-live-streams-batch", ...args);
    this["liveStream"] = (...args) => this.request("ebay-live-stream", ...args);
    this["liveStreamItems"] = (...args) => this.request("ebay-live-stream-items", ...args);
    this["search"] = (...args) => this.request("ebay-search", ...args);
    this["seller"] = (...args) => this.request("ebay-seller", ...args);
    this["sellerAbout"] = (...args) => this.request("ebay-seller-about", ...args);
    this["sellerFeedback"] = (...args) => this.request("ebay-seller-feedback", ...args);
    this["sellerShop"] = (...args) => this.request("ebay-seller-shop", ...args);
  }
}

export { EbayClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default EbayClient;
