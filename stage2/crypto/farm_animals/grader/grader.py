def grade(arg, key):
    if "flag_pigs_shouldnt_write" in key:
        return True, "Correct!"
    else:
        return False, "Sorry, not this time."
