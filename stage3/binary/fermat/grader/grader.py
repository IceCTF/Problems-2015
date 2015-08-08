def grade(arg, key):
    if "flag_fermats_last_exploit" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
