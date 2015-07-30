
def grade(autogen, key):
    if "flag_i_swear_it_was_9_inches" in key.lower():
        return True, "Correct! Woo!"
    else:
        return False, "Try Again."
