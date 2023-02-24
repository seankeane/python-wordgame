import re


def check_only_alpha(check):
    x = re.search(r"^[A-Za-z]*$", check)
    return False if x is None else True