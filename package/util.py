def giftsToMoney(diamonds):
    cent_value = diamonds//2
    cents = (cent_value%100)
    if cents <10:
        cents = f"0{cents}"
    dollars = cent_value//100
    return f"${dollars}.{cents}"

def maxPercent(divisor, dividend):
        if(divisor>dividend):
            return 100
        return int(100*divisor/dividend)