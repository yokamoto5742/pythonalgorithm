def print_price(price, func):
    print(f'値段は{func(price)}です')


def price_with_tax(price):
    return f"{int(price * 1.1)}円(税込)"


def price_without_tax(price):
    return f"{price}円(税抜)"


print_price(price=100, func=price_without_tax)
print_price(price=100, func=price_with_tax)
