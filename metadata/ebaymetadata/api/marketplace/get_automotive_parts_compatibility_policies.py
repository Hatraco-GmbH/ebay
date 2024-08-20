from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.automotive_parts_compatibility_policy_response import AutomotivePartsCompatibilityPolicyResponse
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
        "url": f"/marketplace/{marketplace_id}/get_automotive_parts_compatibility_policies",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AutomotivePartsCompatibilityPolicyResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AutomotivePartsCompatibilityPolicyResponse.from_dict(response.json())

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
) -> Response[Union[Any, AutomotivePartsCompatibilityPolicyResponse]]:
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
) -> Response[Union[Any, AutomotivePartsCompatibilityPolicyResponse]]:
    r"""This method returns the eBay policies that define how to list automotive parts compatibility items
    in the categories of the specified marketplace.  <br><br>By default, this method returns all
    categories that support parts compatibility. You can limit the size of the result set by using the
    <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span
    class=\"tablenote\"><b>Note: </b>To return policy information for the eBay US marketplace, specify
    <code>EBAY_MOTORS_US</code> as the path parameter for <b>marketplace_id</b>.</span><br><span
    class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> This method can
    potentially return a very large response payload. eBay recommends that the response payload be
    compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to
    <code>gzip</code>.</span><br>If you specify a valid marketplace ID but that marketplace does not
    contain policy information, or if you filter out all results, a <b>204 No content</b> status code is
    returned with an empty response body.

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):
        accept_encoding (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AutomotivePartsCompatibilityPolicyResponse]]
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
) -> Optional[Union[Any, AutomotivePartsCompatibilityPolicyResponse]]:
    r"""This method returns the eBay policies that define how to list automotive parts compatibility items
    in the categories of the specified marketplace.  <br><br>By default, this method returns all
    categories that support parts compatibility. You can limit the size of the result set by using the
    <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span
    class=\"tablenote\"><b>Note: </b>To return policy information for the eBay US marketplace, specify
    <code>EBAY_MOTORS_US</code> as the path parameter for <b>marketplace_id</b>.</span><br><span
    class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> This method can
    potentially return a very large response payload. eBay recommends that the response payload be
    compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to
    <code>gzip</code>.</span><br>If you specify a valid marketplace ID but that marketplace does not
    contain policy information, or if you filter out all results, a <b>204 No content</b> status code is
    returned with an empty response body.

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):
        accept_encoding (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AutomotivePartsCompatibilityPolicyResponse]
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
) -> Response[Union[Any, AutomotivePartsCompatibilityPolicyResponse]]:
    r"""This method returns the eBay policies that define how to list automotive parts compatibility items
    in the categories of the specified marketplace.  <br><br>By default, this method returns all
    categories that support parts compatibility. You can limit the size of the result set by using the
    <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span
    class=\"tablenote\"><b>Note: </b>To return policy information for the eBay US marketplace, specify
    <code>EBAY_MOTORS_US</code> as the path parameter for <b>marketplace_id</b>.</span><br><span
    class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> This method can
    potentially return a very large response payload. eBay recommends that the response payload be
    compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to
    <code>gzip</code>.</span><br>If you specify a valid marketplace ID but that marketplace does not
    contain policy information, or if you filter out all results, a <b>204 No content</b> status code is
    returned with an empty response body.

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):
        accept_encoding (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AutomotivePartsCompatibilityPolicyResponse]]
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
) -> Optional[Union[Any, AutomotivePartsCompatibilityPolicyResponse]]:
    r"""This method returns the eBay policies that define how to list automotive parts compatibility items
    in the categories of the specified marketplace.  <br><br>By default, this method returns all
    categories that support parts compatibility. You can limit the size of the result set by using the
    <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span
    class=\"tablenote\"><b>Note: </b>To return policy information for the eBay US marketplace, specify
    <code>EBAY_MOTORS_US</code> as the path parameter for <b>marketplace_id</b>.</span><br><span
    class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> This method can
    potentially return a very large response payload. eBay recommends that the response payload be
    compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to
    <code>gzip</code>.</span><br>If you specify a valid marketplace ID but that marketplace does not
    contain policy information, or if you filter out all results, a <b>204 No content</b> status code is
    returned with an empty response body.

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):
        accept_encoding (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AutomotivePartsCompatibilityPolicyResponse]
    """

    return (
        await asyncio_detailed(
            marketplace_id=marketplace_id,
            client=client,
            filter_=filter_,
            accept_encoding=accept_encoding,
        )
    ).parsed
