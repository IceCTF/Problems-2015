def grade(arg, key):
    if "flag_always_pad_your_rsa_messages" in key:
        return True, "Great!"
    else:
        return False, "Sorry, not this time."
