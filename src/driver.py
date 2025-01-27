from src.person import Person

class Driver(Person):

    def __init__(self, email_address):
        super().__init__(email_address)
        self.vehicle = None

    def take_vehicle(self, vehicle):
        if not (self.vehicle is None):
            raise DriverNotAvailableException()

        self.vehicle = vehicle

class DriverNotAvailableException(Exception):
    pass
