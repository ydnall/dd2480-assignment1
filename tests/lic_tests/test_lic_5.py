from launch_interceptor_program.lic.lic_5 import lic_5
from launch_interceptor_program.model import Parameters


def make_params():
    """Helper to create empty parameters for LIC 5."""
    return Parameters(
        LENGTH1=0,
        RADIUS1=0,
        EPSILON=0,
        AREA1=0,
        Q_PTS=0,
        QUADS=0,
        DIST=0,
        N_PTS=0,
        K_PTS=0,
        A_PTS=0,
        B_PTS=0,
        C_PTS=0,
        D_PTS=0,
        E_PTS=0,
        F_PTS=0,
        G_PTS=0,
        LENGTH2=0,
        RADIUS2=0,
        AREA2=0,
    )


def test_lic_5_true():
    """Positive test: X decreases from 5 to 4."""
    points = [(5, 10), (4, 11)]
    params = make_params()
    assert lic_5(points, params) is True


def test_lic_5_exact_zero_diff():
    """Edge case: X-coordinates are identical. Should be False because 0 is not < 0."""
    points = [(10, 5), (10, 8)]
    params = make_params()
    assert lic_5(points, params) is False


def test_lic_5_too_few_points():
    """Negative test: Only one point, cannot compare with a 'next' point."""
    points = [(1, 1)]
    params = make_params()
    assert lic_5(points, params) is False


def test_lic_5_no_points():
    """Negative test: Completely empty list."""
    points = []
    params = make_params()
    assert lic_5(points, params) is False
