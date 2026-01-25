"""
Conditions Met Vector (CMV) computation.
"""

from .lic import (
    lic_0,
    lic_1,
    lic_2,
    lic_3,
    lic_4,
    lic_5,
    lic_6,
    lic_7,
    lic_8,
    lic_9,
    lic_10,
    lic_11,
    lic_12,
    lic_13,
    lic_14,
)
from .model import Parameters, Points


def compute_cmv(points: Points, parameters: Parameters) -> list[bool]:
    """
    Computes the Conditions Met Vector by evaluating all 15 LICs.

    Args:
        points: List of (x, y) coordinate tuples
        parameters: Parameters object containing values needed for LIC evaluation

    Returns:
        List of 15 boolean values, one for each LIC
    """
    lic_functions = [
        lic_0,
        lic_1,
        lic_2,
        lic_3,
        lic_4,
        lic_5,
        lic_6,
        lic_7,
        lic_8,
        lic_9,
        lic_10,
        lic_11,
        lic_12,
        lic_13,
        lic_14,
    ]

    return [lic(points, parameters) for lic in lic_functions]
