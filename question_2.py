class Car:
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit

    def __repr__(self):
        return f'Car with the maximum speed of {self.max_speed} {self.speed_unit}'

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __repr__(self):
        return f'Boat with the maximum speed of {self.max_speed} knots'
