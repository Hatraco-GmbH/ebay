from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sales_tax_jurisdictions import SalesTaxJurisdictions
from ...types import Response


def _get_kwargs(
    country_code: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/country/{country_code}/sales_tax_jurisdiction",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SalesTaxJurisdictions]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SalesTaxJurisdictions.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, SalesTaxJurisdictions]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    country_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, SalesTaxJurisdictions]]:
    r"""This method retrieves all sales-tax jurisdictions for the country specified in the
    <b>countryCode</b> path parameter. Countries with valid sales-tax jurisdictions are Canada and the
    US.<br><br>The response from this call tells you the jurisdictions for which a seller can configure
    tax tables. Although setting up tax tables is optional, you can use the
    <b>createOrReplaceSalesTax</b> method in the <b>Account API</b> call to configure the tax tables for
    the jurisdictions into which you sell.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax
    tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br><br><div
    class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span
    style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important!
    &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\"
    class=\"mcFormatColor\">Important!</span></b></span></span> In the US, eBay now calculates,
    collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC.
    Sellers can no longer specify sales-tax rates for these jurisdictions using a tax
    table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following
    US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands
    (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to
    <a href=\"https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 \"
    target=\"_blank\">Taxes and import charges</a>.</p></div>

    Args:
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SalesTaxJurisdictions]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    country_code: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, SalesTaxJurisdictions]]:
    r"""This method retrieves all sales-tax jurisdictions for the country specified in the
    <b>countryCode</b> path parameter. Countries with valid sales-tax jurisdictions are Canada and the
    US.<br><br>The response from this call tells you the jurisdictions for which a seller can configure
    tax tables. Although setting up tax tables is optional, you can use the
    <b>createOrReplaceSalesTax</b> method in the <b>Account API</b> call to configure the tax tables for
    the jurisdictions into which you sell.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax
    tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br><br><div
    class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span
    style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important!
    &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\"
    class=\"mcFormatColor\">Important!</span></b></span></span> In the US, eBay now calculates,
    collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC.
    Sellers can no longer specify sales-tax rates for these jurisdictions using a tax
    table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following
    US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands
    (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to
    <a href=\"https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 \"
    target=\"_blank\">Taxes and import charges</a>.</p></div>

    Args:
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SalesTaxJurisdictions]
    """

    return sync_detailed(
        country_code=country_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    country_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, SalesTaxJurisdictions]]:
    r"""This method retrieves all sales-tax jurisdictions for the country specified in the
    <b>countryCode</b> path parameter. Countries with valid sales-tax jurisdictions are Canada and the
    US.<br><br>The response from this call tells you the jurisdictions for which a seller can configure
    tax tables. Although setting up tax tables is optional, you can use the
    <b>createOrReplaceSalesTax</b> method in the <b>Account API</b> call to configure the tax tables for
    the jurisdictions into which you sell.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax
    tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br><br><div
    class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span
    style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important!
    &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\"
    class=\"mcFormatColor\">Important!</span></b></span></span> In the US, eBay now calculates,
    collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC.
    Sellers can no longer specify sales-tax rates for these jurisdictions using a tax
    table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following
    US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands
    (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to
    <a href=\"https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 \"
    target=\"_blank\">Taxes and import charges</a>.</p></div>

    Args:
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SalesTaxJurisdictions]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    country_code: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, SalesTaxJurisdictions]]:
    r"""This method retrieves all sales-tax jurisdictions for the country specified in the
    <b>countryCode</b> path parameter. Countries with valid sales-tax jurisdictions are Canada and the
    US.<br><br>The response from this call tells you the jurisdictions for which a seller can configure
    tax tables. Although setting up tax tables is optional, you can use the
    <b>createOrReplaceSalesTax</b> method in the <b>Account API</b> call to configure the tax tables for
    the jurisdictions into which you sell.<br><br><span class=\"tablenote\"><b>Note:</b> Sales-tax
    tables are only available for the US (EBAY_US) and Canada (EBAY_CA) marketplaces.</span><br><br><div
    class=\"msgbox_important\"><p class=\"msgbox_importantInDiv\" data-mc-autonum=\"&lt;b&gt;&lt;span
    style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important!
    &lt;/span&gt;&lt;/b&gt;\"><span class=\"autonumber\"><span><b><span style=\"color: #dd1e31;\"
    class=\"mcFormatColor\">Important!</span></b></span></span> In the US, eBay now calculates,
    collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC.
    Sellers can no longer specify sales-tax rates for these jurisdictions using a tax
    table.<br><br>However, sellers may continue to use a sales-tax table to set rates for the following
    US territories:<ul><li>American Samoa (AS)</li><li>Guam (GU)</li><li>Northern Mariana Islands
    (MP)</li><li>Palau (PW)</li><li>US Virgin Islands (VI)</li></ul>For additional information, refer to
    <a href=\"https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 \"
    target=\"_blank\">Taxes and import charges</a>.</p></div>

    Args:
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SalesTaxJurisdictions]
    """

    return (
        await asyncio_detailed(
            country_code=country_code,
            client=client,
        )
    ).parsed
