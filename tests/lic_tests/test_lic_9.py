"""Tests for LIC 9."""

from launch_interceptor_program.lic.lic_9 import lic_9
from launch_interceptor_program.model import Parameters


def make_params(**overrides):
    defaults = {
        "LENGTH1": 1.0,
        "RADIUS1": 1.0,
        "EPSILON": 0.1,
        "AREA1": 1.0,
        "Q_PTS": 1,
        "QUADS": 1,
        "DIST": 1.0,
        "N_PTS": 1,
        "K_PTS": 1,
        "A_PTS": 1,
        "B_PTS": 1,
        "C_PTS": 1,
        "D_PTS": 1,
        "E_PTS": 1,
        "F_PTS": 1,
        "G_PTS": 1,
        "LENGTH2": 1.0,
        "RADIUS2": 1.0,
        "AREA2": 1.0,
    }
    defaults.update(overrides)
    return Parameters(**defaults)


def test_lic9_false_few_points():
    """Returns False when there aren’t enough points to form a (i, j, k) triple."""
    # needs at least 5 points when C_PTS=1 and D_PTS=1 because we use indices (0,2,4).
    points = [(0.0, 0.0)] * 4
    params = make_params(C_PTS=1, D_PTS=1, EPSILON=0.1)
    assert not lic_9(points, params)


def test_lic9_true_angle_too_small():
    """Returns True when the angle at the vertex is far from PI (e.g., ~90 degrees)."""
    # With C_PTS=1, D_PTS=1, indices are (0,2,4) so we need >= 5 points
    # Choose p0=(1,0), p2=(0,0) vertex, p4=(0,1) -> 90 degrees (pi/2), should be < pi-eps
    points = [(1, 0), (999, 999), (0, 0), (999, 999), (0, 1)]
    params = make_params(C_PTS=1, D_PTS=1, EPSILON=0.1)
    assert lic_9(points, params)


def test_lic9_false_straight_line():
    """Returns False when the points form a straight line (angle ~ PI)."""
    # p0=(-1,0), p2=(0,0) vertex, p4=(1,0) -> angle = pi, should be within [pi-eps, pi+eps]
    points = [(-1, 0), (999, 999), (0, 0), (999, 999), (1, 0)]
    params = make_params(C_PTS=1, D_PTS=1, EPSILON=0.1)
    assert not lic_9(points, params)


def test_lic9_false_when_point_coincides_with_vertex():
    """Returns False when the angle is undefined (a point coincides with the vertex)."""
    # p0 == vertex, should be skipped and return False
    points = [(0, 0), (999, 999), (0, 0), (999, 999), (1, 0)]
    params = make_params(C_PTS=1, D_PTS=1, EPSILON=0.1)
    assert not lic_9(points, params)
