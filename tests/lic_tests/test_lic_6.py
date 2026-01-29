from launch_interceptor_program.lic.lic_6 import lic_6
from launch_interceptor_program.model import Parameters


def make_test_params(test_N_PTS, test_DIST):
    return Parameters(
        LENGTH1=0.0,
        RADIUS1=0.0,
        EPSILON=0.0,
        AREA1=0.0,
        Q_PTS=0,
        QUADS=0,
        DIST=test_DIST,
        N_PTS=test_N_PTS,
        K_PTS=0,
        A_PTS=0,
        B_PTS=0,
        C_PTS=0,
        D_PTS=0,
        E_PTS=0,
        F_PTS=0,
        G_PTS=0,
        LENGTH2=0.0,
        RADIUS2=0.0,
        AREA2=0.0,
    )


def test_lic_6_calculated_distance_greater_than_dist():
    """
    Contract: LIC 6 returns True when a calculated distance is greater than DIST.

    Test case: Three points where the middle point has a calculated distance of about 2 from the line between the two other points.
    """
    parameters = make_test_params(3, 1)
    points = [(0, 0), (1, 4), (2, 2)]
    result = lic_6(points, parameters)
    assert result == True


def test_lic_6_calculate_distance_shorter_than_dist():
    """
    Contract: LIC 6 returns False when a calculated distance is shorter than DIST.

    Test case: Five points where the first and last point are the same, and the
    middle points have a calculated distance of about 2, about 4 and about 6 from
    the first/last point.
    """
    parameters = make_test_params(5, 7)
    points = [(0, 0), (2, 2), (3, 3), (4, 4), (0, 0)]
    result = lic_6(points, parameters)
    assert result == False


def test_lic_6_less_than_3_total_points():
    """
    Contract: LIC 6 returns False when there are less than 3 total points.

    Test case: Two total points.
    """
    parameters = make_test_params(3, 1)
    points = [(0, 0), (1, 1)]
    result = lic_6(points, parameters)
    assert result == False
