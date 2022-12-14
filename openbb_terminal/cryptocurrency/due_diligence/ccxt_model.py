"""Ccxt model"""
__docformat__ = "numpy"

from typing import Dict
import ccxt
import pandas as pd


def get_exchanges():
    """Helper method to get all the exchanges supported by ccxt
    [Source: https://docs.ccxt.com/en/latest/manual.html]

    Parameters
    ----------

    Returns
    -------
    List[str]
        list of all the exchanges supported by ccxt
    """
    return ccxt.exchanges


def get_orderbook(exchange_id: str, coin: str, vs: str) -> Dict:
    """Returns orderbook for a coin in a given exchange
    [Source: https://docs.ccxt.com/en/latest/manual.html]

    Parameters
    ----------
    exchange_id : str
        exchange id
    coin : str
        coin symbol
    vs : str
        currency to compare coin against

    Returns
    -------
    Dict with bids and asks
    """
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class()
    ob = exchange.fetch_order_book(f"{coin.upper()}/{vs.upper()}")
    return ob


def get_trades(exchange_id: str, coin: str, vs: str) -> pd.DataFrame:
    """Returns trades for a coin in a given exchange
    [Source: https://docs.ccxt.com/en/latest/manual.html]

    Parameters
    ----------
    exchange_id : str
        exchange id
    coin : str
        coin symbol
    vs : str
        currency to compare coin against

    Returns
    -------
    pd.DataFrame
        trades for a coin in a given exchange
    """
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class()
    trades = exchange.fetch_trades(f"{coin.upper()}/{vs.upper()}")
    df = pd.DataFrame(trades, columns=["datetime", "price", "amount", "cost", "side"])
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df
