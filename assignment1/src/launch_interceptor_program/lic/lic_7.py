from ..model import Parameters, Points
from .geometry import distance


def lic_7(points: Points, parameters: Parameters):
    NUMPOINTS = len(points)
    K_PTS = parameters.K_PTS
    LENGTH1 = parameters.LENGTH1

    if NUMPOINTS < 3 or K_PTS < 1 or K_PTS > (NUMPOINTS - 2):
        return False

    for start_index in range(0, NUMPOINTS - K_PTS - 1):
        first_point = points[start_index]
        second_point = points[start_index + K_PTS + 1]
        calculated_distance = distance(first_point, second_point)
        if calculated_distance > LENGTH1:
            return True

    return False
