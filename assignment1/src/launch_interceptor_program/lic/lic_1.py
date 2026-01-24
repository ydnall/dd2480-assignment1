from ..model import Parameters, Points
from .geometry import circumcircle_radius

def lic_1(points: Points, parameters: Parameters) -> bool:
    """
    LIC-1: Determine whether any three consecutive data points require
    a circle with radius greater than RADIUS1 to enclose them.
    """
    for (p1, p2, p3) in zip(points, points[1:], points[2:]):
        if circumcircle_radius(p1, p2, p3) > parameters.RADIUS1:
            return True

    return False
