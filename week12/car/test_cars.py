from car import Car, ElectricCar

# Test the Car class
my_car = Car("toyota", "corolla", 2020, 15000)
print(f"Car representation: {my_car}")
print(f"Car descriptive name: {my_car.get_descriptive_name()}")
print(my_car.read_odometer())

# Update the odometer value
print("\nUpdating odometer...")
my_car.update_odometer(15500)
print(my_car.read_odometer())

# Increment the odometer value
print("\nIncrementing odometer...")
my_car.increment_odometer(100)
print(my_car.read_odometer())

# Test rolling back the odometer (should print error message)
print("\nTrying to roll back odometer...")
my_car.update_odometer(15000)

# Test the ElectricCar class
print("\n" + "="*50 + "\n")
my_tesla = ElectricCar("tesla", "model s", 2022)
print(f"Electric car descriptive name: {my_tesla.get_descriptive_name()}")
print(f"Battery information: {my_tesla.describe_battery()}")
print(f"Gas tank information: {my_tesla.describe_gas_tank()}")
print(f"Range information: {my_tesla.get_range()}")

# Upgrade the battery and check new range
print("\nUpgrading battery...")
my_tesla.upgrade_battery(65)
print(f"New battery information: {my_tesla.describe_battery()}")
print(f"New range information: {my_tesla.get_range()}")

# Create another electric car with custom values
print("\nCreating another electric car...")
my_nissan = ElectricCar("nissan", "leaf", 2021, 5000, 60)
print(f"Car descriptive name: {my_nissan.get_descriptive_name()}")
print(f"Battery information: {my_nissan.describe_battery()}")
print(f"Range information: {my_nissan.get_range()}")
print(my_nissan.read_odometer()) 