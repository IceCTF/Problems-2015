def grade(arg, key):
    if "Flag_gooselings_cant_drive" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
