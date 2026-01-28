from ..model import Parameters, Points
from .geometry import distance, point_line_distance


def lic_6(points: Points, parameters: Parameters):
    NUMPOINTS = len(points)
    N_PTS = parameters.N_PTS
    DIST = parameters.DIST

    if NUMPOINTS < 3:
        return False

    if not 3 <= N_PTS <= NUMPOINTS:
        raise ValueError(
            "N_PTS must be larger than or equal to 3 or less than or equal to NUMPOINTS"
        )

    if not 0 <= DIST:
        raise ValueError("DIST must be larger than or equal to 0")

    for start_index in range(0, (NUMPOINTS - N_PTS) + 1):
        current_set = []
        for i in range(start_index, start_index + N_PTS):
            current_set.append(points[i])
        if current_set[0] == current_set[N_PTS - 1]:
            for current_point in range(1, N_PTS - 1):
                calculated_distance = distance(
                    current_set[0], current_set[current_point]
                )
                if DIST < calculated_distance:
                    return True
        else:
            for current_point in range(1, N_PTS - 1):
                calculated_distance = point_line_distance(
                    current_set[current_point], current_set[0], current_set[N_PTS - 1]
                )
                if DIST < calculated_distance:
                    return True
    return False
