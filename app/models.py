class Driver:
    '''
    Driver class to define Driver Objects
    '''

    def __init__(self,id,name,phone_number,image,car_plate,car_brand,car_colour):
        self.id =id
        self.name = name
        self.phone_number = phone_number
        self.image = image
        self.car_plate = car_plate
        self.car_brand = car_brand
        self.car_colour = car_colour


class Customer:
    '''
    Customer class to define Customer objects
    '''

    def __init__(self,id,pickup_location,dropoff_location):
        self.id= id
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location

class ReqStatus:
    '''
    Class to show request of a ride status from start to completion
    '''
    WAITING = "WAITING"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"

    def __init__(self,id,customer_id,driver_id,picked_up,completed_at):
        self.id = id
        self.customer_id = customer_id
        self.driver_id = driver_id
        self.picked_up = picked_up
        self.completed_at = completed_at
