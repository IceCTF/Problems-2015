def grade(arg, key):
    if "flag_some_barcode_and_hidden_audio" in key:
        return True, "Correct!"
    else:
        return False, "Nope."
