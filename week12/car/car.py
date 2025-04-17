class Car:
    def __init__(self, make, model, year, odometer_reading):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def __repr__(self):
        return f'{self.make.upper()} {self.model.upper()} {self.year} {self.odometer_reading}'
    
    
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("NO!!")
    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("NO!")


class ElectricCar(Car):
    def __init__(self, make, model, year, odometer_reading=0, battery_size=40):
        super().__init__(make, model, year, odometer_reading)
        self.battery_size = battery_size
    
    def describe_battery(self):
        return f"This car has {self.battery_size} battery."
    
    def describe_gas_tank(self):
        return "This car doesn't need a gas tank!"
    
    def upgrade_battery(self, new_size):
        if new_size > self.battery_size:
            self.battery_size = new_size
            print(f"Battery upgraded to {self.battery_size}.")
        else:
            print("NO!")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        return f"This car can go about {range} miles on a full charge."