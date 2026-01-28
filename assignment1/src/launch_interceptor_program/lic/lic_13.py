from ..model import Parameters, Points
from .geometry import circumradius


def lic_13(points: Points, parameters: Parameters) -> bool:
    """
    Here we check if there exist two triplets separated by A_PTS and B_PTS intervening points
    where one cannot fit in a circle of RADIUS1 and another can fit in RADIUS2.

    Both conditions must be met. Returns False if NUMPOINTS < 5.
    """
    NUMPOINTS = len(points)

    # edge case
    if NUMPOINTS < 5:
        return False

    A_PTS = parameters.A_PTS
    B_PTS = parameters.B_PTS
    RADIUS1 = parameters.RADIUS1
    RADIUS2 = parameters.RADIUS2

    if not 0 <= RADIUS2:
        raise ValueError("RADIUS2 must be larger than or equal to 0")

    # flags for lic 13 conditions
    found_cannot = False
    found_can = False

    for i in range(NUMPOINTS - A_PTS - B_PTS - 2):
        p1 = points[i]
        p2 = points[i + A_PTS + 1]
        p3 = points[i + A_PTS + B_PTS + 2]

        r = circumradius(p1, p2, p3)

        if r > RADIUS1:
            found_cannot = True

        if r <= RADIUS2:
            found_can = True

    return found_cannot and found_can
