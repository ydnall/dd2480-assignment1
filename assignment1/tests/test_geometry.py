from launch_interceptor_program.lic.geometry import triangle_area, distance_between_points, distance_between_point_and_line

import math

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

def test_distance_between_different_points():
    """Distance between (0,1) and (0,0) should be 1"""
    result = distance_between_points((0,1), (0,0))
    assert result == 1.0

def test_distance_between_same_point():
    """Distance between the same point should be 0"""
    result = distance_between_points((5,5), (5,5))
    assert result == 0.0

def test_distance_between_point_and_line():
    """Distance between the point (3,4) and the line between (2,2) and (5,5) should be sqrt(2)/2"""
    result = distance_between_point_and_line((3,4), (2,2), (5,5))
    assert result == math.sqrt(2)/2

def test_distance_between_point_on_line_and_line():
    """Distance between a point on a line and the line should be 0"""
    result = distance_between_point_and_line((1,1), (3,3), (4,4))
    assert result == 0.0
