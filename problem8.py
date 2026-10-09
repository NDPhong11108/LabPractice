def vnd_to_usd(amount_vnd):
    return amount_vnd / 25000


def vnd_to_eur(amount_vnd):
    return amount_vnd / 27000


amount = float(input())
print(f"{vnd_to_usd(amount):.2f} USD")
print(f"{vnd_to_eur(amount):.2f} EUR")
