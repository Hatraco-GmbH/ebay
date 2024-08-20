from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product_safety_labels_response import ProductSafetyLabelsResponse
from ...types import Response


def _get_kwargs(
    marketplace_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/marketplace/{marketplace_id}/get_product_safety_labels",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProductSafetyLabelsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProductSafetyLabelsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ProductSafetyLabelsResponse]]:
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
) -> Response[Union[Any, ProductSafetyLabelsResponse]]:
    r"""This method returns product safety label information for the specified eBay marketplace. The
    information includes IDs, descriptions, and URLs (as applicable) for the available statements and
    pictograms. The returned statements are localized for the default language of the marketplace. If a
    marketplace does not support product safety label information, no response payload is returned, but
    only a <b>204 No content</b> status code.<p>This information is used by the seller to add product
    safety label related information to their listings. The <a href=\"/api-
    docs/sell/metadata/resources/marketplace/methods/getRegulatoryPolicies\"
    target=\"_blank\">getRegulatoryPolicies</a> method can be used to see which categories recommend or
    require product safety labels.</p>

    Args:
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProductSafetyLabelsResponse]]
    """

    kwargs = _get_kwargs(
        marketplace_id=marketplace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ProductSafetyLabelsResponse]]:
    r"""This method returns product safety label information for the specified eBay marketplace. The
    information includes IDs, descriptions, and URLs (as applicable) for the available statements and
    pictograms. The returned statements are localized for the default language of the marketplace. If a
    marketplace does not support product safety label information, no response payload is returned, but
    only a <b>204 No content</b> status code.<p>This information is used by the seller to add product
    safety label related information to their listings. The <a href=\"/api-
    docs/sell/metadata/resources/marketplace/methods/getRegulatoryPolicies\"
    target=\"_blank\">getRegulatoryPolicies</a> method can be used to see which categories recommend or
    require product safety labels.</p>

    Args:
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProductSafetyLabelsResponse]
    """

    return sync_detailed(
        marketplace_id=marketplace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ProductSafetyLabelsResponse]]:
    r"""This method returns product safety label information for the specified eBay marketplace. The
    information includes IDs, descriptions, and URLs (as applicable) for the available statements and
    pictograms. The returned statements are localized for the default language of the marketplace. If a
    marketplace does not support product safety label information, no response payload is returned, but
    only a <b>204 No content</b> status code.<p>This information is used by the seller to add product
    safety label related information to their listings. The <a href=\"/api-
    docs/sell/metadata/resources/marketplace/methods/getRegulatoryPolicies\"
    target=\"_blank\">getRegulatoryPolicies</a> method can be used to see which categories recommend or
    require product safety labels.</p>

    Args:
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProductSafetyLabelsResponse]]
    """

    kwargs = _get_kwargs(
        marketplace_id=marketplace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    marketplace_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ProductSafetyLabelsResponse]]:
    r"""This method returns product safety label information for the specified eBay marketplace. The
    information includes IDs, descriptions, and URLs (as applicable) for the available statements and
    pictograms. The returned statements are localized for the default language of the marketplace. If a
    marketplace does not support product safety label information, no response payload is returned, but
    only a <b>204 No content</b> status code.<p>This information is used by the seller to add product
    safety label related information to their listings. The <a href=\"/api-
    docs/sell/metadata/resources/marketplace/methods/getRegulatoryPolicies\"
    target=\"_blank\">getRegulatoryPolicies</a> method can be used to see which categories recommend or
    require product safety labels.</p>

    Args:
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProductSafetyLabelsResponse]
    """

    return (
        await asyncio_detailed(
            marketplace_id=marketplace_id,
            client=client,
        )
    ).parsed
