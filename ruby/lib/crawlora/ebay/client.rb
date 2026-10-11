require "json"
require "net/http"
require "uri"

module Crawlora
  module Ebay
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"ebay-item": {"bodyParam": null, "bodyRequired": false, "id": "ebay-item", "method": "GET", "params": [{"description": "eBay item ID", "in": "path", "name": "item_id", "required": true, "type": "string", "x-example": "196435705622"}], "path": "/ebay/item/{item_id}", "pathParams": ["item_id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "ebay-live-stream": {"bodyParam": null, "bodyRequired": false, "id": "ebay-live-stream", "method": "GET", "params": [{"description": "eBay Live stream/event id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "qrJnMkM8X2hJuIf3"}], "path": "/ebay/live/streams/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "ebay-live-stream-items": {"bodyParam": null, "bodyRequired": false, "id": "ebay-live-stream-items", "method": "GET", "params": [{"description": "eBay Live stream/event id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "qrJnMkM8X2hJuIf3"}], "path": "/ebay/live/streams/{id}/items", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "ebay-live-streams": {"bodyParam": null, "bodyRequired": false, "id": "ebay-live-streams", "method": "GET", "params": [{"description": "eBay Live category channel, defaults to explore", "enum": ["explore", "IPqZx79LNuwFcSVt", "oHjQFTlZ5cYgWkjB", "l68DJtBAVZge4x4n", "2Nk3OYiOJHfXqpWG", "5quuEnjO3axyz46U", "nGpMTpm13Q86Eaoo", "sYRxeaskGmNC6xaB", "iYaYo88zN2vtQorh", "GYAbsFw6onSNloAb", "WJ9zLwYjK8njaBtN", "rALkRyk8gXHzIBR6", "DNta0sJ8Y6NXZsC9", "GU4UfBzZSF4jiteS", "IO7Oih07PtNJSWhU", "cF4xtF8z9riubmLh", "bywKDIdtxhi4hUSO"], "in": "query", "name": "category", "type": "string"}, {"description": "Pagination cursor from a previous response's next_request_number, defaults to 0", "in": "query", "name": "request_number", "type": "integer"}, {"description": "Pagination session id from a previous response's session_id", "in": "query", "name": "session_id", "type": "string"}], "path": "/ebay/live/streams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["explore", "IPqZx79LNuwFcSVt", "oHjQFTlZ5cYgWkjB", "l68DJtBAVZge4x4n", "2Nk3OYiOJHfXqpWG", "5quuEnjO3axyz46U", "nGpMTpm13Q86Eaoo", "sYRxeaskGmNC6xaB", "iYaYo88zN2vtQorh", "GYAbsFw6onSNloAb", "WJ9zLwYjK8njaBtN", "rALkRyk8gXHzIBR6", "DNta0sJ8Y6NXZsC9", "GU4UfBzZSF4jiteS", "IO7Oih07PtNJSWhU", "cF4xtF8z9riubmLh", "bywKDIdtxhi4hUSO"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "request_number", "type": "integer"}, {"in": "query", "name": "session_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "ebay-live-streams-batch": {"bodyParam": null, "bodyRequired": false, "id": "ebay-live-streams-batch", "method": "GET", "params": [{"description": "One or more eBay Live stream/event ids, up to 9. Comma-separated or repeated query values are both accepted.", "in": "query", "name": "ids", "required": true, "type": "string", "x-example": "FncRQ8VJGxKzLase"}], "path": "/ebay/live/streams/batch", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "ebay-search": {"bodyParam": "option", "bodyRequired": true, "id": "ebay-search", "method": "POST", "params": [{"description": "eBay search payload", "in": "body", "name": "option", "required": true, "schema": {"$ref": "#/definitions/ebay.SearchOption"}}], "path": "/ebay/search", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "ebay-seller": {"bodyParam": null, "bodyRequired": false, "id": "ebay-seller", "method": "GET", "params": [{"description": "eBay seller username", "in": "path", "name": "seller", "required": true, "type": "string", "x-example": "poloblade"}], "path": "/ebay/seller/{seller}", "pathParams": ["seller"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "ebay-seller-about": {"bodyParam": null, "bodyRequired": false, "id": "ebay-seller-about", "method": "GET", "params": [{"description": "eBay seller username", "in": "path", "name": "seller", "required": true, "type": "string", "x-example": "poloblade"}], "path": "/ebay/seller/{seller}/about", "pathParams": ["seller"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "ebay-seller-feedback": {"bodyParam": null, "bodyRequired": false, "id": "ebay-seller-feedback", "method": "GET", "params": [{"description": "eBay seller username", "in": "path", "name": "seller", "required": true, "type": "string", "x-example": "poloblade"}, {"default": 1, "description": "Feedback page number", "in": "query", "name": "page", "type": "integer"}, {"default": 48, "description": "Reviews per page", "enum": [24, 48, 72], "in": "query", "name": "per_page", "type": "integer"}], "path": "/ebay/seller/{seller}/feedback", "pathParams": ["seller"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}, {"enum": ["24", "48", "72"], "in": "query", "name": "per_page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "ebay-seller-shop": {"bodyParam": null, "bodyRequired": false, "id": "ebay-seller-shop", "method": "GET", "params": [{"description": "eBay seller username", "in": "path", "name": "seller", "required": true, "type": "string", "x-example": "poloblade"}, {"default": 1, "description": "Shop page number", "in": "query", "name": "page", "type": "integer"}], "path": "/ebay/seller/{seller}/shop", "pathParams": ["seller"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["ebay-item", "ebay-live-stream", "ebay-live-stream-items", "ebay-live-streams", "ebay-live-streams-batch", "ebay-search", "ebay-seller", "ebay-seller-about", "ebay-seller-feedback", "ebay-seller-shop"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-ebay-ruby/0.1.1", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('item') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-item', params, response_type: response_type)
      end
      define_method('live_streams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-live-streams', params, response_type: response_type)
      end
      define_method('live_streams_batch') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-live-streams-batch', params, response_type: response_type)
      end
      define_method('live_stream') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-live-stream', params, response_type: response_type)
      end
      define_method('live_stream_items') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-live-stream-items', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-search', params, response_type: response_type)
      end
      define_method('seller') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-seller', params, response_type: response_type)
      end
      define_method('seller_about') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-seller-about', params, response_type: response_type)
      end
      define_method('seller_feedback') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-seller-feedback', params, response_type: response_type)
      end
      define_method('seller_shop') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('ebay-seller-shop', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
