import { EbayClient } from "../src/index.js";

const client = new EbayClient({ apiKey: "test-key" });
void client.item({"item_id": "sample"});
void client.request("ebay-item", {"item_id": "sample"});
const streamResponse: Promise<Response> = client.request("ebay-item", {"item_id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("ebay-item", {"item_id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.item({"item_id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("ebay-item", {"item_id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("ebay-item", {"item_id": "sample"}, { responseType: "text" });
void rawText;


void client.liveStreams();
void client.request("ebay-live-streams");
// @ts-expect-error The selected operation requires its documented params.
void client.item();
