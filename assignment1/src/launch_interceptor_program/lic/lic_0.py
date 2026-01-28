from ..model import Parameters, Points
from .geometry import distance


def lic_0(points: Points, parameters: Parameters) -> bool:
    """
    Returns True if there exists at least one pair of consecutive points
    whose distance is greater than LENGTH1.
    """
    if not 0 <= parameters.LENGTH1:
        raise ValueError("LENGTH1 must be larger than or equal to 0")

    for p1, p2 in zip(points, points[1:]):
        if distance(p1, p2) > parameters.LENGTH1:
            return True
    return False
