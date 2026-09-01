shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()

    for order in orders:
        if not determine(menus, order):
            return False
    return True

def determine(menus, order):
    primary_index = 0
    last_index = len(menus) - 1
    standard = (primary_index + last_index) // 2

    while primary_index <= last_index:
        if menus[standard] == order:
            return True
        elif menus[standard] > order:
            last_index = standard - 1
        else:
            primary_index = standard + 1

        standard = (primary_index + last_index) // 2

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)