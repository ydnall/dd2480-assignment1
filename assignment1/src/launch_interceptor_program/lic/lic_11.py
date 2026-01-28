"""
LIC 11: X decreases over G_PTS points.
"""

from ..model import Parameters, Point


def lic_11(points: list[Point], params: Parameters) -> bool:
    NUMPOINTS = len(points)
    if NUMPOINTS < 3:
        return False

    G_PTS = params.G_PTS

    if not 1 <= G_PTS <= (NUMPOINTS - 2):
        raise ValueError(
            "G_PTS must be larger than or equal to 1 and less than or equal to (NUMPOINTS - 2)"
        )

    if G_PTS < 1 or G_PTS > NUMPOINTS - 2:
        return False

    for i in range(NUMPOINTS - G_PTS - 1):
        j = i + G_PTS + 1
        if points[j][0] < points[i][0]:  # Xj - Xi < 0
            return True

    return False
