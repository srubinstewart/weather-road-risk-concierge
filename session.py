# session.py
"""
A minimal in-memory session service that stores user preferences,
such as a default location. This demonstrates the 'Sessions & State'
concept required for the Capstone.
"""

class InMemorySessionService:
    """
    Very simple session helper to store a default location per user.
    Keyed by a user_id string.
    """

    def __init__(self):
        # Each user gets a small dictionary of settings.
        self._store = {}

    def set_default_location(self, user_id: str, location: str):
        """Store the user's preferred location."""
        self._store[user_id] = {"default_location": location}

    def get_default_location(self, user_id: str) -> str | None:
        """Retrieve the stored default location, if any."""
        data = self._store.get(user_id)
        if not data:
            return None
        return data.get("default_location")
