from launch_interceptor_program.lic.lic_2 import lic_2
from launch_interceptor_program.model import Parameters


# Helper to create Parameters with only relevant fields set
def make_params(epsilon=0.1):
    return Parameters(
        LENGTH1=0,
        RADIUS1=0,
        EPSILON=epsilon,
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


def test_lic_2_acute_angle():
    """Three points forming an acute angle (< PI - EPSILON)"""
    points = [(0, 0), (1, 0), (1, 1)]  # 90 degree angle at (1,0)
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == True


def test_lic_2_sharp_turn():
    """Three points with a sharp turn significantly less than PI"""
    points = [(0, 0), (1, 0), (0.5, 1)]  # Sharp angle
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == True


def test_lic_2_straight_line():
    """Three collinear points forming angle = PI (straight line)"""
    points = [(0, 0), (1, 0), (2, 0)]  # Perfectly straight
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == False


def test_lic_2_nearly_straight_within_epsilon():
    """Angle close to PI but within EPSILON tolerance"""
    # Create points nearly collinear
    points = [(0, 0), (1, 0), (2, 0.01)]  # Very slight deviation
    params = make_params(epsilon=1.0)  # Large epsilon
    assert lic_2(points, params) == False


def test_lic_2_vertex_coincides_with_first():
    """Vertex coincides with first point - angle undefined"""
    points = [(1, 1), (1, 1), (2, 2)]  # p1 == p2
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == False


def test_lic_2_vertex_coincides_with_last():
    """Vertex coincides with last point - angle undefined"""
    points = [(0, 0), (1, 1), (1, 1)]  # p2 == p3
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == False


def test_lic_2_all_points_same():
    """All three points coincide"""
    points = [(1, 1), (1, 1), (1, 1)]
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == False


def test_lic_2_fewer_than_3_points():
    """Should return False with < 3 points"""
    points = [(0, 0), (1, 1)]
    params = make_params()
    assert lic_2(points, params) == False


def test_lic_2_exactly_3_points_valid():
    """Exactly 3 points forming valid angle"""
    points = [(0, 0), (1, 0), (1, 1)]
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == True


def test_lic_2_multiple_triplets_first_valid():
    """Multiple triplets, first one satisfies condition"""
    points = [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)]  # First triplet has 90° angle
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == True


def test_lic_2_multiple_triplets_last_valid():
    """Multiple triplets, only last one satisfies condition"""
    points = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]  # Last triplet has 90° angle
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == True


def test_lic_2_multiple_triplets_none_valid():
    """Multiple triplets, all collinear (straight lines)"""
    points = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]  # All collinear
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == False


def test_lic_2_epsilon_zero():
    """EPSILON = 0, any deviation from PI should satisfy"""
    points = [(0, 0), (1, 0), (2, 0.001)]  # Tiny deviation
    params = make_params(epsilon=0.0)
    assert lic_2(points, params) == True


def test_lic_2_right_angle():
    """Perfect 90 degree angle (PI/2)"""
    points = [(0, 0), (0, 0), (0, 1), (1, 1)]
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == True


def test_lic_2_obtuse_angle():
    """Obtuse angle (between PI/2 and PI)"""
    points = [(0, 0), (1, 0), (0.5, 0.2)]  # Creates obtuse angle
    params = make_params(epsilon=0.1)
    assert lic_2(points, params) == True
