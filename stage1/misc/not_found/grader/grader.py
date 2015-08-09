def grade(arg, key):
    if "flag_there_you_are_you_silly_flag" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
