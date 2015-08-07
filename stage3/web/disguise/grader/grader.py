
def grade(autogen, key):
    if "flag_why_did_we_stop_using_perl_again" in key.lower():
        return True, "Correct!"
    else:
        return False, "Try Again."
