# Function to calculate hotel cost
def hotel_cost(num_nights):
    price_per_night = 100  # Example: $100 per night
    return num_nights * price_per_night

# Function to calculate flight cost
def plane_cost(city_flight):
    if city_flight.lower() == "new york":
        return 500  # Example: $500 for a flight to New York
    elif city_flight.lower() == "paris":
        return 600  # Example: $600 for a flight to Paris
    elif city_flight.lower() == "tokyo":
        return 800  # Example: $800 for a flight to Tokyo
    else:
        return 0  # Default cost if the city is not listed

# Function to calculate car rental cost
def car_rental(rental_days):
    price_per_day = 50  # Example: $50 per day
    return rental_days * price_per_day

# Function to calculate total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel = hotel_cost(num_nights)
    total_flight = plane_cost(city_flight)
    total_car = car_rental(rental_days)
    total = total_hotel + total_flight + total_car
    return total

# Main program
def main():
    # Get user inputs
    city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")
    num_nights = int(input("Enter the number of nights you will be staying: "))
    rental_days = int(input("Enter the number of days you will be renting a car: "))

    # Calculate total cost
    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    # Print details
    print("\n----- Holiday Cost Breakdown -----")
    print(f"Destination: {city_flight}")
    print(f"Hotel cost for {num_nights} nights: ${hotel_cost(num_nights)}")
    print(f"Flight cost to {city_flight}: ${plane_cost(city_flight)}")
    print(f"Car rental cost for {rental_days} days: ${car_rental(rental_days)}")
    print(f"Total holiday cost: ${total_cost}")

# Run the program
if __name__ == "__main__":
    main()
