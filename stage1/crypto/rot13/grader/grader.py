def grade(arg, key):
    if "rot_13_isnt_secure" in key:
        return True, "Yes, exactly! Now tell that to Jeff."
    else:
        return False, "No dice."
