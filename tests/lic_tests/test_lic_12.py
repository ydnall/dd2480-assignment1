from launch_interceptor_program.lic.lic_12 import lic_12
from launch_interceptor_program.model import Parameters


# Helper to create Parameters with only relevant fields set
def make_params(k_pts=1, length1=1.0, length2=10.0):
    return Parameters(
        LENGTH1=length1,
        RADIUS1=0,
        EPSILON=0,
        AREA1=0,
        Q_PTS=2,
        QUADS=1,
        DIST=0,
        N_PTS=3,
        K_PTS=k_pts,
        A_PTS=1,
        B_PTS=1,
        C_PTS=1,
        D_PTS=1,
        E_PTS=1,
        F_PTS=1,
        G_PTS=1,
        LENGTH2=length2,
        RADIUS2=0,
        AREA2=0,
    )


def test_lic_12_both_conditions_met():
    """Points with distances both > LENGTH1 and < LENGTH2"""
    points = [(0, 0), (0, 0), (5, 0)]  # K_PTS=1, distance=5
    params = make_params(k_pts=1, length1=3.0, length2=10.0)
    assert lic_12(points, params) == True


def test_lic_12_fewer_than_3_points():
    """Should return False with < 3 points"""
    points = [(0, 0), (1, 1)]
    params = make_params()
    assert lic_12(points, params) == False


def test_lic_12_only_greater_condition_met():
    """Only LENGTH1 condition met, not LENGTH2"""
    points = [(0, 0), (0, 0), (5, 0)]
    params = make_params(k_pts=1, length1=3.0, length2=4.0)  # 5 > 3 but 5 !< 4
    assert lic_12(points, params) == False
