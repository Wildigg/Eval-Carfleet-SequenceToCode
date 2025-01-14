from vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, chassis_number, homologue_hazardous):
        super().__init__(chassis_number)
        self.homologue_hazardous = homologue_hazardous

