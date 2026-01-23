from ..model import Points, Parameters
from .geometry import triangle_area

def lic_14(points: Points, parameters: Parameters) -> bool:
    """
    This function checks if there exist two triplets separated by E_PTS and F_PTS 
    intervening points where one has area > AREA1 and another has area < AREA2.

    Both conditions must be met. Returns False if NUMPOINTS < 5.
    """
    n = len(points)

    # edge case
    if n < 5:
        return False
    
    e = parameters.E_PTS
    f = parameters.F_PTS

    # flags for lic 14 condition checks
    found_greater = False
    found_less = False

    for i in range(len(points) - e - f - 2):
        p1 = points[i]
        p2 = points[i + e + 1]
        p3 = points[i + e + f + 2]

        area = triangle_area(p1, p2, p3)

        if area > parameters.AREA1:
            found_greater = True

        if area < parameters.AREA2:
            found_less = True
            
    return found_greater and found_less