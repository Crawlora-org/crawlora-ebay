package net.crawlora.ebay;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the eBay endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 10;
    public static final List<String> OPERATION_IDS = List.of(
            "ebay-item",
            "ebay-live-stream",
            "ebay-live-stream-items",
            "ebay-live-streams",
            "ebay-live-streams-batch",
            "ebay-search",
            "ebay-seller",
            "ebay-seller-about",
            "ebay-seller-feedback",
            "ebay-seller-shop"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("ebay-item", new Operation("ebay-item", "GET", "/ebay/item/{item_id}", Map.ofEntries(Map.entry("item_id", new Param("item_id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("ebay-live-streams", new Operation("ebay-live-streams", "GET", "/ebay/live/streams", Map.ofEntries(Map.entry("category", new Param("category", "query", false, "string", List.of("explore", "IPqZx79LNuwFcSVt", "oHjQFTlZ5cYgWkjB", "l68DJtBAVZge4x4n", "2Nk3OYiOJHfXqpWG", "5quuEnjO3axyz46U", "nGpMTpm13Q86Eaoo", "sYRxeaskGmNC6xaB", "iYaYo88zN2vtQorh", "GYAbsFw6onSNloAb", "WJ9zLwYjK8njaBtN", "rALkRyk8gXHzIBR6", "DNta0sJ8Y6NXZsC9", "GU4UfBzZSF4jiteS", "IO7Oih07PtNJSWhU", "cF4xtF8z9riubmLh", "bywKDIdtxhi4hUSO"), "csv")), Map.entry("request_number", new Param("request_number", "query", false, "integer", List.of(), "csv")), Map.entry("session_id", new Param("session_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("ebay-live-streams-batch", new Operation("ebay-live-streams-batch", "GET", "/ebay/live/streams/batch", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("ebay-live-stream", new Operation("ebay-live-stream", "GET", "/ebay/live/streams/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("ebay-live-stream-items", new Operation("ebay-live-stream-items", "GET", "/ebay/live/streams/{id}/items", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("ebay-search", new Operation("ebay-search", "POST", "/ebay/search", Map.of(), List.of("application/json"), "option"));
        operations.put("ebay-seller", new Operation("ebay-seller", "GET", "/ebay/seller/{seller}", Map.ofEntries(Map.entry("seller", new Param("seller", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("ebay-seller-about", new Operation("ebay-seller-about", "GET", "/ebay/seller/{seller}/about", Map.ofEntries(Map.entry("seller", new Param("seller", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("ebay-seller-feedback", new Operation("ebay-seller-feedback", "GET", "/ebay/seller/{seller}/feedback", Map.ofEntries(Map.entry("seller", new Param("seller", "path", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("per_page", new Param("per_page", "query", false, "integer", List.of("24", "48", "72"), "csv"))), List.of("application/json")));
        operations.put("ebay-seller-shop", new Operation("ebay-seller-shop", "GET", "/ebay/seller/{seller}/shop", Map.ofEntries(Map.entry("seller", new Param("seller", "path", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown eBay operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object item(Map<String, ?> params) { return request("ebay-item", params); }
    public Object liveStreams(Map<String, ?> params) { return request("ebay-live-streams", params); }
    public Object liveStreamsBatch(Map<String, ?> params) { return request("ebay-live-streams-batch", params); }
    public Object liveStream(Map<String, ?> params) { return request("ebay-live-stream", params); }
    public Object liveStreamItems(Map<String, ?> params) { return request("ebay-live-stream-items", params); }
    public Object search(Map<String, ?> params) { return request("ebay-search", params); }
    public Object seller(Map<String, ?> params) { return request("ebay-seller", params); }
    public Object sellerAbout(Map<String, ?> params) { return request("ebay-seller-about", params); }
    public Object sellerFeedback(Map<String, ?> params) { return request("ebay-seller-feedback", params); }
    public Object sellerShop(Map<String, ?> params) { return request("ebay-seller-shop", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
