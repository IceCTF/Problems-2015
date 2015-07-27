
def grade(autogen, key):
    if "flag_why_would_this_even_be_a_feature" in key.lower():
        return True, "Correct!"
    else:
        return False, "Try Again."
