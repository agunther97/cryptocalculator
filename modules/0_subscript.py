SUBSCRIPT = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
def subscript(strv):
    if type(strv)!=str:
        strv=str(strv)
    return strv.translate(SUBSCRIPT)