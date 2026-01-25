"""Tests for LIC 9."""


from launch_interceptor_program.model import Point, Parameters

def make_params(**overrides):
    """Helper: create Parameters with defaults."""
    return Parameters(
        LENGTH1=1.0, RADIUS1=1.0, EPSILON=0.1, AREA1=1.0,
        Q_PTS=1, QUADS=1, DIST=1.0,
        N_PTS=1, K_PTS=1, A_PTS=1, B_PTS=1, C_PTS=1, D_PTS=1,
        E_PTS=1, F_PTS=1, G_PTS=1,
        LENGTH2=1.0, RADIUS2=1.0, AREA2=1.0,
        **overrides  # override specific ones
    )

def test_lic9_false_few_points():
    points = [(0.0, 0.0)] * 4
    params = make_params()
    assert not lic_9(points, params)

def test_lic9_true_angle_too_small():
    points = [(0,0), (1,0), (1,1), (2,0)]
    params = make_params(C_PTS=1, D_PTS=1, EPSILON=0.1)
    assert lic_9(points, params)
