"""Tests for LIC 10."""

from launch_interceptor_program.lic.lic_10 import lic_10
from launch_interceptor_program.model import Parameters


def make_params(**overrides):
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


def test_lic10_false_few_points():
    points = [(0.0, 0.0)] * 4
    params = make_params(E_PTS=1, F_PTS=1, AREA1=0.5)
    assert not lic_10(points, params)


def test_lic10_true_large_area():
    # With E_PTS=1, F_PTS=1, indices are (0,2,4) so we need at least 5 points
    points = [(0, 0), (999, 999), (1, 0), (999, 999), (0, 2)]
    params = make_params(E_PTS=1, F_PTS=1, AREA1=0.5)
    assert lic_10(points, params)


def test_lic10_false_small_area():
    points = [(0, 0), (999, 999), (1, 0), (999, 999), (0, 0.2)]
    params = make_params(E_PTS=1, F_PTS=1, AREA1=0.5)
    assert not lic_10(points, params)
