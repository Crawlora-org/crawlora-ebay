import { EbayClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new EbayClient({ apiKey });

  const seller = await client.seller({ seller: "musicmagpie" });
  console.log("seller", seller);
  const search = await client.search({ option: {"keyword": "vintage camera"} });
  console.log("search", search);
