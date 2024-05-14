# Create class for the trucks

class Truck:
    def __init__(self, truckNumber, speed, load, packages, mileage, address, depart_time):
        self.truckNumber = truckNumber
        #self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.truckNumber, self.speed, self.load, self.packages, self.mileage,
                                               self.address, self.depart_time)
