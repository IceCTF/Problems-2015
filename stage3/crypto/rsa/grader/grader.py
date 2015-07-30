def grade(arg, key):
    if "flag_dont_you_just_love_rsa" in key:
        return True, "Oh yes i do!"
    else:
        return False, "Sorry, not this time."
