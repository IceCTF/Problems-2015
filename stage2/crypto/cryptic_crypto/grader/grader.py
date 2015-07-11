def grade(arg, key):
    if "flag_substitution_ciphers_are_bad" in key:
        return True, "Correct!"
    else:
        return False, "Sorry, not this time."
