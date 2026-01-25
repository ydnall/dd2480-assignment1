from launch_interceptor_program.lic.lic_7 import lic_7
from launch_interceptor_program.model import Parameters


def make_test_params(test_K_PTS, test_LENGTH1):
    return Parameters(
        LENGTH1=test_LENGTH1,
        RADIUS1=0.0,
        EPSILON=0.0,
        AREA1=0.0,
        Q_PTS=0,
        QUADS=0,
        DIST=0.0,
        N_PTS=0,
        K_PTS=test_K_PTS,
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


def test_lic_7_calculated_distance_greater_than_length1():
    """
    Contract: LIC 7 returns True when a calculated distance is greater than LENGTH1.

    Test case: Four points where the first and last point are separated by two points,
    and have a calculated distance of about 11, and LENGTH1 = 3.
    """
    parameters = make_test_params(2, 3)
    points = [(0, 0), (2, 2), (4, 4), (8, 8)]
    result = lic_7(points, parameters)
    assert result == True


def test_lic_7_calculated_distance_shorter_than_length1():
    """
    Contract: LIC 7 returns False when a calculated distance is shorter than LENGTH1.

    Test case: Four points where the first and last point are separated by two points,
    and have a calculated distance of about 11, and LENGTH1 = 12
    """
    parameters = make_test_params(2, 12)
    points = [(0, 0), (2, 2), (4, 4), (8, 8)]
    result = lic_7(points, parameters)
    assert result == False


def test_lic_7_less_than_3_total_points():
    """
    Contract: LIC 7 returns False when there are less than 3 points in total.

    Test case: Two points in total.
    """
    parameters = make_test_params(2, 3)
    points = [(0, 0), (1, 1)]
    result = lic_7(points, parameters)
    assert result == False
