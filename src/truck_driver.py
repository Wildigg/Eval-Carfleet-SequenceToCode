from src.driver import Driver

class TruckDriver(Driver):

    def __init__(self, email_address, license_hazardous_validity_limit):
        super().__init__(email_address)
        self.license_hazardous_validity_limit = license_hazardous_validity_limit
