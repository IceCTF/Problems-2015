def grade(arg, key):
    if "Flag_that_movie_sucked" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
