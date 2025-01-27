from datetime import datetime

class Enterprise:

    def __init__(self):
        self.vehicles = []
        self.drivers = []

    def assign_vehicle_to_driver(self, chassis_number, driver_email_address):
        driver = self.get_driver_by_email_address(driver_email_address)
        vehicle = self.get_vehicle_by_chassis_number(chassis_number)
        driver.take_vehicle(vehicle)

    def get_vehicle_by_chassis_number(self, chassis_number):
        for vehicle in self.vehicles:
            if vehicle.chassis_number == chassis_number:
                return vehicle

        raise VehicleNotFoundException()

    def get_driver_by_email_address(self, driver_email_address):
        for driver in self.drivers:
            if driver.email_address == driver_email_address:
                return driver

        raise DriverNotFoundException()

    def prepare_delivery(self, delivery, chassis_number, driver_email_address):
        truck_driver = self.get_driver_by_email_address(driver_email_address)
        truck = self.get_vehicle_by_chassis_number(chassis_number)

        if delivery.hazardous_cargos:
            if datetime.now() > truck_driver.license_hazardous_validity_limit:
                raise TruckDriverHazardousLicenseException()

            if not truck.homologue_hazardous:
                raise TruckHazardousMaterialException()

class VehicleNotFoundException(Exception):
    pass

class DriverNotFoundException(Exception):
    pass

class TruckDriverHazardousLicenseException(Exception):
    pass

class TruckHazardousMaterialException(Exception):
    pass
