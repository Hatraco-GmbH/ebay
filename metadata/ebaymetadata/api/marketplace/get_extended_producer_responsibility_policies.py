from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extended_producer_responsibility_policy_response import ExtendedProducerResponsibilityPolicyResponse
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
        "url": f"/marketplace/{marketplace_id}/get_extended_producer_responsibility_policies",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ExtendedProducerResponsibilityPolicyResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExtendedProducerResponsibilityPolicyResponse.from_dict(response.json())

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
) -> Response[Union[Any, ExtendedProducerResponsibilityPolicyResponse]]:
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
) -> Response[Union[Any, ExtendedProducerResponsibilityPolicyResponse]]:
    r"""This method returns the Extended Producer Responsibility policies for one, multiple, or all eBay
    categories in an eBay marketplace.<br><br>The identifier of the eBay marketplace is passed in as a
    path parameter, and unless one or more eBay category IDs are passed in through the filter query
    parameter, this method will return metadata on every applicable category for the specified
    marketplace.<br><br><span class=\"tablenote\"><span
    style=\"color:#004680\"><strong>Note:</strong></span> Currently, the Extended Producer
    Responsibility policies are only applicable to a limited number of categories.</span><br><span
    class=\"tablenote\"><span style=\"color:#004680\"><strong>Note: </strong></span>Extended Producer
    Responsibility IDs are no longer set at the listing level so category-level metadata is no longer
    returned. Instead, sellers will provide/manage these IDs at the account level by going to <a
    href=\"https://accountsettings.ebay.fr/epr-fr \" target=\"_blank\">Account
    Settings</a>.</span><br><span class=\"tablenote\"><span
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
        Response[Union[Any, ExtendedProducerResponsibilityPolicyResponse]]
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
) -> Optional[Union[Any, ExtendedProducerResponsibilityPolicyResponse]]:
    r"""This method returns the Extended Producer Responsibility policies for one, multiple, or all eBay
    categories in an eBay marketplace.<br><br>The identifier of the eBay marketplace is passed in as a
    path parameter, and unless one or more eBay category IDs are passed in through the filter query
    parameter, this method will return metadata on every applicable category for the specified
    marketplace.<br><br><span class=\"tablenote\"><span
    style=\"color:#004680\"><strong>Note:</strong></span> Currently, the Extended Producer
    Responsibility policies are only applicable to a limited number of categories.</span><br><span
    class=\"tablenote\"><span style=\"color:#004680\"><strong>Note: </strong></span>Extended Producer
    Responsibility IDs are no longer set at the listing level so category-level metadata is no longer
    returned. Instead, sellers will provide/manage these IDs at the account level by going to <a
    href=\"https://accountsettings.ebay.fr/epr-fr \" target=\"_blank\">Account
    Settings</a>.</span><br><span class=\"tablenote\"><span
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
        Union[Any, ExtendedProducerResponsibilityPolicyResponse]
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
) -> Response[Union[Any, ExtendedProducerResponsibilityPolicyResponse]]:
    r"""This method returns the Extended Producer Responsibility policies for one, multiple, or all eBay
    categories in an eBay marketplace.<br><br>The identifier of the eBay marketplace is passed in as a
    path parameter, and unless one or more eBay category IDs are passed in through the filter query
    parameter, this method will return metadata on every applicable category for the specified
    marketplace.<br><br><span class=\"tablenote\"><span
    style=\"color:#004680\"><strong>Note:</strong></span> Currently, the Extended Producer
    Responsibility policies are only applicable to a limited number of categories.</span><br><span
    class=\"tablenote\"><span style=\"color:#004680\"><strong>Note: </strong></span>Extended Producer
    Responsibility IDs are no longer set at the listing level so category-level metadata is no longer
    returned. Instead, sellers will provide/manage these IDs at the account level by going to <a
    href=\"https://accountsettings.ebay.fr/epr-fr \" target=\"_blank\">Account
    Settings</a>.</span><br><span class=\"tablenote\"><span
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
        Response[Union[Any, ExtendedProducerResponsibilityPolicyResponse]]
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
) -> Optional[Union[Any, ExtendedProducerResponsibilityPolicyResponse]]:
    r"""This method returns the Extended Producer Responsibility policies for one, multiple, or all eBay
    categories in an eBay marketplace.<br><br>The identifier of the eBay marketplace is passed in as a
    path parameter, and unless one or more eBay category IDs are passed in through the filter query
    parameter, this method will return metadata on every applicable category for the specified
    marketplace.<br><br><span class=\"tablenote\"><span
    style=\"color:#004680\"><strong>Note:</strong></span> Currently, the Extended Producer
    Responsibility policies are only applicable to a limited number of categories.</span><br><span
    class=\"tablenote\"><span style=\"color:#004680\"><strong>Note: </strong></span>Extended Producer
    Responsibility IDs are no longer set at the listing level so category-level metadata is no longer
    returned. Instead, sellers will provide/manage these IDs at the account level by going to <a
    href=\"https://accountsettings.ebay.fr/epr-fr \" target=\"_blank\">Account
    Settings</a>.</span><br><span class=\"tablenote\"><span
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
        Union[Any, ExtendedProducerResponsibilityPolicyResponse]
    """

    return (
        await asyncio_detailed(
            marketplace_id=marketplace_id,
            client=client,
            filter_=filter_,
            accept_encoding=accept_encoding,
        )
    ).parsed
