def grade(arg, key):
    if "flag_hello_people_who_look_at_the_back_of_the_sign" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
