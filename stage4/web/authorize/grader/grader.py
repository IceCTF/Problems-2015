
def grade(autogen, key):
    if "flag_binary_search_those_credentials" in key.lower():
        return True, "Correct!"
    else:
        return False, "Try Again."
