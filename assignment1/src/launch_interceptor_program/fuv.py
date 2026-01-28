from .pum import compute_pum


def compute_fuv(pum: list[list[bool]], puv: list[bool]) -> list[bool]:
    """
    Computes the 15-element FUV based on PUM and PUV.
    """
    fuv = [False for _ in range(15)]

    for i in range(15):
        # if PUV is false, lic should not hold back launch.
        if not puv[i]:
            fuv[i] = True
        else:  # if puv is true, all elements in pum is true rule 2:
            # check pum[i][j] for all j and j=!1
            is_row_all_true = True
            for j in range(15):
                if i != j and not pum[i][j]:
                    is_row_all_true = False
                    break

            fuv[i] = is_row_all_true

    return fuv
