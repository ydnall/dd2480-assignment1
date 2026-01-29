from launch_interceptor_program.lic.lic_1 import lic_1
from launch_interceptor_program.model import Parameters


# Helper to create Parameters with only relevant fields set
def make_params(radius1=1.0):
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
        A_PTS=1,
        B_PTS=1,
        C_PTS=1,
        D_PTS=1,
        E_PTS=1,
        F_PTS=1,
        G_PTS=1,
        LENGTH2=0,
        RADIUS2=0,
        AREA2=0,
    )


def test_lic_1_radius_greater_than_radius1():
    """Three points require a circle with radius > RADIUS1"""
    points = [(0, 0), (2, 0), (0, 2)]  # min_enclosing_circle_radius = sqrt(2) ≈ 1.414
    params = make_params(radius1=1.0)
    assert lic_1(points, params) == True


def test_lic_1_radius_equal_to_radius1():
    """Radius equal to RADIUS1 should NOT satisfy (> strictly)"""
    points = [(0, 0), (2, 0), (0, 2)]  # min_enclosing_circle_radius ≈ 1.414
    params = make_params(radius1=(2**0.5))
    assert lic_1(points, params) == False


def test_lic_1_all_triplets_within_radius():
    """All consecutive triplets fit within or on the circle"""
    points = [(0, 0), (1, 0), (0, 1), (1, 1)]
    params = make_params(radius1=2.0)
    assert lic_1(points, params) == False


def test_lic_1_collinear_points_within_radius():
    """Collinear points with min_enclosing_circle_radius 1.0 are within RADIUS1=100.0"""
    points = [(0, 0), (1, 0), (2, 0)]  # min_enclosing_circle_radius = 1.0
    params = make_params(radius1=100.0)
    assert lic_1(points, params) == False


def test_lic_1_collinear_points_exceeds_radius():
    """Collinear points with min_enclosing_circle_radius 5.0 exceed RADIUS1=1.0"""
    points = [(0, 0), (5, 0), (10, 0)]  # min_enclosing_circle_radius = 5.0
    params = make_params(radius1=1.0)
    assert lic_1(points, params) == True


def test_lic_1_multiple_triplets_one_valid():
    """Multiple triplets, one violates the radius constraint"""
    points = [
        (0, 0),
        (0.5, 0),
        (0, 0.5),  # small triangle
        (0, 0),
        (5, 0),
        (0, 5),  # large triangle
    ]
    params = make_params(radius1=1.0)
    assert lic_1(points, params) == True


def test_lic_1_less_than_three_points():
    """Should return False with fewer than three points"""
    points = [(0, 0), (1, 0)]
    params = make_params(radius1=1.0)
    assert lic_1(points, params) == False


def test_lic_1_no_points():
    """Should return False with no points"""
    points = []
    params = make_params(radius1=1.0)
    assert lic_1(points, params) == False
