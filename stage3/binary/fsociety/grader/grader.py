def grade(arg, key):
    if "flag_leave_me_here" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
