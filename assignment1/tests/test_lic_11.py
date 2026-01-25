"""Tests for LIC 11."""

from launch_interceptor_program.lic.lic_11 import lic_11
from launch_interceptor_program.model import Parameters


def make_params(**overrides):
    """Create Parameters with defaults; override per test."""
    return Parameters(
        LENGTH1=1.0,
        RADIUS1=1.0,
        EPSILON=0.1,
        AREA1=1.0,
        Q_PTS=1,
        QUADS=1,
        DIST=1.0,
        N_PTS=1,
        K_PTS=1,
        A_PTS=1,
        B_PTS=1,
        C_PTS=1,
        D_PTS=1,
        E_PTS=1,
        F_PTS=1,
        G_PTS=1,
        LENGTH2=1.0,
        RADIUS2=1.0,
        AREA2=1.0,
        **overrides,
    )


def test_lic11_false_too_few_points():
    points = [(0.0, 0.0), (1.0, 0.0)]
    params = make_params(G_PTS=1)
    assert not lic_11(points, params)


def test_lic11_true_when_x_decreases():
    # i = 0 → (2, 0), j = 2 with G_PTS=1 → (-1, 0): x decreases (2 -> -1)
    points = [(2.0, 0.0), (0.0, 0.0), (-1.0, 0.0)]
    params = make_params(G_PTS=1)
    assert lic_11(points, params)


def test_lic11_false_when_x_does_not_decrease():
    points = [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0)]
    params = make_params(G_PTS=1)
    assert not lic_11(points, params)
