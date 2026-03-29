"""Position-sizing strategies: fixed and half-Kelly."""

from __future__ import annotations

import logging
import math

import config as cfg
from db import queries

log = logging.getLogger(__name__)


def compute_half_kelly(
    win_rate: float,
    entry_price: float,
    bankroll: float,
) -> float:
    """Return the half-Kelly stake in USDC.

    Kelly fraction = (win_rate * b - (1 - win_rate)) / b
    where b = 1/entry_price - 1  (net odds on a $1 payout contract).

    We halve it for safety, multiply by bankroll, and floor at $1.00.
    Returns 0.0 if the edge is negative or inputs are degenerate.
    """
    if entry_price <= 0 or entry_price >= 1:
        return 0.0
    b = 1.0 / entry_price - 1.0
    if b <= 0:
        return 0.0

    kelly = (win_rate * b - (1.0 - win_rate)) / b
    if kelly <= 0:
        return 0.0

    half_kelly = kelly / 2.0
    stake = half_kelly * bankroll
    # Floor at $1.00 minimum meaningful trade
    stake = max(math.floor(stake * 100) / 100, 1.00)
    if stake > bankroll:
        stake = bankroll
    return round(stake, 2)


async def get_trade_size(
    entry_price: float,
    real_bankroll: float | None = None,
) -> float:
    """Dispatcher: return the trade size based on the current sizing_mode setting.

    Parameters
    ----------
    entry_price : float
        The entry price of the contract (0-1 range).
    real_bankroll : float | None
        When sizing_mode is 'half-kelly' and demo mode is OFF, this is the
        actual Polymarket USDC balance passed by the scheduler.  Falls back
        to the configured trade_amount_usdc if not provided.
    """
    mode = await queries.get_sizing_mode()

    if mode == "half-kelly":
        win_rate = await queries.get_win_rate_for_kelly()
        if win_rate < 0:
            log.info(
                "Half-Kelly: insufficient data (fewer than %d resolved signals), "
                "falling back to fixed",
                cfg.KELLY_MIN_SAMPLES,
            )
            return await queries.get_trade_amount()

        demo = await queries.is_demo_mode()
        if demo:
            bankroll = await queries.get_demo_balance()
        else:
            # Real mode: use the actual Polymarket balance when the scheduler
            # provides it; otherwise fall back to the configured trade amount.
            if real_bankroll is not None:
                bankroll = real_bankroll
            else:
                bankroll = await queries.get_trade_amount()
                log.warning("Half-Kelly real mode: using trade_amount as bankroll proxy")

        size = compute_half_kelly(win_rate, entry_price, bankroll)
        if size <= 0:
            log.info("Half-Kelly computed $0 — using minimum $1.00")
            size = 1.00
        return size

    # Default: fixed
    return await queries.get_trade_amount()
