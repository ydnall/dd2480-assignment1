import math

from launch_interceptor_program.lic.geometry import (
    angle,
    distance,
    min_enclosing_circle_radius,
    point_line_distance,
    quadrant,
    triangle_area,
)


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


def test_distance_horizontal():
    """Horizontal distance of 5 units"""
    result = distance((0, 0), (5, 0))
    assert result == 5.0


def test_distance_vertical():
    """Vertical distance of 3 units"""
    result = distance((0, 0), (0, 3))
    assert result == 3.0


def test_distance_diagonal():
    """3-4-5 right triangle diagonal"""
    result = distance((0, 0), (3, 4))
    assert result == 5.0


def test_distance_same_point():
    """Same point should have distance 0"""
    result = distance((2, 3), (2, 3))
    assert result == 0.0


def test_distance_between_different_points():
    """Distance between (0,1) and (0,0) should be 1"""
    result = distance((0, 1), (0, 0))
    assert result == 1.0


def test_distance_between_same_point():
    """Distance between the same point should be 0"""
    result = distance((5, 5), (5, 5))
    assert result == 0.0


def test_point_line_distance():
    """Distance between the point (3,4) and the line between (2,2) and (5,5) should be sqrt(2)/2"""
    result = point_line_distance((3, 4), (2, 2), (5, 5))
    assert result == math.sqrt(2) / 2


def test_distance_between_point_on_line_and_line():
    """Distance between a point on a line and the line should be 0"""
    result = point_line_distance((1, 1), (3, 3), (4, 4))
    assert result == 0.0


def test_quadrant_first():
    """Point in first quadrant (x >= 0, y >= 0)"""
    assert quadrant((1, 1)) == 1
    assert quadrant((5, 3)) == 1


def test_quadrant_second():
    """Point in second quadrant (x < 0, y >= 0)"""
    assert quadrant((-1, 1)) == 2
    assert quadrant((-3, 5)) == 2


def test_quadrant_third():
    """Point in third quadrant (x <= 0, y < 0)"""
    assert quadrant((-1, -1)) == 3
    assert quadrant((-5, -3)) == 3


def test_quadrant_fourth():
    """Point in fourth quadrant (x > 0, y < 0)"""
    assert quadrant((1, -1)) == 4
    assert quadrant((3, -5)) == 4


def test_quadrant_origin():
    """Origin should be in first quadrant (priority rule)"""
    assert quadrant((0, 0)) == 1


def test_quadrant_positive_x_axis():
    """Positive X-axis should be in first quadrant"""
    assert quadrant((5, 0)) == 1


def test_quadrant_negative_x_axis():
    """Negative X-axis should be in second quadrant (priority rule)"""
    assert quadrant((-5, 0)) == 2


def test_quadrant_positive_y_axis():
    """Positive Y-axis should be in first quadrant"""
    assert quadrant((0, 5)) == 1


def test_quadrant_negative_y_axis():
    """Negative Y-axis should be in third quadrant (priority rule)"""
    assert quadrant((0, -5)) == 3


def test_angle_right_angle():
    """90-degree angle should be pi/2 radians"""
    result = angle((1, 0), (0, 0), (0, 1))
    assert math.isclose(result, math.pi / 2, abs_tol=1e-9)


def test_angle_straight_line():
    """180-degree angle (straight line) should be pi radians"""
    result = angle((-1, 0), (0, 0), (1, 0))
    assert math.isclose(result, math.pi, abs_tol=1e-9)


def test_angle_acute():
    """45-degree angle should be pi/4 radians"""
    result = angle((1, 0), (0, 0), (1, 1))
    assert math.isclose(result, math.pi / 4, abs_tol=1e-9)


def test_angle_zero():
    """Zero-degree angle (coinciding points) should return 0"""
    result = angle((1, 0), (0, 0), (0, 0))
    assert result == 0.0


def test_angle_vertex_coincides_first_point():
    """When vertex coincides with first point, should return 0"""
    result = angle((0, 0), (0, 0), (1, 1))
    assert result == 0.0


def test_min_enclosing_circle_radius_equilateral_triangle():
    """Equilateral triangle with side 2 should have min_enclosing_circle_radius 2/sqrt(3)"""
    result = min_enclosing_circle_radius((0, 0), (2, 0), (1, math.sqrt(3)))
    expected = 2 / math.sqrt(3)
    assert math.isclose(result, expected, rel_tol=1e-12)


def test_min_enclosing_circle_radius_right_triangle():
    """Right triangle with legs 3,4 should have min_enclosing_circle_radius 2.5 (hypotenuse/2)"""
    result = min_enclosing_circle_radius((0, 0), (3, 0), (0, 4))
    assert math.isclose(result, 2.5, abs_tol=1e-12)


def test_min_enclosing_circle_radius_collinear_points():
    """Collinear points should return half the longest distance"""
    result = min_enclosing_circle_radius((0, 0), (1, 0), (2, 0))
    # Longest distance is 2, so min_enclosing_circle_radius is 1
    assert math.isclose(result, 1.0, abs_tol=1e-12)


def test_min_enclosing_circle_radius_obtuse_triangle():
    """Obtuse triangle should return half the longest side"""
    result = min_enclosing_circle_radius((0, 0), (1, 0), (0.5, 0.1))
    longest_side = distance((0, 0), (1, 0))
    assert math.isclose(result, longest_side / 2, abs_tol=1e-12)
