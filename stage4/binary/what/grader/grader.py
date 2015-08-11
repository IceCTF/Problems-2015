def grade(arg, key):
    if "flag_squeamish_ossifrage" in key:
        return True, "Sweet!"
    else:
        return False, "Nope."
