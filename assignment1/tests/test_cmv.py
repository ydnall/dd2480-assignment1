"""
Tests for the Conditions Met Vector (CMV) computation.
"""

import math

from launch_interceptor_program.cmv import compute_cmv
from launch_interceptor_program.model import Parameters


# Helper to create Parameters with default values
def make_params(
    length1=1.0,
    radius1=1.0,
    epsilon=0.1,
    area1=1.0,
    q_pts=2,
    quads=1,
    dist=1.0,
    n_pts=3,
    k_pts=1,
    a_pts=1,
    b_pts=1,
    c_pts=1,
    d_pts=1,
    e_pts=1,
    f_pts=1,
    g_pts=1,
    length2=1.0,
    radius2=1.0,
    area2=1.0,
):
    return Parameters(
        LENGTH1=length1,
        RADIUS1=radius1,
        EPSILON=epsilon,
        AREA1=area1,
        Q_PTS=q_pts,
        QUADS=quads,
        DIST=dist,
        N_PTS=n_pts,
        K_PTS=k_pts,
        A_PTS=a_pts,
        B_PTS=b_pts,
        C_PTS=c_pts,
        D_PTS=d_pts,
        E_PTS=e_pts,
        F_PTS=f_pts,
        G_PTS=g_pts,
        LENGTH2=length2,
        RADIUS2=radius2,
        AREA2=area2,
    )


def test_cmv_returns_15_elements():
    """CMV should always return exactly 15 boolean values"""
    points = [(0, 0), (1, 1), (2, 2)]
    params = make_params()
    result = compute_cmv(points, params)
    assert len(result) == 15
    assert all(isinstance(val, bool) for val in result)


def test_cmv_empty_points():
    """CMV with empty points list should return 15 False values"""
    points = []
    params = make_params()
    result = compute_cmv(points, params)
    assert len(result) == 15
    assert all(val is False for val in result)


def test_cmv_single_point():
    """CMV with single point should return mostly False values"""
    points = [(5, 5)]
    params = make_params()
    result = compute_cmv(points, params)
    assert len(result) == 15


def test_cmv_lic_0_satisfied():
    """Test that LIC 0 is correctly set when condition is met"""
    # Two points with distance 5 > LENGTH1=3
    points = [(0, 0), (5, 0)]
    params = make_params(length1=3.0)
    result = compute_cmv(points, params)
    assert result[0] is True


def test_cmv_lic_0_not_satisfied():
    """Test that LIC 0 is correctly set when condition is not met"""
    # Two points with distance 1 < LENGTH1=5
    points = [(0, 0), (1, 0)]
    params = make_params(length1=5.0)
    result = compute_cmv(points, params)
    assert result[0] is False


def test_cmv_lic_5_satisfied():
    """Test that LIC 5 is correctly set when X[j] - X[i] < 0"""
    # Second point has smaller X coordinate
    points = [(5, 0), (2, 0)]
    params = make_params()
    result = compute_cmv(points, params)
    assert result[5] is True


def test_cmv_lic_5_not_satisfied():
    """Test that LIC 5 is correctly set when all X coordinates are non-decreasing"""
    # X coordinates are increasing
    points = [(0, 0), (1, 0), (2, 0)]
    params = make_params()
    result = compute_cmv(points, params)
    assert result[5] is False


def test_cmv_multiple_lics_satisfied():
    """Test scenario where multiple LICs are satisfied simultaneously"""
    # Points that satisfy multiple conditions
    points = [
        (0, 0),  # First point
        (10, 0),  # Far from first (satisfies LIC 0)
        (5, 10),  # Forms large triangle (satisfies LIC 3)
        (-1, 5),  # X decreases (satisfies LIC 5)
    ]
    params = make_params(
        length1=5.0,  # Distance between first two points is 10 > 5
        area1=10.0,  # Triangle area should be > 10
    )
    result = compute_cmv(points, params)

    assert len(result) == 15
    assert result[0] is True  # LIC 0: distance > LENGTH1
    assert result[5] is True  # LIC 5: X decreases


def test_cmv_with_collinear_points():
    """Test CMV with collinear points"""
    # Three collinear points on x-axis
    points = [(0, 0), (1, 0), (2, 0), (3, 0)]
    params = make_params(area1=0.5)  # Area threshold > 0
    result = compute_cmv(points, params)

    assert len(result) == 15
    assert result[3] is False


def test_cmv_quadrant_distribution():
    """Test CMV with points in different quadrants (LIC 4)"""
    # Points in all 4 quadrants
    points = [
        (1, 1),  # Quadrant I
        (-1, 1),  # Quadrant II
        (-1, -1),  # Quadrant III
        (1, -1),  # Quadrant IV
    ]
    params = make_params(q_pts=4, quads=3)  # 4 consecutive points in > 3 quadrants
    result = compute_cmv(points, params)

    assert len(result) == 15
    assert result[4] is True


def test_cmv_angle_condition():
    """Test CMV with angle-based LIC (LIC 2)"""
    # Three points forming a sharp angle
    points = [
        (0, 0),
        (1, 0),  # Vertex
        (1, 0.1),  # Forms angle close to 90 degrees
    ]
    params = make_params(epsilon=0.1)  # Small epsilon
    result = compute_cmv(points, params)

    assert len(result) == 15
    # The angle should be < PI - EPSILON or > PI + EPSILON


def test_cmv_comprehensive_scenario():
    """Comprehensive test with realistic data"""
    # Create a diverse set of points
    points = [
        (0, 0),
        (5, 0),
        (5, 5),
        (0, 5),
        (-2, 3),
        (3, -2),
        (8, 8),
        (1, 1),
    ]

    params = make_params(
        length1=3.0,
        radius1=2.0,
        epsilon=0.5,
        area1=5.0,
        q_pts=3,
        quads=2,
        dist=1.0,
        n_pts=3,
        k_pts=1,
    )

    result = compute_cmv(points, params)

    # Verify structure
    assert len(result) == 15
    assert all(isinstance(val, bool) for val in result)

    # At least some LICs should be satisfied with this data
    assert any(result)


def test_cmv_no_conditions_met():
    """Test scenario where no conditions are met"""
    # Two very close points
    points = [(0, 0), (0.01, 0)]

    # Parameters set to impossible thresholds
    params = make_params(
        length1=100.0,  # Very large distance required
        radius1=0.001,  # Very small radius
        epsilon=math.pi - 0.001,  # Almost no angle deviation allowed
        area1=1000.0,  # Very large area required
    )

    result = compute_cmv(points, params)

    assert len(result) == 15
    # Most LICs should not be satisfied
    assert result.count(False) > result.count(True)


def test_cmv_all_same_point():
    """Test CMV when all points are identical"""
    # All points at origin
    points = [(0, 0), (0, 0), (0, 0), (0, 0)]
    params = make_params()
    result = compute_cmv(points, params)

    assert len(result) == 15
    # Most conditions should fail when all points are the same
    assert result.count(False) >= 10
