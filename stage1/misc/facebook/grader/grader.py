def grade(arg, key):
    if "flag_why_hide_stuff_on_facebook" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
