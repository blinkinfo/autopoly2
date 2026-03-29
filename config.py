"""AutoPoly configuration — loads from environment variables with sensible defaults."""

import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Polymarket
# ---------------------------------------------------------------------------
POLYMARKET_PRIVATE_KEY: str | None = os.getenv("POLYMARKET_PRIVATE_KEY")
POLYMARKET_FUNDER_ADDRESS: str | None = os.getenv("POLYMARKET_FUNDER_ADDRESS")
POLYMARKET_SIGNATURE_TYPE: int = int(os.getenv("POLYMARKET_SIGNATURE_TYPE", "2"))

CLOB_HOST: str = "https://clob.polymarket.com"
GAMMA_API_HOST: str = "https://gamma-api.polymarket.com"
CHAIN_ID: int = 137

# ---------------------------------------------------------------------------
# Telegram
# ---------------------------------------------------------------------------
TELEGRAM_BOT_TOKEN: str | None = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID: str | None = os.getenv("TELEGRAM_CHAT_ID")

# ---------------------------------------------------------------------------
# Trading
# ---------------------------------------------------------------------------
TRADE_AMOUNT_USDC: float = float(os.getenv("TRADE_AMOUNT_USDC", "1.0"))

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
DB_PATH: str = os.getenv("DB_PATH", "autopoly.db")

# ---------------------------------------------------------------------------
# Demo / Sizing defaults
# ---------------------------------------------------------------------------
DEFAULT_DEMO_BANKROLL: float = 100.0
DEFAULT_SIZING_MODE: str = "fixed"

# ---------------------------------------------------------------------------
# Strategy
# ---------------------------------------------------------------------------
SIGNAL_THRESHOLD: float = 0.53
SIGNAL_LEAD_TIME: int = 85  # seconds before slot end to check signal
