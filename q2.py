flight_route = [
    ("New Orleans", "Atlanta"),
    ("Atlanta", "New York"),
    ("New York", "London"),
    ("London", "Paris"),
]


def print_itinerary(route_list):
    print("Flight Itinerary")
    print("-" * 40)

    for leg_number, (departure, arrival) in enumerate(route_list, start=1):
        print(f"Leg {leg_number}: {departure} -> {arrival}")

    print("-" * 40)
    print(f"Total legs: {len(route_list)}")


print_itinerary(flight_route)
