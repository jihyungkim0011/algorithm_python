shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    result_list = []
    prices.sort(reverse=1)
    coupons.sort(reverse=1)
    len_prices = len(prices)
    len_coupons = len(coupons)

    if len_prices > len_coupons:
        for _ in range(0, len_prices - len_coupons):
            coupons.append(0)

    for i in range(len_prices):
        discounted = prices[i] * (100 - coupons[i]) / 100
        result_list.append(discounted)


    return int(sum(result_list))


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))