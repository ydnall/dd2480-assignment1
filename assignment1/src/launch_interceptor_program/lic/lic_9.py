"""
LIC 9: Angle with separated points.
"""
import math
from ..model import Point, Parameters
from .geometry import angle

def lic_9(points: list[Point], params: Parameters) -> bool:
    """LIC 9 implementation."""
    n = len(points)
    if n < 5:
        return False
    
    c_pts = params.C_PTS
    d_pts = params.D_PTS
    epsilon = params.EPSILON
    
    if c_pts < 1 or d_pts < 1 or c_pts + d_pts > n - 3:
        return False
    
    for i in range(n - c_pts - d_pts - 2):
        j = i + c_pts + 1
        k = j + d_pts + 1
        
        p1, vertex, p3 = points[i], points[j], points[k]
        
        if (p1[0] == vertex[0] and p1[1] == vertex[1]) or \
           (p3[0] == vertex[0] and p3[1] == vertex[1]):
            continue
        
        theta = angle(p1, vertex, p3)
        if theta < math.pi - epsilon or theta > math.pi + epsilon:
            return True
    
    return False
