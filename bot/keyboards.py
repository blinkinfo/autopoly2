"""Inline keyboard layouts for the Telegram bot."""

from __future__ import annotations

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("\U0001f4ca Status", callback_data="cmd_status"),
            InlineKeyboardButton("\U0001f4e1 Signals", callback_data="cmd_signals"),
        ],
        [
            InlineKeyboardButton("\U0001f4b0 Trades", callback_data="cmd_trades"),
            InlineKeyboardButton("\u2699\ufe0f Settings", callback_data="cmd_settings"),
        ],
        [
            InlineKeyboardButton("\U0001f4dd Demo", callback_data="cmd_demo"),
            InlineKeyboardButton("\u2753 Help", callback_data="cmd_help"),
        ],
    ])


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

def settings_keyboard(
    autotrade_on: bool,
    trade_amount: float,
    sizing_mode: str = "fixed",
    demo_on: bool = True,
    demo_balance: float = 100.0,
) -> InlineKeyboardMarkup:
    at_label = "\U0001f916 AutoTrade: ON" if autotrade_on else "\U0001f916 AutoTrade: OFF"
    sizing_label = "Fixed" if sizing_mode == "fixed" else "Half-Kelly"
    demo_label = "\U0001f4dd Demo: ON" if demo_on else "\U0001f4dd Demo: OFF"
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(at_label, callback_data="toggle_autotrade")],
        [InlineKeyboardButton(f"\U0001f4b5 Trade Amount: ${trade_amount:.2f}", callback_data="change_amount")],
        [InlineKeyboardButton(f"\U0001f4cf Sizing: {sizing_label}", callback_data="toggle_sizing")],
        [InlineKeyboardButton(demo_label, callback_data="toggle_demo")],
        [InlineKeyboardButton(f"\U0001f4b0 Demo Balance: ${demo_balance:.2f}", callback_data="change_demo_bankroll")],
        [InlineKeyboardButton("\U0001f504 Reset Demo", callback_data="reset_demo")],
        [InlineKeyboardButton("\U0001f519 Back to Menu", callback_data="cmd_menu")],
    ])


# ---------------------------------------------------------------------------
# Filter rows (Last 10 / Last 50 / All Time)
# ---------------------------------------------------------------------------

def signal_filter_row(active: str = "all") -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(
            ("[Last 10]" if active == "10" else "Last 10"),
            callback_data="signals_10",
        ),
        InlineKeyboardButton(
            ("[Last 50]" if active == "50" else "Last 50"),
            callback_data="signals_50",
        ),
        InlineKeyboardButton(
            ("[All Time]" if active == "all" else "All Time"),
            callback_data="signals_all",
        ),
    ]
    return InlineKeyboardMarkup([
        buttons,
        [InlineKeyboardButton("\U0001f519 Back to Menu", callback_data="cmd_menu")],
    ])


def trade_filter_row(active: str = "all", demo: bool = False) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(
            ("[Last 10]" if active == "10" else "Last 10"),
            callback_data="trades_10",
        ),
        InlineKeyboardButton(
            ("[Last 50]" if active == "50" else "Last 50"),
            callback_data="trades_50",
        ),
        InlineKeyboardButton(
            ("[All Time]" if active == "all" else "All Time"),
            callback_data="trades_all",
        ),
    ]
    # Demo / Real filter row
    demo_label = "[Demo]" if demo else "Demo"
    real_label = "[Real]" if not demo else "Real"
    mode_row = [
        InlineKeyboardButton(real_label, callback_data="trades_mode_real"),
        InlineKeyboardButton(demo_label, callback_data="trades_mode_demo"),
    ]
    return InlineKeyboardMarkup([
        buttons,
        mode_row,
        [InlineKeyboardButton("\U0001f519 Back to Menu", callback_data="cmd_menu")],
    ])


# ---------------------------------------------------------------------------
# Demo dashboard
# ---------------------------------------------------------------------------

def demo_dashboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("\U0001f4b0 Demo Trades", callback_data="trades_mode_demo")],
        [InlineKeyboardButton("\U0001f504 Reset Demo", callback_data="reset_demo")],
        [InlineKeyboardButton("\U0001f519 Back to Menu", callback_data="cmd_menu")],
    ])


# ---------------------------------------------------------------------------
# Back button only
# ---------------------------------------------------------------------------

def back_to_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("\U0001f519 Back to Menu", callback_data="cmd_menu")],
    ])
