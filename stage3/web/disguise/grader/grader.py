
def grade(autogen, key):
    if "flag_xss_all_the_things" in key.lower():
        return True, "Correct!"
    else:
        return False, "Try Again."
