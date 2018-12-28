#Vers 1
def excluding_vat_price(price):
    if price:
        result = round(price / ((100 + 15) / 100),2)
        return result
    else:
        return -1


#Vers 2 works-on-my-machine
def excluding_vat_price(price):
    result = round(price / ((100 + 15) / 100), 2)
    return result if price else -1
