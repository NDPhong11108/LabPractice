def loan_decision(income, score, debt, employed):
    if not 0 < income < float("inf") or not 0 <= debt < float("inf"):
        return "Error: Invalid input"
    if not 300 <= score <= 850 or employed not in ("True", "False"):
        return "Error: Invalid input"
    ratio = debt / income
    if score < 500:
        return "Rejected: Low Credit Score"
    if ratio > 0.5:
        return "Rejected: High Debt"
    if employed == "False":
        return "Approved with Guarantor" if score >= 750 else "Rejected: Unemployed"
    if score >= 700 and ratio <= 0.3:
        return "Approved: Premium Rate"
    return "Approved: Standard Rate"


try:
    income = float(input())
    score = int(input())
    debt = float(input())
    print(loan_decision(income, score, debt, input()))
except Exception:
    print("Error: Invalid input")
