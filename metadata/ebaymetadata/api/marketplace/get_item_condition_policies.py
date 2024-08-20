from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.item_condition_policy_response import ItemConditionPolicyResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    marketplace_id: str,
    *,
    filter_: Union[Unset, str] = UNSET,
    accept_encoding: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(accept_encoding, Unset):
        headers["Accept-Encoding"] = accept_encoding

    params: Dict[str, Any] = {}

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/marketplace/{marketplace_id}/get_item_condition_policies",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ItemConditionPolicyResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ItemConditionPolicyResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ItemConditionPolicyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
    accept_encoding: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ItemConditionPolicyResponse]]:
    r"""This method returns item condition metadata on one, multiple, or all eBay categories on an eBay
    marketplace. This metadata consists of the different item conditions (with IDs) that an eBay
    category supports, and a boolean to indicate if an eBay category requires an item condition.
    <br><br>If applicable, this metadata also shows the different condition descriptors (with IDs) that
    an eBay category supports.<br><br><span class=\"tablenote\"><b>Note:</b> Currently, condition
    grading is only applicable to the following trading card categories: <ul><li>Non-Sport Trading Card
    Singles</li><li>CCG Individual Cards</li><li>Sports Trading Cards Singles</li></ul></span><br>The
    identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay
    category IDs are passed in through the <b>filter</b> query parameter, this method will return
    metadata on every single category for the specified marketplace. If you only want to view item
    condition metadata for one eBay category or a select group of eBay categories, you can pass in up to
    50 eBay category ID through the <b>filter</b> query parameter.<br><br><span
    class=\"tablenote\"><span style=\"color:#FF0000\"><strong>Important:</strong></span> <b>Certified -
    Refurbished</b>-eligible sellers, and sellers who are eligible to list with the new values
    (EXCELLENT_REFURBISHED, VERY_GOOD_REFURBISHED, and GOOD_REFURBISHED) must use an OAuth token created
    with the <a href=\"/api-docs/static/oauth-authorization-code-grant.html\"
    target=\"_blank\">authorization code grant flow</a> and
    <b>https://api.ebay.com/oauth/api_scope/sell.inventory</b> scope in order to retrieve the
    refurbished conditions for the relevant categories.<br/><br/>See the <a href=\"/api-
    docs/sell/static/metadata/condition-id-values.html#Category \" target=\"_blank\">eBay Refurbished
    Program - Category and marketplace support</a> topic for the categories and marketplaces that
    support these refurbished conditions<br/><br/>These restricted item conditions will not be returned
    if an OAuth token created with the <a href=\"/api-docs/static/oauth-client-credentials-grant.html\"
    target=\"_blank\">client credentials grant flow</a> and <b>https://api.ebay.com/oauth/api_scope</b>
    scope is used, or if any seller is not eligible to list with that item condition. <br/><br/> See the
    <a href=\"/api-docs/static/oauth-scopes.html\" target=\"_blank\">Specifying OAuth scopes</a> topic
    for more information about specifying scopes.</span><br><br><span class=\"tablenote\"><span
    style=\"color:#478415\"><strong>Tip:</strong></span> This method can potentially return a very large
    response payload. eBay recommends that the response payload be compressed by passing in the
    <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):
        accept_encoding (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ItemConditionPolicyResponse]]
    """

    kwargs = _get_kwargs(
        marketplace_id=marketplace_id,
        filter_=filter_,
        accept_encoding=accept_encoding,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
    accept_encoding: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ItemConditionPolicyResponse]]:
    r"""This method returns item condition metadata on one, multiple, or all eBay categories on an eBay
    marketplace. This metadata consists of the different item conditions (with IDs) that an eBay
    category supports, and a boolean to indicate if an eBay category requires an item condition.
    <br><br>If applicable, this metadata also shows the different condition descriptors (with IDs) that
    an eBay category supports.<br><br><span class=\"tablenote\"><b>Note:</b> Currently, condition
    grading is only applicable to the following trading card categories: <ul><li>Non-Sport Trading Card
    Singles</li><li>CCG Individual Cards</li><li>Sports Trading Cards Singles</li></ul></span><br>The
    identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay
    category IDs are passed in through the <b>filter</b> query parameter, this method will return
    metadata on every single category for the specified marketplace. If you only want to view item
    condition metadata for one eBay category or a select group of eBay categories, you can pass in up to
    50 eBay category ID through the <b>filter</b> query parameter.<br><br><span
    class=\"tablenote\"><span style=\"color:#FF0000\"><strong>Important:</strong></span> <b>Certified -
    Refurbished</b>-eligible sellers, and sellers who are eligible to list with the new values
    (EXCELLENT_REFURBISHED, VERY_GOOD_REFURBISHED, and GOOD_REFURBISHED) must use an OAuth token created
    with the <a href=\"/api-docs/static/oauth-authorization-code-grant.html\"
    target=\"_blank\">authorization code grant flow</a> and
    <b>https://api.ebay.com/oauth/api_scope/sell.inventory</b> scope in order to retrieve the
    refurbished conditions for the relevant categories.<br/><br/>See the <a href=\"/api-
    docs/sell/static/metadata/condition-id-values.html#Category \" target=\"_blank\">eBay Refurbished
    Program - Category and marketplace support</a> topic for the categories and marketplaces that
    support these refurbished conditions<br/><br/>These restricted item conditions will not be returned
    if an OAuth token created with the <a href=\"/api-docs/static/oauth-client-credentials-grant.html\"
    target=\"_blank\">client credentials grant flow</a> and <b>https://api.ebay.com/oauth/api_scope</b>
    scope is used, or if any seller is not eligible to list with that item condition. <br/><br/> See the
    <a href=\"/api-docs/static/oauth-scopes.html\" target=\"_blank\">Specifying OAuth scopes</a> topic
    for more information about specifying scopes.</span><br><br><span class=\"tablenote\"><span
    style=\"color:#478415\"><strong>Tip:</strong></span> This method can potentially return a very large
    response payload. eBay recommends that the response payload be compressed by passing in the
    <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):
        accept_encoding (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ItemConditionPolicyResponse]
    """

    return sync_detailed(
        marketplace_id=marketplace_id,
        client=client,
        filter_=filter_,
        accept_encoding=accept_encoding,
    ).parsed


