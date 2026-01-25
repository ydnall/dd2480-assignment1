from launch_interceptor_program.lic.lic_0 import lic_0
from launch_interceptor_program.model import Parameters

# Helper to create Parameters with only relevant fields set
def make_params(length1=1.0):
    return Parameters(
        LENGTH1=length1, RADIUS1=0, EPSILON=0, AREA1=0,
        Q_PTS=2, QUADS=1, DIST=0, N_PTS=3, K_PTS=1,
        A_PTS=1, B_PTS=1, C_PTS=1, D_PTS=1,
        E_PTS=1, F_PTS=1, G_PTS=1,
        LENGTH2=0, RADIUS2=0, AREA2=0
    )


def test_lic_0_distance_greater_than_length1():
    """At least one pair of consecutive points has distance > LENGTH1"""
    points = [(0, 0), (5, 0)]  # distance = 5
    params = make_params(length1=3.0)
    assert lic_0(points, params) == True


def test_lic_0_distance_equal_to_length1():
    """Distance equal to LENGTH1 should NOT satisfy (> strictly)"""
    points = [(0, 0), (3, 0)]  # distance = 3
    params = make_params(length1=3.0)
    assert lic_0(points, params) == False


def test_lic_0_all_distances_less_than_length1():
    """All consecutive distances < LENGTH1"""
    points = [(0, 0), (1, 0), (2, 0)]
    params = make_params(length1=5.0)
    assert lic_0(points, params) == False


def test_lic_0_multiple_pairs_one_valid():
    """Multiple pairs, one satisfies the condition"""
    points = [(0, 0), (1, 0), (10, 0)]  # distances: 1, 9
    params = make_params(length1=5.0)
    assert lic_0(points, params) == True


def test_lic_0_single_point():
    """Should return False with only one point"""
    points = [(0, 0)]
    params = make_params(length1=1.0)
    assert lic_0(points, params) == False


def test_lic_0_no_points():
    """Should return False with no points"""
    points = []
    params = make_params(length1=1.0)
    assert lic_0(points, params) == False
