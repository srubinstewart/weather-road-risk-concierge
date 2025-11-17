# tools.py
"""
Tool definitions for the Daily Weather and Road Risk Concierge Agent.

For the purposes of this capstone, get_weather() returns a simple,
hard-coded forecast. In a future version this could call a real
weather API or an MCP tool.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class WeatherForecast:
    location: str
    temperature_c: float
    precipitation: str  # "none", "snow", "rain", "mix"
    wind_kph: float
    summary: str


def get_weather(location: str, time_period: Optional[str] = None) -> WeatherForecast:
    """
    Very simple stub that returns a fake forecast.

    Args:
        location: A location string (e.g. ZIP code or town name).
        time_period: Optional text like "morning", "evening", "today".

    Returns:
        WeatherForecast: a small structured object.
    """
    # You can adjust these values later if you want.
    # For now, they just demonstrate the shape of the data.
    base_summary = f"Light snow with moderate winds in {location}"
    if time_period:
        base
