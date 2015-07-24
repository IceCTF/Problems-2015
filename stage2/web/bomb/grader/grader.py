
def grade(autogen, key):
    if "flag_the_building_is_safe" in key.lower():
        return True, "Correct!"
    else:
        return False, "Try Again."
