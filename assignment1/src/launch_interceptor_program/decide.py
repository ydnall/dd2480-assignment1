"""
Top-level DECIDE() entrypoint for the Launch Interceptor Program.
"""

from .cmv import compute_cmv
from .model import Connector, DecisionInput, DecisionResult


def decide(inputs: DecisionInput) -> DecisionResult:
    """
    Determines if an interceptor will be launched based upon
    input rader tracking information.

    Args:
        inputs: DecisionInput(POINTS, PARAMETERS, LCM, PUV)

    Returns:
        DecisionResult(LAUNCH, CMV, PUM, FUV)
    """
    # CMV (Conditions Met Vector)
    cmv = compute_cmv(inputs.POINTS, inputs.PARAMETERS)

    pass
