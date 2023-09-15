class Vehicle:
    color = 'White'
    def __init__(self, name, max_speed, mileage, capacity):
        self.capacity = capacity
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self, capacity):
        self.capacity = capacity
        print(f"The seating capacity of a {self.name} is {capacity} passengers")
    def show(self):
        print(f"Name: {self.name}\nMax speed: {self.max_speed}\nMileage: {self.mileage}\nColor: {self.color}")
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        print(f"The seating capacity of a {self.name} is {capacity} passengers")
    def fare(self):
        return super().fare() * 1.1

run_down_bus = Bus('Mercedes', 80, 69500, 50)
run_down_car = Vehicle('BMW', 120, 10520, 5)
run_down_car.show()
run_down_bus.show()
run_down_bus.seating_capacity()
print(f'Fare is: {run_down_bus.fare()}')
print(type(run_down_bus), type(run_down_car))
print(f'Is {run_down_bus.name} an instance of Vehicle? {isinstance(run_down_bus, Vehicle)}')