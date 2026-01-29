from launch_interceptor_program.lic.lic_14 import lic_14
from launch_interceptor_program.model import Parameters


def make_params(e_pts=1, f_pts=1, area1=1.0, area2=10.0):
    return Parameters(
        LENGTH1=0,
        RADIUS1=0,
        EPSILON=0,
        AREA1=area1,
        Q_PTS=2,
        QUADS=1,
        DIST=0,
        N_PTS=3,
        K_PTS=1,
        A_PTS=1,
        B_PTS=1,
        C_PTS=1,
        D_PTS=1,
        E_PTS=e_pts,
        F_PTS=f_pts,
        G_PTS=1,
        LENGTH2=0,
        RADIUS2=0,
        AREA2=area2,
    )


def test_lic_14_both_conditions_met():
    """Triplet with area between AREA1 and AREA2"""
    # Triangle (0,0), (2,0), (0,3) has area = 3
    points = [(0, 0), (0, 0), (2, 0), (0, 0), (0, 3)]
    params = make_params(e_pts=1, f_pts=1, area1=2.0, area2=5.0)
    assert lic_14(points, params) == True


def test_lic_14_fewer_than_5_points():
    """Should return False with < 5 points"""
    points = [(0, 0), (1, 0), (2, 0), (3, 0)]
    params = make_params()
    assert lic_14(points, params) == False


def test_lic_14_only_greater_condition_met():
    """Only AREA1 condition met"""
    points = [(0, 0), (0, 0), (2, 0), (0, 0), (0, 3)]  # area = 3
    params = make_params(area1=2.0, area2=2.5)  # 3 > 2 but 3 !< 2.5
    assert lic_14(points, params) == False


def test_lic_14_collinear_points():
    """Collinear points have area 0"""
    points = [(0, 0), (0, 0), (1, 0), (0, 0), (2, 0)]  # area = 0
    params = make_params(area1=0.0, area2=1.0)  # 0 !> 0, 0 < 1
    assert lic_14(points, params) == False
