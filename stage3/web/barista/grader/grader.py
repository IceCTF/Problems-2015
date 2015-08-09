
def grade(autogen, key):
    if "flag_i_dont_even_like_coffee_but_i_love_coffeescript" in key.lower():
        return True, "Correct!"
    else:
        return False, "Try Again."
