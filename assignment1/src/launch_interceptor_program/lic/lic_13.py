from ..model import Parameters, Points
from .geometry import circumradius

def lic_13(points: Points, parameters: Parameters) -> bool:
    """
    Here we check if there exist two triplets separated by A_PTS and B_PTS intervening points
    where one cannot fit in a circle of RADIUS1 and another can fit in RADIUS2.

    Both conditions must be met. Returns False if NUMPOINTS < 5.
    """
    n = len(points)
      
    # edge case
    if n < 5:
        return False
    
    a = parameters.A_PTS
    b = parameters.B_PTS

    # flags for lic 13 conditions
    found_cannot = False
    found_can = False

    for i in range(n - a - b - 2):
        p1 = points[i]
        p2 = points[i + a + 1]
        p3 = points[i + a + b + 2]

        r = circumradius(p1, p2, p3)

        if r > parameters.RADIUS1:
            found_cannot = True

        if r <= parameters.RADIUS2:
            found_can = True

    return found_cannot and found_can