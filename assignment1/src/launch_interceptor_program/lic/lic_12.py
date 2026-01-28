from ..model import Parameters, Points
from .geometry import distance


def lic_12(points: Points, parameters: Parameters) -> bool:
    """
    Simply check if there exist two pairs of points separated by K_PTS intervening points
    where one pair has distance > LENGTH1 and another has distance < LENGTH2.

    Both conditions must be met. Returns False if NUMPOINTS < 3.
    """
    NUMPOINTS = len(points)

    # edge case
    if NUMPOINTS < 3:
        return False

    K_PTS = parameters.K_PTS
    LENGTH1 = parameters.LENGTH1
    LENGTH2 = parameters.LENGTH2

    if not 0 <= LENGTH2:
        raise ValueError("LENGTH2 must be larger than or equal to 0")

    # flags for the lic 12 condition check
    found_greater = False
    found_less = False

    for i in range(NUMPOINTS - K_PTS - 1):
        dist = distance(points[i], points[i + K_PTS + 1])

        if dist > LENGTH1:
            found_greater = True
        if dist < LENGTH2:
            found_less = True

    return found_greater and found_less
