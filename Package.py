# Create class for packages

class Packages:
    def __init__(self, ID, address, city, state, zipcode, Deadline_time, weight, currentstatus, status, departuretime, deliverytime):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.currentstatus = currentstatus
        self.status = status
        self.departure_time = None # Departure time
        self.delivery_time = None # Delivery time

    def __str__(self):
        return "ID:%s, %s, %s, %s, %s, %s, %s, %s, %s, Delivered at: %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.Deadline_time, self.weight, self.status, self.departure_time, self.delivery_time,)

    #def update_status(self, convert_timedelta):
        #if self.delivery_time < convert_timedelta:
            #self.currentstatus = "At Hub"
        #elif self.departure_time > convert_timedelta:
            #self.currentstatus = "En route"
        #else:
            #self.status = "Delivered"
    def update_status(self, timeChange):
        if self.delivery_time == None:
            self.status = "At the hub"
        elif timeChange < self.departure_time:
            self.status = "At the hub"
        elif timeChange < self.delivery_time:
            self.status = "En Route"
        else:
            self.status = "Delivered"