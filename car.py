

class Car(object):


    #initialise car object
    def __init__(self, name='General', model='GM', carType='saloon'):
        self.name = name
        self.model = model
        self.carType = carType
        self.speed = 0

        if (self.name == 'Koenigsegg') or (self.name == 'Porshe'):
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if (self.carType == 'saloon'):
            self.num_of_wheels = 4
        else:
            self.num_of_wheels = 8

        if (self.carType != 'trailer'):
            self.carType == 'saloon'


    #check if is a saloon car
    def is_saloon(self):
        if (self.carType == 'saloon'):
            return True
        else:
            return False

    def drive(self, weirdStuff):
        if (weirdStuff == 7):
            self.speed = 77
        elif (weirdStuff == 3):
            self.speed = 1000
        
        return self
    