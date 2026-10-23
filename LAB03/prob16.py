TYPES = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")


def check_transfusion(donor, recipient):
    donor = donor.strip().upper()
    recipient = recipient.strip().upper()
    if donor not in TYPES or recipient not in TYPES:
        return "Error: Invalid blood type"
    abo_ok = donor[:-1] == "O" or donor[:-1] == recipient[:-1] or recipient[:-1] == "AB"
    rh_ok = donor[-1] == "-" or recipient[-1] == "+"
    if abo_ok and rh_ok:
        return "Compatible (Universal Donor)" if donor == "O-" else "Compatible"
    if not abo_ok and not rh_ok:
        return "Incompatible: ABO and Rh"
    return "Incompatible: ABO" if not abo_ok else "Incompatible: Rh"


try:
    print(check_transfusion(input(), input()))
except EOFError:
    print("Error: Invalid blood type")
