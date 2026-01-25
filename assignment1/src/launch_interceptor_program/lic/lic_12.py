from ..model import Parameters, Points
from .geometry import distance

def lic_12(points: Points, parameters: Parameters) -> bool:
    """
    Simply check if there exist two pairs of points separated by K_PTS intervening points
    where one pair has distance > LENGTH1 and another has distance < LENGTH2.

    Both conditions must be met. Returns False if NUMPOINTS < 3.
    """
    n = len(points)

    # edge case
    if n < 3:
        return False
    
    k = parameters.K_PTS

    # flags for the lic 12 condition check
    found_greater = False
    found_less = False

    for i in range(n - k - 1):
        dist = distance(points[i], points[i + k + 1])

        if dist > parameters.LENGTH1:
            found_greater = True
        if dist < parameters.LENGTH2:
            found_less = True
        
    return found_greater and found_less

