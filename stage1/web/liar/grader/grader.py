
def grade(autogen, key):
    if "hidden_in_the_code" in key.lower():
        return True, "Correct!"
    elif "not_this_time" in key.lower():
        return False, "Not this time!"
    else:
        return False, "Try Again."
