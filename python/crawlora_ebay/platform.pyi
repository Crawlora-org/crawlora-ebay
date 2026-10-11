from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySellerShopResponseDoc = TypedDict('ModelEbaySellerShopResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySearchResp],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySearchResp = TypedDict('ModelEbaySearchResp', {
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'result': NotRequired[list[ModelEbaySearchItem]],
    'total': NotRequired[int],
}, total=False)

ModelEbaySearchItem = TypedDict('ModelEbaySearchItem', {
    'bid_count': NotRequired[int],
    'caption': NotRequired[str],
    'image': NotRequired[str],
    'is_authenticity_guaranteed': NotRequired[bool],
    'item_id': NotRequired[str],
    'link': NotRequired[str],
    'location': NotRequired[str],
    'logistic': NotRequired[str],
    'offer_note': NotRequired[str],
    'price': NotRequired[float],
    'price_from': NotRequired[float],
    'price_to': NotRequired[float],
    'rating': NotRequired[float],
    'rating_num': NotRequired[int],
    'seller': NotRequired[str],
    'sold_count': NotRequired[int],
    'sub_title': NotRequired[str],
    'title': NotRequired[str],
    'watcher_count': NotRequired[int],
}, total=False)

ModelEbaySellerFeedbackResponseDoc = TypedDict('ModelEbaySellerFeedbackResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySellerFeedback],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySellerFeedback = TypedDict('ModelEbaySellerFeedback', {
    'description': NotRequired[str],
    'detailed_seller_ratings': NotRequired[dict[str, float]],
    'followers': NotRequired[int],
    'has_more': NotRequired[bool],
    'items_sold': NotRequired[int],
    'next_page': NotRequired[int],
    'overall_rating_summary': NotRequired[dict[str, int]],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
    'positive_feedback_percent': NotRequired[float],
    'reviews': NotRequired[list[ModelEbaySellerReview]],
    'seller': NotRequired[str],
    'store_name': NotRequired[str],
    'store_url': NotRequired[str],
    'total_feedback_count': NotRequired[int],
}, total=False)

ModelEbaySellerReview = TypedDict('ModelEbaySellerReview', {
    'buyer': NotRequired[str],
    'buyer_feedback': NotRequired[int],
    'comment': NotRequired[str],
    'period': NotRequired[str],
    'rating': NotRequired[str],
    'verified_purchase': NotRequired[bool],
}, total=False)

ModelEbaySellerAboutResponseDoc = TypedDict('ModelEbaySellerAboutResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySellerAbout],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySellerAbout = TypedDict('ModelEbaySellerAbout', {
    'banner_url': NotRequired[str],
    'categories': NotRequired[list[ModelEbaySellerAboutCategory]],
    'contact_seller_url': NotRequired[str],
    'description': NotRequired[str],
    'followers': NotRequired[int],
    'items_sold': NotRequired[int],
    'location': NotRequired[str],
    'logo_url': NotRequired[str],
    'member_since': NotRequired[str],
    'positive_feedback_percent': NotRequired[float],
    'seller': NotRequired[str],
    'store_name': NotRequired[str],
    'store_url': NotRequired[str],
    'top_rated_seller': NotRequired[bool],
    'top_rated_seller_summary': NotRequired[str],
}, total=False)

ModelEbaySellerAboutCategory = TypedDict('ModelEbaySellerAboutCategory', {
    'name': NotRequired[str],
    'subcategories': NotRequired[list[ModelEbaySellerAboutSubcategory]],
    'url': NotRequired[str],
}, total=False)

