from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.regulatory_policy_response import RegulatoryPolicyResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    marketplace_id: str,
    *,
    filter_: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/marketplace/{marketplace_id}/get_regulatory_policies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, RegulatoryPolicyResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RegulatoryPolicyResponse.from_dict(response.json())

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
) -> Response[Union[Any, RegulatoryPolicyResponse]]:
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
) -> Response[Union[Any, RegulatoryPolicyResponse]]:
    r"""This method returns regulatory policies for one, multiple, or all eBay categories in an eBay
    marketplace. The identifier of the eBay marketplace is passed in as a path parameter, and unless one
    or more eBay category IDs are passed in through the filter query parameter, this method will return
    metadata for every listing category in the specified marketplace.</p><p><span
    class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> This method can
    potentially return a very large response payload. eBay recommends that the response payload be
    compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to
    <code>gzip</code>.</span></p>

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RegulatoryPolicyResponse]]
    """

    kwargs = _get_kwargs(
        marketplace_id=marketplace_id,
        filter_=filter_,
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
) -> Optional[Union[Any, RegulatoryPolicyResponse]]:
    r"""This method returns regulatory policies for one, multiple, or all eBay categories in an eBay
    marketplace. The identifier of the eBay marketplace is passed in as a path parameter, and unless one
    or more eBay category IDs are passed in through the filter query parameter, this method will return
    metadata for every listing category in the specified marketplace.</p><p><span
    class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> This method can
    potentially return a very large response payload. eBay recommends that the response payload be
    compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to
    <code>gzip</code>.</span></p>

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RegulatoryPolicyResponse]
    """

    return sync_detailed(
        marketplace_id=marketplace_id,
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, RegulatoryPolicyResponse]]:
    r"""This method returns regulatory policies for one, multiple, or all eBay categories in an eBay
    marketplace. The identifier of the eBay marketplace is passed in as a path parameter, and unless one
    or more eBay category IDs are passed in through the filter query parameter, this method will return
    metadata for every listing category in the specified marketplace.</p><p><span
    class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> This method can
    potentially return a very large response payload. eBay recommends that the response payload be
    compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to
    <code>gzip</code>.</span></p>

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RegulatoryPolicyResponse]]
    """

    kwargs = _get_kwargs(
        marketplace_id=marketplace_id,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, RegulatoryPolicyResponse]]:
    r"""This method returns regulatory policies for one, multiple, or all eBay categories in an eBay
    marketplace. The identifier of the eBay marketplace is passed in as a path parameter, and unless one
    or more eBay category IDs are passed in through the filter query parameter, this method will return
    metadata for every listing category in the specified marketplace.</p><p><span
    class=\"tablenote\"><span style=\"color:#478415\"><strong>Tip:</strong></span> This method can
    potentially return a very large response payload. eBay recommends that the response payload be
    compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to
    <code>gzip</code>.</span></p>

    Args:
        marketplace_id (str):
        filter_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RegulatoryPolicyResponse]
    """

    return (
        await asyncio_detailed(
            marketplace_id=marketplace_id,
            client=client,
            filter_=filter_,
        )
    ).parsed
