from launch_interceptor_program.lic.lic_3 import lic_3
from launch_interceptor_program.model import Parameters


def make_params(area1):
    """Helper to create parameters with a specific AREA1."""
    return Parameters(
        LENGTH1=0,
        RADIUS1=0,
        EPSILON=0,
        AREA1=area1,
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


def test_lic_3_true_case():
    """Positive test: Triangle with area 1.0 is greater than AREA1=0.5."""
    points = [(0, 0), (2, 0), (0, 1)]  # Area is 1.0
    params = make_params(0.5)
    assert lic_3(points, params) is True


def test_lic_3_false_small_area():
    """Negative test: Triangle with area 1.0 is NOT greater than AREA1=2.0."""
    points = [(0, 0), (2, 0), (0, 1)]  # Area is 1.0
    params = make_params(2.0)
    assert lic_3(points, params) is False


def test_lic_3_edge_case_equal():
    """Edge case: Area is exactly AREA1. Should be False because it must be GREATER than."""
    points = [(0, 0), (2, 0), (0, 1)]  # Area is 1.0
    params = make_params(1.0)
    assert lic_3(points, params) is False
