def duty_free(price, discount, holiday_cost):
    price = price * discount / 100
    result = holiday_cost // price
    return result