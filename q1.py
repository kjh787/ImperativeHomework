inventory = {
    "hammer":       {"price": 12.99, "quantity": 25},
    "screwdriver":  {"price": 6.49,  "quantity": 4},
    "wrench":       {"price": 9.75,  "quantity": 10},
    "tape measure": {"price": 8.25,  "quantity": 2},
    "drill":        {"price": 59.99, "quantity": 7},
}


def check_low_stock(threshold):
    print(f"Items with fewer than {threshold} in stock:")
    found_low = False

    for item, details in inventory.items():
        if details["quantity"] < threshold:
            print(f"  {item}: {details['quantity']} left (price ${details['price']:.2f})")
            found_low = True

    if not found_low:
        print("  None. All items are sufficiently stocked.")


check_low_stock(5)
print()
check_low_stock(1)