ModelEbaySellerAboutSubcategory = TypedDict('ModelEbaySellerAboutSubcategory', {
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelEbaySellerResponseDoc = TypedDict('ModelEbaySellerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySeller],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySeller = TypedDict('ModelEbaySeller', {
    'description': NotRequired[str],
    'detailed_seller_ratings': NotRequired[dict[str, float]],
    'display_name': NotRequired[str],
    'feedback_count': NotRequired[int],
    'feedback_summary': NotRequired[dict[str, int]],
    'followers': NotRequired[int],
    'items_sold': NotRequired[int],
    'location': NotRequired[str],
    'member_since': NotRequired[str],
    'positive_feedback_percent': NotRequired[float],
    'profile_url': NotRequired[str],
    'seller': NotRequired[str],
    'store_name': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelEbaySearchResponseDoc = TypedDict('ModelEbaySearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySearchResp],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySearchOption = TypedDict('ModelEbaySearchOption', {
    'keyword': Required[str],
    'limit': NotRequired[Literal['60', '120', '240']],
    'listing_type': NotRequired[Literal['active', 'sold', 'completed', 'sold_completed']],
    'page': NotRequired[int],
}, total=False)

ModelEbayLiveStreamItemsResponseDoc = TypedDict('ModelEbayLiveStreamItemsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbayLiveStreamItemsResp],
    'msg': NotRequired[Any],
}, total=False)

ModelEbayLiveStreamItemsResp = TypedDict('ModelEbayLiveStreamItemsResp', {
    'event_id': NotRequired[str],
    'items': NotRequired[list[ModelEbayLiveStreamItem]],
    'next_cursor': NotRequired[str],
}, total=False)

ModelEbayLiveStreamItem = TypedDict('ModelEbayLiveStreamItem', {
    'auction_currency': NotRequired[str],
    'auction_ending_at': NotRequired[str],
    'auction_price': NotRequired[float],
    'auction_status': NotRequired[str],
    'bid_count': NotRequired[int],
    'currency': NotRequired[str],
    'end_date': NotRequired[str],
    'image_url': NotRequired[str],
    'is_exclusive': NotRequired[bool],
    'is_visible': NotRequired[bool],
    'leader_username': NotRequired[str],
    'listing_id': NotRequired[str],
    'pin': NotRequired[bool],
    'price': NotRequired[float],
    'purchasable': NotRequired[bool],
    'sale_type': NotRequired[str],
    'status': NotRequired[str],
    'title': NotRequired[str],
    'winner_username': NotRequired[str],
}, total=False)

ModelEbayLiveStreamResponseDoc = TypedDict('ModelEbayLiveStreamResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbayLiveStreamDetail],
    'msg': NotRequired[Any],
}, total=False)

ModelEbayLiveStreamDetail = TypedDict('ModelEbayLiveStreamDetail', {
    'channels': NotRequired[list[str]],
    'concurrent_viewer_count': NotRequired[int],
    'description': NotRequired[str],
    'end_time': NotRequired[str],
    'hosts': NotRequired[list[ModelEbayLiveStreamHost]],
    'id': NotRequired[str],
    'is_case_break': NotRequired[bool],
    'is_user_registered': NotRequired[bool],
    'like_count': NotRequired[int],
    'live_stream_url': NotRequired[str],
    'preview_image_url': NotRequired[str],
    'preview_stream_url': NotRequired[str],
    'replay_url': NotRequired[str],
    'site_id': NotRequired[str],
    'start_time': NotRequired[str],
    'state': NotRequired[str],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'vendor_event_id': NotRequired[str],
    'watched_count': NotRequired[int],
}, total=False)

ModelEbayLiveStreamHost = TypedDict('ModelEbayLiveStreamHost', {
    'communication_rating': NotRequired[float],
    'feedback_negative_count': NotRequired[int],
    'feedback_neutral_count': NotRequired[int],
    'feedback_positive_count': NotRequired[int],
    'feedback_positive_percent': NotRequired[float],
    'id': NotRequired[str],
    'item_as_described_rating': NotRequired[float],
    'profile_picture_url': NotRequired[str],
    'shipping_cost_rating': NotRequired[float],
    'shipping_time_rating': NotRequired[float],
    'store_name': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelEbayLiveStreamsBatchResponseDoc = TypedDict('ModelEbayLiveStreamsBatchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbayLiveStreamsBatchResp],
    'msg': NotRequired[Any],
}, total=False)

ModelEbayLiveStreamsBatchResp = TypedDict('ModelEbayLiveStreamsBatchResp', {
    'streams': NotRequired[list[ModelEbayLiveStream]],
}, total=False)

ModelEbayLiveStream = TypedDict('ModelEbayLiveStream', {
    'channels': NotRequired[list[str]],
    'description': NotRequired[str],
    'end_time': NotRequired[str],
    'hosts': NotRequired[list[ModelEbayLiveStreamHost]],
    'id': NotRequired[str],
    'is_case_break': NotRequired[bool],
    'is_user_registered': NotRequired[bool],
    'like_count': NotRequired[int],
    'live_stream_url': NotRequired[str],
    'preview_image_url': NotRequired[str],
    'preview_stream_url': NotRequired[str],
    'start_time': NotRequired[str],
    'state': NotRequired[str],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'watched_count': NotRequired[int],
}, total=False)

ModelEbayLiveStreamsResponseDoc = TypedDict('ModelEbayLiveStreamsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbayLiveStreamsResp],
    'msg': NotRequired[Any],
}, total=False)

