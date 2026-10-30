def update_cart(item, action="add", cart=None):
    if cart is None:  # make a new list each call, not a shared default
        cart = []
    if action == "add":
        cart.append(item)
        return cart
    if action == "remove":
        if item in cart:
            cart.remove(item)
        return cart
    return item in cart  # action == "has"


a = input()
b = input()
c = input()
d = input()

cart1 = update_cart(a)
print(cart1)
print(update_cart(b, "has"))  # a different new cart
cart1 = update_cart(c, "add", cart1)
print(cart1)
cart1 = update_cart(d, "remove", cart1)
print(cart1)
