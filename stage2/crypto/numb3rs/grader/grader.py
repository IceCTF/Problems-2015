def grade(arg, key):
    if "flag_alphabetic_indices" in key:
        return True, "Correct!"
    else:
        return False, "Sorry, not this time."