ModelEbayLiveStreamsResp = TypedDict('ModelEbayLiveStreamsResp', {
    'category': NotRequired[str],
    'next_request_number': NotRequired[int],
    'session_id': NotRequired[str],
    'streams': NotRequired[list[ModelEbayLiveStream]],
}, total=False)

ModelEbayItemResponseDoc = TypedDict('ModelEbayItemResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbayItem],
    'msg': NotRequired[Any],
}, total=False)

ModelEbayItem = TypedDict('ModelEbayItem', {
    'availability': NotRequired[str],
    'condition': NotRequired[str],
    'description': NotRequired[str],
    'images': NotRequired[list[str]],
    'item_feedback_count': NotRequired[int],
    'item_id': NotRequired[str],
    'item_specifics': NotRequired[dict[str, str]],
    'link': NotRequired[str],
    'location': NotRequired[str],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'rating': NotRequired[float],
    'rating_count': NotRequired[int],
    'sale_status': NotRequired[str],
    'seller_categories': NotRequired[list[str]],
    'seller_description': NotRequired[str],
    'seller_detailed_ratings': NotRequired[dict[str, float]],
    'seller_feedback_score': NotRequired[int],
    'seller_followers': NotRequired[int],
    'seller_items_sold': NotRequired[int],
    'seller_link': NotRequired[str],
    'seller_logo_url': NotRequired[str],
    'seller_member_since': NotRequired[str],
    'seller_name': NotRequired[str],
    'seller_positive_feedback': NotRequired[float],
    'seller_store_name': NotRequired[str],
    'seller_total_feedback_count': NotRequired[int],
    'shipping': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

EbayItemResponse = ModelEbayItemResponseDoc
EbayItemParams = TypedDict('EbayItemParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'item_id': Required[str],
}, total=False)

EbayLiveStreamsResponse = ModelEbayLiveStreamsResponseDoc
EbayLiveStreamsParams = TypedDict('EbayLiveStreamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['explore', 'IPqZx79LNuwFcSVt', 'oHjQFTlZ5cYgWkjB', 'l68DJtBAVZge4x4n', '2Nk3OYiOJHfXqpWG', '5quuEnjO3axyz46U', 'nGpMTpm13Q86Eaoo', 'sYRxeaskGmNC6xaB', 'iYaYo88zN2vtQorh', 'GYAbsFw6onSNloAb', 'WJ9zLwYjK8njaBtN', 'rALkRyk8gXHzIBR6', 'DNta0sJ8Y6NXZsC9', 'GU4UfBzZSF4jiteS', 'IO7Oih07PtNJSWhU', 'cF4xtF8z9riubmLh', 'bywKDIdtxhi4hUSO']],
    'request_number': NotRequired[int],
    'session_id': NotRequired[str],
}, total=False)

EbayLiveStreamsBatchResponse = ModelEbayLiveStreamsBatchResponseDoc
EbayLiveStreamsBatchParams = TypedDict('EbayLiveStreamsBatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
}, total=False)

EbayLiveStreamResponse = ModelEbayLiveStreamResponseDoc
EbayLiveStreamParams = TypedDict('EbayLiveStreamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

EbayLiveStreamItemsResponse = ModelEbayLiveStreamItemsResponseDoc
EbayLiveStreamItemsParams = TypedDict('EbayLiveStreamItemsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

EbaySearchBody = ModelEbaySearchOption
EbaySearchResponse = ModelEbaySearchResponseDoc
EbaySearchParams = TypedDict('EbaySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'option': Required[EbaySearchBody],
}, total=False)

EbaySellerResponse = ModelEbaySellerResponseDoc
EbaySellerParams = TypedDict('EbaySellerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
}, total=False)

EbaySellerAboutResponse = ModelEbaySellerAboutResponseDoc
EbaySellerAboutParams = TypedDict('EbaySellerAboutParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
}, total=False)

