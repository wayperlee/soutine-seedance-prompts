"""Soutine Seedance Prompts — thin reference to the Soutine landing page."""

LANDING = "https://soutine.ai/seedance-prompts"
HOMEPAGE = "https://soutine.ai/"

def open_landing() -> str:
    """Return the canonical deep-link URL for this prompt library."""
    return LANDING

__all__ = ["LANDING", "HOMEPAGE", "open_landing"]
__version__ = "0.1.0"
