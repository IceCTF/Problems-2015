def grade(arg, key):
    if "now_youre_thinking_with_exif" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