EbaySellerFeedbackResponse = ModelEbaySellerFeedbackResponseDoc
EbaySellerFeedbackParams = TypedDict('EbaySellerFeedbackParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
    'page': NotRequired[int],
    'per_page': NotRequired[Literal['24', '48', '72']],
}, total=False)

EbaySellerShopResponse = ModelEbaySellerShopResponseDoc
EbaySellerShopParams = TypedDict('EbaySellerShopParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
    'page': NotRequired[int],
}, total=False)

class EbayGroup:
    @overload
    def item(self, **params: Unpack[EbayItemStreamParams]) -> BinaryIO: ...
    @overload
    def item(self, **params: Unpack[EbayItemTextResponseParams]) -> str: ...
    @overload
    def item(self, **params: Unpack[EbayItemDefaultParams]) -> EbayItemResponse: ...
    @overload
    def live_streams(self, **params: Unpack[EbayLiveStreamsStreamParams]) -> BinaryIO: ...
    @overload
    def live_streams(self, **params: Unpack[EbayLiveStreamsTextResponseParams]) -> str: ...
    @overload
    def live_streams(self, **params: Unpack[EbayLiveStreamsDefaultParams]) -> EbayLiveStreamsResponse: ...
    @overload
    def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchStreamParams]) -> BinaryIO: ...
    @overload
    def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchTextResponseParams]) -> str: ...
    @overload
    def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchDefaultParams]) -> EbayLiveStreamsBatchResponse: ...
    @overload
    def live_stream(self, **params: Unpack[EbayLiveStreamStreamParams]) -> BinaryIO: ...
    @overload
    def live_stream(self, **params: Unpack[EbayLiveStreamTextResponseParams]) -> str: ...
    @overload
    def live_stream(self, **params: Unpack[EbayLiveStreamDefaultParams]) -> EbayLiveStreamResponse: ...
    @overload
    def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsStreamParams]) -> BinaryIO: ...
    @overload
    def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsTextResponseParams]) -> str: ...
    @overload
    def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsDefaultParams]) -> EbayLiveStreamItemsResponse: ...
    @overload
    def search(self, **params: Unpack[EbaySearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[EbaySearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[EbaySearchDefaultParams]) -> EbaySearchResponse: ...
    @overload
    def seller(self, **params: Unpack[EbaySellerStreamParams]) -> BinaryIO: ...
    @overload
    def seller(self, **params: Unpack[EbaySellerTextResponseParams]) -> str: ...
    @overload
    def seller(self, **params: Unpack[EbaySellerDefaultParams]) -> EbaySellerResponse: ...
    @overload
    def seller_about(self, **params: Unpack[EbaySellerAboutStreamParams]) -> BinaryIO: ...
    @overload
    def seller_about(self, **params: Unpack[EbaySellerAboutTextResponseParams]) -> str: ...
    @overload
    def seller_about(self, **params: Unpack[EbaySellerAboutDefaultParams]) -> EbaySellerAboutResponse: ...
    @overload
    def seller_feedback(self, **params: Unpack[EbaySellerFeedbackStreamParams]) -> BinaryIO: ...
    @overload
    def seller_feedback(self, **params: Unpack[EbaySellerFeedbackTextResponseParams]) -> str: ...
    @overload
    def seller_feedback(self, **params: Unpack[EbaySellerFeedbackDefaultParams]) -> EbaySellerFeedbackResponse: ...
    @overload
    def seller_shop(self, **params: Unpack[EbaySellerShopStreamParams]) -> BinaryIO: ...
    @overload
    def seller_shop(self, **params: Unpack[EbaySellerShopTextResponseParams]) -> str: ...
    @overload
    def seller_shop(self, **params: Unpack[EbaySellerShopDefaultParams]) -> EbaySellerShopResponse: ...

OperationId = Literal[
    'ebay-item',
    'ebay-live-streams',
    'ebay-live-streams-batch',
    'ebay-live-stream',
    'ebay-live-stream-items',
    'ebay-search',
    'ebay-seller',
    'ebay-seller-about',
    'ebay-seller-feedback',
    'ebay-seller-shop',
]

class CrawloraClient:
    ebay: EbayGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-item'],
        params: EbayItemParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayItemResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-live-streams'],
        params: EbayLiveStreamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayLiveStreamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-live-streams-batch'],
        params: EbayLiveStreamsBatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayLiveStreamsBatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-live-stream'],
        params: EbayLiveStreamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayLiveStreamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-live-stream-items'],
        params: EbayLiveStreamItemsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayLiveStreamItemsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-search'],
        params: EbaySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-seller'],
        params: EbaySellerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySellerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-seller-about'],
        params: EbaySellerAboutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySellerAboutResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-seller-feedback'],
        params: EbaySellerFeedbackParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySellerFeedbackResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-seller-shop'],
        params: EbaySellerShopParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySellerShopResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-item'],
        params: EbayItemParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayItemResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-live-streams'],
        params: EbayLiveStreamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayLiveStreamsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-live-streams-batch'],
        params: EbayLiveStreamsBatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayLiveStreamsBatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-live-stream'],
        params: EbayLiveStreamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayLiveStreamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-live-stream-items'],
        params: EbayLiveStreamItemsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbayLiveStreamItemsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-search'],
        params: EbaySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-seller'],
        params: EbaySellerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySellerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-seller-about'],
        params: EbaySellerAboutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySellerAboutResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-seller-feedback'],
        params: EbaySellerFeedbackParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySellerFeedbackResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-seller-shop'],
        params: EbaySellerShopParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EbaySellerShopResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class EbayClient(CrawloraClient):
    def __enter__(self) -> EbayClient: ...
    @overload
    def item(self, **params: Unpack[EbayItemStreamParams]) -> BinaryIO: ...
    @overload
    def item(self, **params: Unpack[EbayItemTextResponseParams]) -> str: ...
    @overload
    def item(self, **params: Unpack[EbayItemDefaultParams]) -> EbayItemResponse: ...
    @overload
    def live_streams(self, **params: Unpack[EbayLiveStreamsStreamParams]) -> BinaryIO: ...
    @overload
    def live_streams(self, **params: Unpack[EbayLiveStreamsTextResponseParams]) -> str: ...
    @overload
    def live_streams(self, **params: Unpack[EbayLiveStreamsDefaultParams]) -> EbayLiveStreamsResponse: ...
    @overload
    def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchStreamParams]) -> BinaryIO: ...
    @overload
    def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchTextResponseParams]) -> str: ...
    @overload
    def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchDefaultParams]) -> EbayLiveStreamsBatchResponse: ...
    @overload
    def live_stream(self, **params: Unpack[EbayLiveStreamStreamParams]) -> BinaryIO: ...
    @overload
    def live_stream(self, **params: Unpack[EbayLiveStreamTextResponseParams]) -> str: ...
    @overload
    def live_stream(self, **params: Unpack[EbayLiveStreamDefaultParams]) -> EbayLiveStreamResponse: ...
    @overload
    def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsStreamParams]) -> BinaryIO: ...
    @overload
    def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsTextResponseParams]) -> str: ...
    @overload
    def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsDefaultParams]) -> EbayLiveStreamItemsResponse: ...
    @overload
    def search(self, **params: Unpack[EbaySearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[EbaySearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[EbaySearchDefaultParams]) -> EbaySearchResponse: ...
    @overload
    def seller(self, **params: Unpack[EbaySellerStreamParams]) -> BinaryIO: ...
    @overload
    def seller(self, **params: Unpack[EbaySellerTextResponseParams]) -> str: ...
    @overload
    def seller(self, **params: Unpack[EbaySellerDefaultParams]) -> EbaySellerResponse: ...
    @overload
    def seller_about(self, **params: Unpack[EbaySellerAboutStreamParams]) -> BinaryIO: ...
    @overload
    def seller_about(self, **params: Unpack[EbaySellerAboutTextResponseParams]) -> str: ...
    @overload
    def seller_about(self, **params: Unpack[EbaySellerAboutDefaultParams]) -> EbaySellerAboutResponse: ...
    @overload
    def seller_feedback(self, **params: Unpack[EbaySellerFeedbackStreamParams]) -> BinaryIO: ...
    @overload
    def seller_feedback(self, **params: Unpack[EbaySellerFeedbackTextResponseParams]) -> str: ...
    @overload
    def seller_feedback(self, **params: Unpack[EbaySellerFeedbackDefaultParams]) -> EbaySellerFeedbackResponse: ...
    @overload
    def seller_shop(self, **params: Unpack[EbaySellerShopStreamParams]) -> BinaryIO: ...
    @overload
    def seller_shop(self, **params: Unpack[EbaySellerShopTextResponseParams]) -> str: ...
    @overload
    def seller_shop(self, **params: Unpack[EbaySellerShopDefaultParams]) -> EbaySellerShopResponse: ...

class AsyncEbayClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncEbayClient: ...
    ebay: _AsyncEbayGroup
    @overload
    async def item(self, **params: Unpack[EbayItemStreamParams]) -> BinaryIO: ...
    @overload
    async def item(self, **params: Unpack[EbayItemTextResponseParams]) -> str: ...
    @overload
    async def item(self, **params: Unpack[EbayItemDefaultParams]) -> EbayItemResponse: ...
    @overload
    async def live_streams(self, **params: Unpack[EbayLiveStreamsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_streams(self, **params: Unpack[EbayLiveStreamsTextResponseParams]) -> str: ...
    @overload
    async def live_streams(self, **params: Unpack[EbayLiveStreamsDefaultParams]) -> EbayLiveStreamsResponse: ...
    @overload
    async def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchStreamParams]) -> BinaryIO: ...
    @overload
    async def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchTextResponseParams]) -> str: ...
    @overload
    async def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchDefaultParams]) -> EbayLiveStreamsBatchResponse: ...
    @overload
    async def live_stream(self, **params: Unpack[EbayLiveStreamStreamParams]) -> BinaryIO: ...
    @overload
    async def live_stream(self, **params: Unpack[EbayLiveStreamTextResponseParams]) -> str: ...
    @overload
    async def live_stream(self, **params: Unpack[EbayLiveStreamDefaultParams]) -> EbayLiveStreamResponse: ...
    @overload
    async def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsTextResponseParams]) -> str: ...
    @overload
    async def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsDefaultParams]) -> EbayLiveStreamItemsResponse: ...
    @overload
    async def search(self, **params: Unpack[EbaySearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[EbaySearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[EbaySearchDefaultParams]) -> EbaySearchResponse: ...
    @overload
    async def seller(self, **params: Unpack[EbaySellerStreamParams]) -> BinaryIO: ...
    @overload
    async def seller(self, **params: Unpack[EbaySellerTextResponseParams]) -> str: ...
    @overload
    async def seller(self, **params: Unpack[EbaySellerDefaultParams]) -> EbaySellerResponse: ...
    @overload
    async def seller_about(self, **params: Unpack[EbaySellerAboutStreamParams]) -> BinaryIO: ...
    @overload
    async def seller_about(self, **params: Unpack[EbaySellerAboutTextResponseParams]) -> str: ...
    @overload
    async def seller_about(self, **params: Unpack[EbaySellerAboutDefaultParams]) -> EbaySellerAboutResponse: ...
    @overload
    async def seller_feedback(self, **params: Unpack[EbaySellerFeedbackStreamParams]) -> BinaryIO: ...
    @overload
    async def seller_feedback(self, **params: Unpack[EbaySellerFeedbackTextResponseParams]) -> str: ...
    @overload
    async def seller_feedback(self, **params: Unpack[EbaySellerFeedbackDefaultParams]) -> EbaySellerFeedbackResponse: ...
    @overload
    async def seller_shop(self, **params: Unpack[EbaySellerShopStreamParams]) -> BinaryIO: ...
    @overload
    async def seller_shop(self, **params: Unpack[EbaySellerShopTextResponseParams]) -> str: ...
    @overload
    async def seller_shop(self, **params: Unpack[EbaySellerShopDefaultParams]) -> EbaySellerShopResponse: ...

class _AsyncEbayGroup:
    @overload
    async def item(self, **params: Unpack[EbayItemStreamParams]) -> BinaryIO: ...
    @overload
    async def item(self, **params: Unpack[EbayItemTextResponseParams]) -> str: ...
    @overload
    async def item(self, **params: Unpack[EbayItemDefaultParams]) -> EbayItemResponse: ...
    @overload
    async def live_streams(self, **params: Unpack[EbayLiveStreamsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_streams(self, **params: Unpack[EbayLiveStreamsTextResponseParams]) -> str: ...
    @overload
    async def live_streams(self, **params: Unpack[EbayLiveStreamsDefaultParams]) -> EbayLiveStreamsResponse: ...
    @overload
    async def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchStreamParams]) -> BinaryIO: ...
    @overload
    async def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchTextResponseParams]) -> str: ...
    @overload
    async def live_streams_batch(self, **params: Unpack[EbayLiveStreamsBatchDefaultParams]) -> EbayLiveStreamsBatchResponse: ...
    @overload
    async def live_stream(self, **params: Unpack[EbayLiveStreamStreamParams]) -> BinaryIO: ...
    @overload
    async def live_stream(self, **params: Unpack[EbayLiveStreamTextResponseParams]) -> str: ...
    @overload
    async def live_stream(self, **params: Unpack[EbayLiveStreamDefaultParams]) -> EbayLiveStreamResponse: ...
    @overload
    async def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsTextResponseParams]) -> str: ...
    @overload
    async def live_stream_items(self, **params: Unpack[EbayLiveStreamItemsDefaultParams]) -> EbayLiveStreamItemsResponse: ...
    @overload
    async def search(self, **params: Unpack[EbaySearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[EbaySearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[EbaySearchDefaultParams]) -> EbaySearchResponse: ...
    @overload
    async def seller(self, **params: Unpack[EbaySellerStreamParams]) -> BinaryIO: ...
    @overload
    async def seller(self, **params: Unpack[EbaySellerTextResponseParams]) -> str: ...
    @overload
    async def seller(self, **params: Unpack[EbaySellerDefaultParams]) -> EbaySellerResponse: ...
    @overload
    async def seller_about(self, **params: Unpack[EbaySellerAboutStreamParams]) -> BinaryIO: ...
    @overload
    async def seller_about(self, **params: Unpack[EbaySellerAboutTextResponseParams]) -> str: ...
    @overload
    async def seller_about(self, **params: Unpack[EbaySellerAboutDefaultParams]) -> EbaySellerAboutResponse: ...
    @overload
    async def seller_feedback(self, **params: Unpack[EbaySellerFeedbackStreamParams]) -> BinaryIO: ...
    @overload
    async def seller_feedback(self, **params: Unpack[EbaySellerFeedbackTextResponseParams]) -> str: ...
    @overload
    async def seller_feedback(self, **params: Unpack[EbaySellerFeedbackDefaultParams]) -> EbaySellerFeedbackResponse: ...
    @overload
    async def seller_shop(self, **params: Unpack[EbaySellerShopStreamParams]) -> BinaryIO: ...
    @overload
    async def seller_shop(self, **params: Unpack[EbaySellerShopTextResponseParams]) -> str: ...
    @overload
    async def seller_shop(self, **params: Unpack[EbaySellerShopDefaultParams]) -> EbaySellerShopResponse: ...

EbayItemDefaultParams = TypedDict('EbayItemDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'item_id': Required[str],
}, total=False)

EbayItemTextResponseParams = TypedDict('EbayItemTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'item_id': Required[str],
}, total=False)

