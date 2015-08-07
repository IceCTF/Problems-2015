def grade(arg, key):
    if "flag_moo_moo_the_cow_says" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
