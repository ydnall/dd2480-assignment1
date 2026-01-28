"""
LIC 9: Angle with separated points.
"""

from math import pi

from ..model import Parameters, Point
from .geometry import angle


def lic_9(points: list[Point], params: Parameters) -> bool:
    """LIC 9 implementation."""
    NUMPOINTS = len(points)
    if NUMPOINTS < 5:
        return False

    C_PTS = params.C_PTS
    D_PTS = params.D_PTS
    EPSILON = params.EPSILON

    if not 1 <= C_PTS:
        raise ValueError("C_PTS must be larger than or equal to 1")

    if not 1 <= D_PTS:
        raise ValueError("D_PTS must be larger than or equal to 1")

    if not (C_PTS + D_PTS) <= (NUMPOINTS - 3):
        raise ValueError(
            "(C_PTS + D_PTS) must be less than or eqaul to (NUMPOINTS - 3)"
        )

    for i in range(NUMPOINTS - C_PTS - D_PTS - 2):
        j = i + C_PTS + 1
        k = j + D_PTS + 1

        p1, vertex, p3 = points[i], points[j], points[k]

        if (p1[0] == vertex[0] and p1[1] == vertex[1]) or (
            p3[0] == vertex[0] and p3[1] == vertex[1]
        ):
            continue

        theta = angle(p1, vertex, p3)
        if theta < pi - EPSILON or theta > pi + EPSILON:
            return True

    return False
