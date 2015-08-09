def grade(arg, key):
    if "flag_keep_your_files_close_and_your_tempfiles_closer" in key:
        return True, "Nice!"
    else:
        return False, "Nope."
