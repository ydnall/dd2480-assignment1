from ..model import Parameters, Points
from .geometry import distance


def lic_7(points: Points, parameters: Parameters):
    NUMPOINTS = len(points)
    K_PTS = parameters.K_PTS
    LENGTH1 = parameters.LENGTH1

    if NUMPOINTS < 3:
        return False

    if not 1 <= K_PTS <= (NUMPOINTS - 2):
        raise ValueError(
            "K_PTS must be larger than or equal to 1 and less than or equal to (NUMPOINTS - 2)"
        )

    for start_index in range(0, NUMPOINTS - K_PTS - 1):
        first_point = points[start_index]
        second_point = points[start_index + K_PTS + 1]
        calculated_distance = distance(first_point, second_point)
        if calculated_distance > LENGTH1:
            return True

    return False
