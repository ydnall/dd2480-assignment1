"""
Shared input/output types for the Launch Interceptor Program.

These types model the DECIDE() inputs and outputs defined in the spec.
"""

from dataclasses import dataclass
from enum import IntEnum


class Connector(IntEnum):
    NOTUSED = 777
    ORR = 778
    ANDD = 779


@dataclass(frozen=True)
class Parameters:
    """Parameter bundle used by LIC evaluations."""
    LENGTH1: float
    RADIUS1: float
    EPSILON: float
    AREA1: float
    Q_PTS: int
    QUADS: int
    DIST: float
    N_PTS: int
    K_PTS: int
    A_PTS: int
    B_PTS: int
    C_PTS: int
    D_PTS: int
    E_PTS: int
    F_PTS: int
    G_PTS: int
    LENGTH2: float
    RADIUS2: float
    AREA2: float

Point = tuple[float, float]
Points = list[Point]

@dataclass(frozen=True)
class DecisionInput:
    """Grouped inputs for a DECIDE() evaluation."""
    POINTS: Points
    PARAMETERS: Parameters
    LCM: list[list[Connector]]
    PUV: list[bool]


@dataclass(frozen=True)
class DecisionResult:
    """DECIDE() output and intermediate vectors."""
    LAUNCH: bool
    CMV: list[bool]
    PUM: list[list[bool]]
    FUV: list[bool]
