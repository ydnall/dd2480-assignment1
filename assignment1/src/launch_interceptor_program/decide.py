"""
Top-level DECIDE() entrypoint for the Launch Interceptor Program.
"""

from .lic.lic_9 import lic_9


from .model import DecisionInput, DecisionResult


def decide(inputs: DecisionInput) -> DecisionResult:
    """
    Determines if an interceptor will be launched based upon
    input rader tracking information.

    Args:
        inputs: DecisionInput(POINTS, PARAMETERS, LCM, PUV)

    Returns:
        DecisionResult(LAUNCH, CMV, PUM, FUV)
    """
    raise NotImplementedError("DECIDE logic not implemented yet")

