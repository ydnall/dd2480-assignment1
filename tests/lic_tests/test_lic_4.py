from launch_interceptor_program.lic.lic_4 import lic_4
from launch_interceptor_program.model import Parameters


def create_params(q_pts=0, quads=0, area1=0):
    """
    Helper function to create a Paramters object with default values.
    """
    return Parameters(
        LENGTH1=0,
        RADIUS1=0,
        EPSILON=0,
        AREA1=area1,
        Q_PTS=q_pts,
        QUADS=quads,
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


# unit test
def test_get_quadrant_axes():
    """Verify that points on axes follow priority rules (I > II > III > IV)"""
    from launch_interceptor_program.lic.geometry import quadrant

    assert quadrant((0, 0)) == 1  # Origo
    assert quadrant((-1, 0)) == 2  # Negativ X-axel
    assert quadrant((0, -1)) == 3  # Negativ Y-axel
    assert quadrant((1, -1)) == 4  # Standard Q4


def test_lic_4_true():
    """
    Test case where 3 consecutive points (Q_PTS=3) lie in tree different
    quadrants, which is more than the limit.
    """
    points = [(1, 1), (-1, 1), (-1, -1)]
    params = create_params(q_pts=3, quads=2)
    assert lic_4(points, params) is True


def test_lic_4_false():
    """
    Test case where the points lie in exactly quads quadrant
    """
    points = [(1, 1), (2, 2), (-1, 1)]  # Q1, Q1, Q2 (Totalt 2 unika)
    params = create_params(q_pts=3, quads=2)
    assert lic_4(points, params) is False


def test_lic_4_sliding_window():
    """
    Test case for the sliding window logic.
    """
    points = [
        (1, 1),
        (2, 2),  # Q1, Q1 (Början: bara 1 kvadrant)
        (1, 1),
        (-1, 1),
        (-1, -1),  # Här triggas det: Q1, Q2, Q3 (3 kvadranter!)
    ]
    params = create_params(q_pts=3, quads=2)
    assert lic_4(points, params) is True
