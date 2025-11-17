# agents.py
"""
Agent definitions for the Daily Weather and Road Risk Concierge.

This file contains:
- WeatherAgent      (gets raw forecast data)
- SafetyAgent       (turns forecast into risk analysis)
- CoordinatorAgent  (orchestrates the workflow)

The SafetyAgent uses a placeholder LLM class for simplicity.
You can later replace it with Gemini calls if you like.
"""

from typing import Optional
from tools import get_weather, WeatherForecast
from session import InMemorySessionService


# -----------------------------------------------------------
# Placeholder LLM Client (You can replace with Gemini later)
# -----------------------------------------------------------
class LLMClient:
    def generate(self, prompt: str) -> str:
        """
        Placeholder LLM response.
        This is intentionally simple for the capstone baseline.
        """
        return "Placeholder LLM response. Replace with Gemini call if desired."


# -----------------------------------------------------------
# WeatherAgent
# -----------------------------------------------------------
class WeatherAgent:
    """Agent responsible for retrieving or simulating weather data."""

    def handle(self, location: str, time_period: Optional[str] = None) -> WeatherForecast:
        return get_weather(location, time_period)


# -----------------------------------------------------------
# SafetyAgent
# -----------------------------------------------------------
class SafetyAgent:
    """Agent that interprets weather into road safety risk."""

    def __init__(self, llm: LLMClient):
        self.llm = llm

    def assess_risk(self, forecast: WeatherForecast) -> dict:
        """
        Produce a simple risk analysis.
        For the project, this returns a static dict.
        """
        # In a real implementation you’d call the LLM:
        # text = self.llm.generate(prompt)

        return {
            "risk_level": "moderate",
            "explanation": (
                "Light snow, below freezing temperatures, and moderate winds "
                "increase the chance of icy bridges and slick roads."
            ),
            "tips": [
                "Drive slower than usual.",
                "Increase following distance.",
                "Avoid sudden braking on bridges."
            ],
        }


# -----------------------------------------------------------
# CoordinatorAgent
# -----------------------------------------------------------
class CoordinatorAgent:
    """The top-level agent that orchestrates WeatherAgent and SafetyAgent."""

    def __init__(self, session_service: InMemorySessionService):
        self.session = session_service
        self.weather_agent = WeatherAgent()
        self.safety_agent = SafetyAgent(llm=LLMClient())

    def handle_message(self, user_id: str, message: str) -> str:
        message_lower = message.lower()

        # ---- Handle setting a default location --------------------------------
        if "set my default location to" in message_lower:
            parts = message_lower.split("set my default location to")
            location = parts[1].strip()
            self.session.set_default_location(user_id, location)
            return f"Got it. I will remember your default location as {location}."

        # ---- Determine which location to use -----------------------------------
        default_location = self.session.get_default_location_
