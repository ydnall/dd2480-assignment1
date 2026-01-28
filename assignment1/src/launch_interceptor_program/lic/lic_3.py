from ..model import Parameters, Points
from .geometry import triangle_area


def lic_3(points: Points, parameters: Parameters) -> bool:
    """
    Ensures at least one set of three consecutive points are vertices of a triangle
    with area greater than AREA1.
    """
    if not 0 <= parameters.AREA1:
        raise ValueError("AREA1 must be larger than or equal to 0")

    NUMPOINTS = len(points)
    for i in range(NUMPOINTS - 2):
        area = triangle_area(points[i], points[i + 1], points[i + 2])
        if area > parameters.AREA1:
            return True

    return False
