def grade(arg, key):
    if "flag_wait_wasnt_it_dalvik" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