async def asyncio_detailed(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
    accept_encoding: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ItemConditionPolicyResponse]]:
    r"""This method returns item condition metadata on one, multiple, or all eBay categories on an eBay
    marketplace. This metadata consists of the different item conditions (with IDs) that an eBay
    category supports, and a boolean to indicate if an eBay category requires an item condition.
    <br><br>If applicable, this metadata also shows the different condition descriptors (with IDs) that
    an eBay category supports.<br><br><span class=\"tablenote\"><b>Note:</b> Currently, condition
    grading is only applicable to the following trading card categories: <ul><li>Non-Sport Trading Card
    Singles</li><li>CCG Individual Cards</li><li>Sports Trading Cards Singles</li></ul></span><br>The
    identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay
    category IDs are passed in through the <b>filter</b> query parameter, this method will return
    metadata on every single category for the specified marketplace. If you only want to view item
    condition metadata for one eBay category or a select group of eBay categories, you can pass in up to
    50 eBay category ID through the <b>filter</b> query parameter.<br><br><span
    class=\"tablenote\"><span style=\"color:#FF0000\"><strong>Important:</strong></span> <b>Certified -
    Refurbished</b>-eligible sellers, and sellers who are eligible to list with the new values
    (EXCELLENT_REFURBISHED, VERY_GOOD_REFURBISHED, and GOOD_REFURBISHED) must use an OAuth token created
    with the <a href=\"/api-docs/static/oauth-authorization-code-grant.html\"
    target=\"_blank\">authorization code grant flow</a> and
    <b>https://api.ebay.com/oauth/api_scope/sell.inventory</b> scope in order to retrieve the
    refurbished conditions for the relevant categories.<br/><br/>See the <a href=\"/api-
    docs/sell/static/metadata/condition-id-values.html#Category \" target=\"_blank\">eBay Refurbished
    Program - Category and marketplace support</a> topic for the categories and marketplaces that
    support these refurbished conditions<br/><br/>These restricted item conditions will not be returned
    if an OAuth token created with the <a href=\"/api-docs/static/oauth-client-credentials-grant.html\"
    target=\"_blank\">client credentials grant flow</a> and <b>https://api.ebay.com/oauth/api_scope</b>
    scope is used, or if any seller is not eligible to list with that item condition. <br/><br/> See the
    <a href=\"/api-docs/static/oauth-scopes.html\" target=\"_blank\">Specifying OAuth scopes</a> topic
    for more information about specifying scopes.</span><br><br><span class=\"tablenote\"><span
    style=\"color:#478415\"><strong>Tip:</strong></span> This method can potentially return a very large
    response payload. eBay recommends that the response payload be compressed by passing in the
    <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):
        accept_encoding (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ItemConditionPolicyResponse]]
    """

    kwargs = _get_kwargs(
        marketplace_id=marketplace_id,
        filter_=filter_,
        accept_encoding=accept_encoding,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
    accept_encoding: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ItemConditionPolicyResponse]]:
    r"""This method returns item condition metadata on one, multiple, or all eBay categories on an eBay
    marketplace. This metadata consists of the different item conditions (with IDs) that an eBay
    category supports, and a boolean to indicate if an eBay category requires an item condition.
    <br><br>If applicable, this metadata also shows the different condition descriptors (with IDs) that
    an eBay category supports.<br><br><span class=\"tablenote\"><b>Note:</b> Currently, condition
    grading is only applicable to the following trading card categories: <ul><li>Non-Sport Trading Card
    Singles</li><li>CCG Individual Cards</li><li>Sports Trading Cards Singles</li></ul></span><br>The
    identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay
    category IDs are passed in through the <b>filter</b> query parameter, this method will return
    metadata on every single category for the specified marketplace. If you only want to view item
    condition metadata for one eBay category or a select group of eBay categories, you can pass in up to
    50 eBay category ID through the <b>filter</b> query parameter.<br><br><span
    class=\"tablenote\"><span style=\"color:#FF0000\"><strong>Important:</strong></span> <b>Certified -
    Refurbished</b>-eligible sellers, and sellers who are eligible to list with the new values
    (EXCELLENT_REFURBISHED, VERY_GOOD_REFURBISHED, and GOOD_REFURBISHED) must use an OAuth token created
    with the <a href=\"/api-docs/static/oauth-authorization-code-grant.html\"
    target=\"_blank\">authorization code grant flow</a> and
    <b>https://api.ebay.com/oauth/api_scope/sell.inventory</b> scope in order to retrieve the
    refurbished conditions for the relevant categories.<br/><br/>See the <a href=\"/api-
    docs/sell/static/metadata/condition-id-values.html#Category \" target=\"_blank\">eBay Refurbished
    Program - Category and marketplace support</a> topic for the categories and marketplaces that
    support these refurbished conditions<br/><br/>These restricted item conditions will not be returned
    if an OAuth token created with the <a href=\"/api-docs/static/oauth-client-credentials-grant.html\"
    target=\"_blank\">client credentials grant flow</a> and <b>https://api.ebay.com/oauth/api_scope</b>
    scope is used, or if any seller is not eligible to list with that item condition. <br/><br/> See the
    <a href=\"/api-docs/static/oauth-scopes.html\" target=\"_blank\">Specifying OAuth scopes</a> topic
    for more information about specifying scopes.</span><br><br><span class=\"tablenote\"><span
    style=\"color:#478415\"><strong>Tip:</strong></span> This method can potentially return a very large
    response payload. eBay recommends that the response payload be compressed by passing in the
    <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):
        accept_encoding (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ItemConditionPolicyResponse]
    """

    return (
        await asyncio_detailed(
            marketplace_id=marketplace_id,
            client=client,
            filter_=filter_,
            accept_encoding=accept_encoding,
        )
    ).parsed
