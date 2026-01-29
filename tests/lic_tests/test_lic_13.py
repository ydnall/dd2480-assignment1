from launch_interceptor_program.lic.lic_13 import lic_13
from launch_interceptor_program.model import Parameters


def make_params(a_pts=1, b_pts=1, radius1=1.0, radius2=10.0):
    return Parameters(
        LENGTH1=0,
        RADIUS1=radius1,
        EPSILON=0,
        AREA1=0,
        Q_PTS=2,
        QUADS=1,
        DIST=0,
        N_PTS=3,
        K_PTS=1,
        A_PTS=a_pts,
        B_PTS=b_pts,
        C_PTS=1,
        D_PTS=1,
        E_PTS=1,
        F_PTS=1,
        G_PTS=1,
        LENGTH2=0,
        RADIUS2=radius2,
        AREA2=0,
    )


def test_lic_13_both_conditions_met():
    """Triplet with min_enclosing_circle_radius between RADIUS1 and RADIUS2"""
    points = [(0, 0), (0, 0), (3, 0), (0, 0), (0, 4)]  # right triangle 3-4-5, R=2.5
    params = make_params(a_pts=1, b_pts=1, radius1=2.0, radius2=3.0)
    assert lic_13(points, params) == True


def test_lic_13_fewer_than_5_points():
    """Should return False with < 5 points"""
    points = [(0, 0), (1, 0), (2, 0), (3, 0)]
    params = make_params()
    assert lic_13(points, params) == False


def test_lic_13_only_cannot_contain_met():
    """Only RADIUS1 condition met"""
    points = [(0, 0), (0, 0), (3, 0), (0, 0), (0, 4)]  # R=2.5
    params = make_params(radius1=2.0, radius2=2.0)  # 2.5 > 2.0 but 2.5 !<= 2.0
    assert lic_13(points, params) == False
