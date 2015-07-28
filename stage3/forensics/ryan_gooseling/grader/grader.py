def grade(arg, key):
    if "flag_gooselings_cant_drive" in key.lower():
        return True, "Correct!"
    else:
        return False, "Nope."
