from ..model import Parameters, Points
from .geometry import triangle_area


def lic_14(points: Points, parameters: Parameters) -> bool:
    """
    This function checks if there exist two triplets separated by E_PTS and F_PTS
    intervening points where one has area > AREA1 and another has area < AREA2.

    Both conditions must be met. Returns False if NUMPOINTS < 5.
    """
    NUMPOINTS = len(points)

    # edge case
    if NUMPOINTS < 5:
        return False

    E_PTS = parameters.E_PTS
    F_PTS = parameters.F_PTS
    AREA1 = parameters.AREA1
    AREA2 = parameters.AREA2

    if not 0 <= AREA2:
        raise ValueError("AREA2 must be larger than or equal to 0")

    # flags for lic 14 condition checks
    found_greater = False
    found_less = False

    for i in range(NUMPOINTS - E_PTS - F_PTS - 2):
        p1 = points[i]
        p2 = points[i + E_PTS + 1]
        p3 = points[i + E_PTS + F_PTS + 2]

        area = triangle_area(p1, p2, p3)

        if area > AREA1:
            found_greater = True

        if area < AREA2:
            found_less = True

    return found_greater and found_less
