from collections import defaultdict

def check(input_str: str):
    rep = defaultdict(bool)

    for char in input_str:
        rep[char] = not rep[char]

    found_odd = False
    for is_odd in rep.values():
        if is_odd:
            if found_odd:
                return False

            found_odd = True

    return True