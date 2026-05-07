def calculate_shipping(weight, distance):
    rate = 0.5
    return weight * distance * rate

print(calculate_shipping(10, 20))
