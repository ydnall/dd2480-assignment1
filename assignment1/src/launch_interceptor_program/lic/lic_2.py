from math import pi

from ..model import Parameters, Points
from .geometry import angle


def lic_2(points: Points, parameters: Parameters) -> bool:
    """
    True if any 3 consecutive points form an angle < pi-eps or > pi+eps
    at the middle point.
    """
    if not 0 <= parameters.EPSILON < pi:
        raise ValueError("EPSILON must be larger than or equal to 0 and less than pi")

    for p1, p2, p3 in zip(points, points[1:], points[2:]):
        # Check if vertex coincides with either endpoint
        if p1 == p2 or p2 == p3:
            continue

        computed_angle = angle(p1, p2, p3)

        if computed_angle < (pi - parameters.EPSILON) or computed_angle > (
            pi + parameters.EPSILON
        ):
            return True

    return False
