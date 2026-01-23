from launch_interceptor_program.lic.geometry import triangle_area


def test_triangle_area_unit_triangle():
    """Unit right triangle should have area 0.5"""
    result = triangle_area((0, 0), (1, 0), (0, 1))
    assert result == 0.5

def test_triangle_area_collinear_points():
    """Collinear points should have area 0"""
    result = triangle_area((0, 0), (1, 1), (2, 2))
    assert result == 0.0

def test_triangle_area_known_triangle():
    """Triangle with base 2, height 3 should have area 3"""
    result = triangle_area((0, 0), (2, 0), (0, 3))
    assert result == 3.0