EbayItemStreamParams = TypedDict('EbayItemStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'item_id': Required[str],
}, total=False)

EbayLiveStreamsDefaultParams = TypedDict('EbayLiveStreamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': NotRequired[Literal['explore', 'IPqZx79LNuwFcSVt', 'oHjQFTlZ5cYgWkjB', 'l68DJtBAVZge4x4n', '2Nk3OYiOJHfXqpWG', '5quuEnjO3axyz46U', 'nGpMTpm13Q86Eaoo', 'sYRxeaskGmNC6xaB', 'iYaYo88zN2vtQorh', 'GYAbsFw6onSNloAb', 'WJ9zLwYjK8njaBtN', 'rALkRyk8gXHzIBR6', 'DNta0sJ8Y6NXZsC9', 'GU4UfBzZSF4jiteS', 'IO7Oih07PtNJSWhU', 'cF4xtF8z9riubmLh', 'bywKDIdtxhi4hUSO']],
    'request_number': NotRequired[int],
    'session_id': NotRequired[str],
}, total=False)

EbayLiveStreamsTextResponseParams = TypedDict('EbayLiveStreamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': NotRequired[Literal['explore', 'IPqZx79LNuwFcSVt', 'oHjQFTlZ5cYgWkjB', 'l68DJtBAVZge4x4n', '2Nk3OYiOJHfXqpWG', '5quuEnjO3axyz46U', 'nGpMTpm13Q86Eaoo', 'sYRxeaskGmNC6xaB', 'iYaYo88zN2vtQorh', 'GYAbsFw6onSNloAb', 'WJ9zLwYjK8njaBtN', 'rALkRyk8gXHzIBR6', 'DNta0sJ8Y6NXZsC9', 'GU4UfBzZSF4jiteS', 'IO7Oih07PtNJSWhU', 'cF4xtF8z9riubmLh', 'bywKDIdtxhi4hUSO']],
    'request_number': NotRequired[int],
    'session_id': NotRequired[str],
}, total=False)

