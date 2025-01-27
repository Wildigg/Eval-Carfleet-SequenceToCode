from datetime import datetime

from src.entreprise import Enterprise
from src.driver import Driver
from src.vehicle import Vehicle
from src.truck import Truck
from src.truck_driver import TruckDriver
from src.person import Person
from src.delivery import Delivery

def person_check():
    person1 = Person("person1@mail.com")

    print(person1.email_address)

def delivery_check():
    delivery = Delivery(True)

    print(delivery.hazardous_cargos)

def vehicle_check():
    vehicle1 = Vehicle('cn_1')

    print(vehicle1.chassis_number)

def truck_check():
    truck = Truck('cn_t_1', False)

    print(truck.chassis_number)
    print(truck.homologue_hazardous)

def driver_check():
    driver1 = Driver('driver1@mail.com')

    print(driver1.email_address)

    vehicle1 = Vehicle('cn_1')
    vehicle2 = Vehicle('cn_2')

    driver1.take_vehicle(vehicle1)
    # Error test
    # driver1.take_vehicle(vehicle2)

def truck_driver_check():
    t_driver1 = TruckDriver('driver_t_1@mail.com', datetime(2020, 5, 17))

    print(t_driver1.email_address)
    print(t_driver1.license_hazardous_validity_limit)

    t_vehicle1 = Truck('cn_t_1', False)
    vehicle2 = Vehicle('cn_1')

    t_driver1.take_vehicle(t_vehicle1)
    # Error test
    # t_driver1.take_vehicle(vehicle2)

def enterprise_check():
    driver1 = Driver('driver1@mail.com')
    t_driver1 = TruckDriver('driver_t_1@mail.com', datetime(9999, 12, 31))
    t_driver2 = TruckDriver('driver_t_2@mail.com', datetime(1111, 1, 1))

    vehicle1 = Vehicle('cn_1')
    t_vehicle1 = Truck('cn_t_1', True)
    t_vehicle2 = Truck('cn_t_2', False)

    enterprise = Enterprise()

    enterprise.drivers.extend([driver1, t_driver1, t_driver2])
    enterprise.vehicles.extend([vehicle1, t_vehicle1, t_vehicle2])

    print(enterprise.get_driver_by_email_address('driver_t_1@mail.com').email_address)
    print(enterprise.get_vehicle_by_chassis_number('cn_1').chassis_number)

    # Error Test
    # enterprise.get_driver_by_email_address('matchless').chassis_number
    # enterprise.get_vehicle_by_chassis_number('matchless').chassis_number

    delivery1 = Delivery(False)
    delivery2 = Delivery(True)

    enterprise.prepare_delivery(delivery1, 'cn_1', 'driver1@mail.com')

    # Error Test
    # enterprise.prepare_delivery(delivery2, 'cn_t_2', 'driver_t_2@mail.com')
    # enterprise.prepare_delivery(delivery2, 'cn_t_2', 'driver_t_1@mail.com')

    enterprise.prepare_delivery(delivery2, 'cn_t_1', 'driver_t_1@mail.com')

if __name__ == "__main__":
    person_check()
    delivery_check()
    vehicle_check()
    truck_check()
    driver_check()
    truck_driver_check()
    enterprise_check()

