def grade(arg, key):
    if "NOW_YOURE_THINKING_WITH_EXIF" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
