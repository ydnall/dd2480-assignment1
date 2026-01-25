from .geometry import distance_between_points

def lic_0(points: Points, parameters: Parameters) -> bool:
    """
    Returns True if there exists at least one pair of consecutive points
    whose distance is greater than LENGTH1.
    """
    for (p1, p2) in zip(points, points[1:]):
        if distance_between_points(p1, p2) > parameters.LENGTH1:
            return True
    return False
