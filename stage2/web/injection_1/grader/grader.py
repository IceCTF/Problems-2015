
def grade(autogen, key):
    if "flag_these_kinds_of_injections_arent_scary_right" in key.lower():
        return True, "Correct!"
    else:
        return False, "Try Again."
