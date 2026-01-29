from launch_interceptor_program.lic.lic_8 import lic_8
from launch_interceptor_program.model import Parameters


def make_test_params(test_A_PTS, test_B_PTS, test_RADIUS1):
    return Parameters(
        LENGTH1=0.0,
        RADIUS1=test_RADIUS1,
        EPSILON=0.0,
        AREA1=0.0,
        Q_PTS=0,
        QUADS=0,
        DIST=0.0,
        N_PTS=0,
        K_PTS=0,
        A_PTS=test_A_PTS,
        B_PTS=test_B_PTS,
        C_PTS=0,
        D_PTS=0,
        E_PTS=0,
        F_PTS=0,
        G_PTS=0,
        LENGTH2=0.0,
        RADIUS2=0.0,
        AREA2=0.0,
    )


def test_lic_8_min_enclosing_circle_radius_bigger_than_radius1():
    """
    Contract: LIC 8 returns True when the min_enclosing_circle_radius of three points is bigger than RADIUS1.

    Test case: Six points where the first and third is separated by one point, and the third
    and sixth is separated by two points. The min_enclosing_circle_radius of the first, third and sixth point
    is about 4, and RADIUS1 = 2.
    """
    parameters = make_test_params(1, 2, 2)
    points = [(1, 1), (2, 5), (4, 4), (6, 3), (7, 7), (8, 2)]
    result = lic_8(points, parameters)
    assert result == True


def test_lic_8_min_enclosing_circle_radius_smaller_than_radius1():
    """
    Contract: LIC 8 returns False when the min_enclosing_circle_radius of three points is smaller than RADIUS1.

    Test case: Six points where the first and third is separated by one point, and the third
    and sixth is separated by two points. The min_enclosing_circle_radius of the first, third and sixth point
    is about 4, and RADIUS1 = 5.
    """
    parameters = make_test_params(1, 2, 5)
    points = [(1, 1), (2, 5), (4, 4), (6, 3), (7, 7), (8, 2)]
    result = lic_8(points, parameters)
    assert result == False


def test_lic_8_less_than_5_total_points():
    """
    Contract: LIC 8 returns False when there are less than 5 points in total.

    Test case: Three points in total.
    """
    parameters = make_test_params(1, 2, 3)
    points = [(1, 1), (4, 4), (8, 2)]
    result = lic_8(points, parameters)
    assert result == False
