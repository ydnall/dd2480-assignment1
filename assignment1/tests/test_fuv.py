"""
Tests for the (FUV) computation.
"""

from launch_interceptor_program.fuv import compute_fuv


def test_fuv_returns_15_elements():  # Ändrad från fuv_test_...
    """FUV should always return exactly 15 boolean values"""
    pum = [[True for _ in range(15)] for _ in range(15)]
    puv = [True] * 15
    result = compute_fuv(pum, puv)
    assert len(result) == 15
    assert all(isinstance(val, bool) for val in result)


def test_fuv_puv_false():  # Ändrad
    """FUV[i] should be True if PUV[i] is False"""
    pum = [[False for _ in range(15)] for _ in range(15)]
    puv = [False] * 15
    puv[0] = False

    result = compute_fuv(pum, puv)
    assert result[0] is True


def test_fuv_pum_row_all_true():  # Ändrad
    """FUV[i] should be True if PUV[i] is True and all PUM row elements are True"""
    pum = [[True for _ in range(15)] for _ in range(15)]
    puv = [True] * 15

    result = compute_fuv(pum, puv)
    assert result[0] is True


def test_fuv_pum_row_contains_false():  # Ändrad
    """FUV[i] should be False if PUV[i] is True and any PUM row element is False"""
    pum = [[True for _ in range(15)] for _ in range(15)]
    pum[0][1] = False

    puv = [True] * 15

    result = compute_fuv(pum, puv)
    assert result[0] is False


def test_fuv_ignores_diagonal():  # Ändrad
    """FUV computation should ignore the diagonal element PUM[i][i]"""
    pum = [[True for _ in range(15)] for _ in range(15)]
    pum[0][0] = False

    puv = [True] * 15

    result = compute_fuv(pum, puv)
    assert result[0] is True
