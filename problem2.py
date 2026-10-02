card = input() == "True"
no_overdue = input() != "True"
available = input() == "True"
print("Card is valid:", card)
print("No overdue books:", no_overdue)
print("Book is available:", available)
print("Can borrow:", card and no_overdue and available)
