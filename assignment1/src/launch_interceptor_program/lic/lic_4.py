from ..model import Parameters, Points
from .geometry import quadrant


def lic_4(points: Points, parameters: Parameters) -> bool:
    """
    Checks if there exists a set of Q_PTS consecutive points
    that lie in more than QUADS quadrants.
    """
    NUMPOINTS = len(points)

    if NUMPOINTS < parameters.Q_PTS:
        return False

    if not 2 <= parameters.Q_PTS <= NUMPOINTS:
        raise ValueError(
            "Q_PTS must be larger than or equal to 2 and less than or equal to NUMPOINTS"
        )

    if not 1 <= parameters.QUADS <= 3:
        raise ValueError(
            "QUADS must be larger than or equal to 1 and less than or equal to 3"
        )

    for i in range(NUMPOINTS - parameters.Q_PTS + 1):

        quadrants_in_window = set()

        for j in range(parameters.Q_PTS):
            current_point = points[i + j]
            q = quadrant(current_point)
            quadrants_in_window.add(q)

            if len(quadrants_in_window) > parameters.QUADS:
                return True

    return False
