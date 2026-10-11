import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class EbayClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  item(params: OperationParamsMap["ebay-item"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveStreams(params?: OperationParamsMap["ebay-live-streams"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveStreamsBatch(params: OperationParamsMap["ebay-live-streams-batch"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveStream(params: OperationParamsMap["ebay-live-stream"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveStreamItems(params: OperationParamsMap["ebay-live-stream-items"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["ebay-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  seller(params: OperationParamsMap["ebay-seller"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sellerAbout(params: OperationParamsMap["ebay-seller-about"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sellerFeedback(params: OperationParamsMap["ebay-seller-feedback"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sellerShop(params: OperationParamsMap["ebay-seller-shop"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  item(params: OperationParamsMap["ebay-item"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveStreams(params?: OperationParamsMap["ebay-live-streams"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveStreamsBatch(params: OperationParamsMap["ebay-live-streams-batch"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveStream(params: OperationParamsMap["ebay-live-stream"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveStreamItems(params: OperationParamsMap["ebay-live-stream-items"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["ebay-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  seller(params: OperationParamsMap["ebay-seller"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sellerAbout(params: OperationParamsMap["ebay-seller-about"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sellerFeedback(params: OperationParamsMap["ebay-seller-feedback"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sellerShop(params: OperationParamsMap["ebay-seller-shop"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  item(...args: OperationRequestArgs<"ebay-item">): Promise<OperationResponseMap["ebay-item"]>;
  liveStreams(...args: OperationRequestArgs<"ebay-live-streams">): Promise<OperationResponseMap["ebay-live-streams"]>;
  liveStreamsBatch(...args: OperationRequestArgs<"ebay-live-streams-batch">): Promise<OperationResponseMap["ebay-live-streams-batch"]>;
  liveStream(...args: OperationRequestArgs<"ebay-live-stream">): Promise<OperationResponseMap["ebay-live-stream"]>;
  liveStreamItems(...args: OperationRequestArgs<"ebay-live-stream-items">): Promise<OperationResponseMap["ebay-live-stream-items"]>;
  search(...args: OperationRequestArgs<"ebay-search">): Promise<OperationResponseMap["ebay-search"]>;
  seller(...args: OperationRequestArgs<"ebay-seller">): Promise<OperationResponseMap["ebay-seller"]>;
  sellerAbout(...args: OperationRequestArgs<"ebay-seller-about">): Promise<OperationResponseMap["ebay-seller-about"]>;
  sellerFeedback(...args: OperationRequestArgs<"ebay-seller-feedback">): Promise<OperationResponseMap["ebay-seller-feedback"]>;
  sellerShop(...args: OperationRequestArgs<"ebay-seller-shop">): Promise<OperationResponseMap["ebay-seller-shop"]>;
}
export { EbayClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default EbayClient;