EbayLiveStreamsStreamParams = TypedDict('EbayLiveStreamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': NotRequired[Literal['explore', 'IPqZx79LNuwFcSVt', 'oHjQFTlZ5cYgWkjB', 'l68DJtBAVZge4x4n', '2Nk3OYiOJHfXqpWG', '5quuEnjO3axyz46U', 'nGpMTpm13Q86Eaoo', 'sYRxeaskGmNC6xaB', 'iYaYo88zN2vtQorh', 'GYAbsFw6onSNloAb', 'WJ9zLwYjK8njaBtN', 'rALkRyk8gXHzIBR6', 'DNta0sJ8Y6NXZsC9', 'GU4UfBzZSF4jiteS', 'IO7Oih07PtNJSWhU', 'cF4xtF8z9riubmLh', 'bywKDIdtxhi4hUSO']],
    'request_number': NotRequired[int],
    'session_id': NotRequired[str],
}, total=False)

EbayLiveStreamsBatchDefaultParams = TypedDict('EbayLiveStreamsBatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

EbayLiveStreamsBatchTextResponseParams = TypedDict('EbayLiveStreamsBatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

EbayLiveStreamsBatchStreamParams = TypedDict('EbayLiveStreamsBatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
}, total=False)

EbayLiveStreamDefaultParams = TypedDict('EbayLiveStreamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

EbayLiveStreamTextResponseParams = TypedDict('EbayLiveStreamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

EbayLiveStreamStreamParams = TypedDict('EbayLiveStreamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

EbayLiveStreamItemsDefaultParams = TypedDict('EbayLiveStreamItemsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

EbayLiveStreamItemsTextResponseParams = TypedDict('EbayLiveStreamItemsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

EbayLiveStreamItemsStreamParams = TypedDict('EbayLiveStreamItemsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

EbaySearchDefaultParams = TypedDict('EbaySearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'option': Required[EbaySearchBody],
}, total=False)

EbaySearchTextResponseParams = TypedDict('EbaySearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'option': Required[EbaySearchBody],
}, total=False)

EbaySearchStreamParams = TypedDict('EbaySearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'option': Required[EbaySearchBody],
}, total=False)

EbaySellerDefaultParams = TypedDict('EbaySellerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'seller': Required[str],
}, total=False)

EbaySellerTextResponseParams = TypedDict('EbaySellerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'seller': Required[str],
}, total=False)

EbaySellerStreamParams = TypedDict('EbaySellerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'seller': Required[str],
}, total=False)

EbaySellerAboutDefaultParams = TypedDict('EbaySellerAboutDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'seller': Required[str],
}, total=False)

