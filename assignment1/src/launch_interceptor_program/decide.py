"""
Top-level DECIDE() entrypoint for the Launch Interceptor Program.
"""

from .cmv import compute_cmv
from .pum import compute_pum
from .fuv import compute_fuv
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
    # PUM (Preliminary Unlocking Matrix)
    pum = compute_pum(cmv, inputs.LCM)
    # FUV (Final Unlocking Vector)
    fuv = compute_fuv(pum, inputs.PUV)
    
    launch = "YES" if all(fuv) else "NO"

    result = DecisionResult(launch, cmv, pum, fuv)

    return result
