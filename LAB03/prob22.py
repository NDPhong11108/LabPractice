SPECIALS = "!@#$%^&*-_"


def count_types(password):
    upper = lower = digits = specials = 0
    for ch in password:
        if "A" <= ch <= "Z":
            upper += 1
        elif "a" <= ch <= "z":
            lower += 1
        elif "0" <= ch <= "9":
            digits += 1
        elif ch in SPECIALS:
            specials += 1
        else:
            return None  # invalid character
    return upper, lower, digits, specials


def rate_password(password):
    counts = count_types(password)
    if password == "" or counts is None:
        return "Invalid password"
    k = 0
    for c in counts:
        if c > 0:
            k += 1
    if len(password) < 8 or k <= 2:
        rating = "Weak"
    elif k == 3:
        rating = "Medium"
    else:
        rating = "Strong"
    u, l, d, s = counts
    return f"{rating} (U:{u} L:{l} D:{d} S:{s})"


try:
    print(rate_password(input()))
except EOFError:
    print("Invalid password")
