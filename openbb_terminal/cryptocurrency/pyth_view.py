# pylint: disable= C0301

import asyncio
import logging
import os

from openbb_terminal.cryptocurrency.pyth_model import get_price
from openbb_terminal.decorators import check_api_key
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    export_data,
)
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
@check_api_key(["API_COINGLASS_KEY"])
def display_price(symbol: str, export: str = "") -> None:
    """Displays live price from pyth live feed
    [Source: https://pyth.network/]

    Parameters
    ----------
    symbol : str
        Symbol of the asset to get price for
    export : str
        Export dataframe data to csv,json,xlsx file"""

    try:
        while True:
            price, confidence, previous_price = asyncio.run(get_price(symbol))
            console.print(
                f"Price of {symbol} is {'[red]' if previous_price >= price else '[green]'}{price}{'[/red]' if previous_price >= price else '[/green]'} ± {confidence}",  # noqa: E501
                end="\r",
            )
    except KeyboardInterrupt:
        print(f"\nStopped watching {symbol} price\n")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "price",
        "",
    )