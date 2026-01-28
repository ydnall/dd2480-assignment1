import pytest
from launch_interceptor_program.decide import decide
from launch_interceptor_program.model import (
    Connector,
    DecisionInput,
    DecisionResult,
    Parameters,
)


def dummy_parameters() -> Parameters:
    """Minimal valid PARAMETERS object (values irrelevant for decide())."""
    return Parameters(
        LENGTH1=0.0,
        RADIUS1=0.0,
        EPSILON=0.0,
        AREA1=0.0,
        Q_PTS=2,
        QUADS=1,
        DIST=0.0,
        N_PTS=3,
        K_PTS=1,
        A_PTS=1,
        B_PTS=1,
        C_PTS=1,
        D_PTS=1,
        E_PTS=1,
        F_PTS=1,
        G_PTS=1,
        LENGTH2=0.0,
        RADIUS2=0.0,
        AREA2=0.0,
    )


def full_notused_lcm() -> list[list[Connector]]:
    """15x15 LCM filled with NOTUSED."""
    return [[Connector.NOTUSED for _ in range(15)] for _ in range(15)]


def test_decide():
    """
    Checks if the decide function return the correct result for LAUNCH.
    """

    inputs = DecisionInput(
        POINTS=[(0, 0), (1, 0), (2, 0), (3, 0)],
        PARAMETERS=dummy_parameters(),
        LCM=full_notused_lcm(),
        PUV=[True] * 15,
    )

    result = decide(inputs)

    assert result.LAUNCH == "YES"
