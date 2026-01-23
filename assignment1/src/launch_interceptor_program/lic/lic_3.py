from ..model import Parameters, Points
from .geometry import triangle_area

def lic_3(points: Points, parameters: Parameters) -> bool:
    for i in range(len(points) - 2):
        area = triangle_area(points[i], points[i + 1], points[i + 2])
        if area > parameters.AREA1:
            return True
    
    return False
