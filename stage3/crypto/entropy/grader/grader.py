def grade(arg, key):
    if "flag_keep_the_prime_count_high" in key:
        return True, "I'll remember to do that next time"
    else:
        return False, "Sorry, not this time."
