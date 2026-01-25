from ..model import Parameters, Points
import math

def lic_2(points: Points, parameters: Parameters) -> bool:
    epsilon = parameters.EPSILON
    
    for (p1, p2, p3) in zip(points, points[1:], points[2:]):
        # Check if vertex coincides with either endpoint
        if p1 == p2 or p2 == p3:
            continue
        
        v1_x = p1[0] - p2[0]
        v1_y = p1[1] - p2[1]
        v2_x = p3[0] - p2[0]
        v2_y = p3[1] - p2[1]
        
        # The dot product equation says that:
        # dot_product = mag_v1 * mag_v2 * cos_angle
        # What we want is the cos_angle, and in this equation,
        # we already know all the other components, so we can just
        # step by step extract the angle.
        dot_product = v1_x * v2_x + v1_y * v2_y
        
        mag_v1 = math.sqrt(v1_x**2 + v1_y**2)
        mag_v2 = math.sqrt(v2_x**2 + v2_y**2)

        cos_angle = dot_product / (mag_v1 * mag_v2)
        
        # Mathematically not necessary but we need it in case
        # python approximates values.
        cos_angle = max(-1.0, min(1.0, cos_angle))

        # We need the radians form to compare with pi and epsilon
        angle = math.acos(cos_angle)
        
        if angle < (math.pi - epsilon) or angle > (math.pi + epsilon):
            return True
    
    return False
