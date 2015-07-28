def grade(arg, key):
    if "flag_damn_that_movie_was_bad" in key.lower():
        return True, "Correct!"
    else:
        return False, "Nope."
