def grade(arg, key):
    if "this_would_be_the_flag_you_are_looking_for" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