EbaySellerAboutTextResponseParams = TypedDict('EbaySellerAboutTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'seller': Required[str],
}, total=False)

EbaySellerAboutStreamParams = TypedDict('EbaySellerAboutStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'seller': Required[str],
}, total=False)

EbaySellerFeedbackDefaultParams = TypedDict('EbaySellerFeedbackDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'seller': Required[str],
    'page': NotRequired[int],
    'per_page': NotRequired[Literal['24', '48', '72']],
}, total=False)

EbaySellerFeedbackTextResponseParams = TypedDict('EbaySellerFeedbackTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'seller': Required[str],
    'page': NotRequired[int],
    'per_page': NotRequired[Literal['24', '48', '72']],
}, total=False)

EbaySellerFeedbackStreamParams = TypedDict('EbaySellerFeedbackStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'seller': Required[str],
    'page': NotRequired[int],
    'per_page': NotRequired[Literal['24', '48', '72']],
}, total=False)

EbaySellerShopDefaultParams = TypedDict('EbaySellerShopDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'seller': Required[str],
    'page': NotRequired[int],
}, total=False)

EbaySellerShopTextResponseParams = TypedDict('EbaySellerShopTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'seller': Required[str],
    'page': NotRequired[int],
}, total=False)

EbaySellerShopStreamParams = TypedDict('EbaySellerShopStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'seller': Required[str],
    'page': NotRequired[int],
}, total=False)
