VISIBLE_DIGITS = 4


def mask_card(card):
    cleaned = card.replace(" ", "").replace("-", "")
    hidden_count = len(cleaned) - VISIBLE_DIGITS
    masked = "*" * hidden_count + cleaned[hidden_count:]
    return masked
