from ..model import Parameters, Points
from .geometry import circumradius


def lic_1(points: Points, parameters: Parameters) -> bool:
    """
    LIC-1: Determine whether any three consecutive data points require
    a circle with radius greater than RADIUS1 to enclose them.
    """
    if not 0 <= parameters.RADIUS1:
        raise ValueError("RADIUS1 must be larger than or equal to 0")

    for p1, p2, p3 in zip(points, points[1:], points[2:]):
        if circumradius(p1, p2, p3) > parameters.RADIUS1:
            return True

    return False
