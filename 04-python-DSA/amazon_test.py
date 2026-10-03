def total_price(s, t):
    size = {
        "small": 1,
        "medium": 2,
        "large": 2
    }
    
    toppings = {
        "cheese": 1,
        "mushroom": 2
    }
    
    cost = size[s] + toppings[t]
    return cost

print(total_price("small", "cheese"))