#CUSTOM CODE START
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class QuickCommandsEvent:
    """Event emitted when getQuickCommand response is received."""

    commands: list[dict[str, Any]]

#CUSTOM CODE END