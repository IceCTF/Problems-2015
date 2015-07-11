def grade(arg, key):
    if "flag_reverse_engineer_icectf" in key:
        return True, "Correct you are."
    else:
        return False, "Nope."
