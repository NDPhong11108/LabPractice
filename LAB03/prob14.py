def check_email(email):
    if " " in email:
        return "Invalid: contains spaces"
    if email.count("@") != 1:
        return "Invalid: must contain exactly one @"
    username, domain = email.split("@")
    if username == "":
        return "Invalid: missing username"
    if "." not in domain:
        return "Invalid: domain needs a dot"
    if domain.startswith(".") or domain.endswith("."):
        return "Invalid: bad domain"
    if domain.lower().endswith((".edu", ".edu.vn")):
        return "Valid (Education)"
    return "Valid"


try:
    print(check_email(input()))
except EOFError:
    print("Error: Invalid input")
