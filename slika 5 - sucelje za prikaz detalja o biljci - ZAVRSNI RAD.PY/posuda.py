import numpy as np

class PyFloraPosuda:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = ""
        self.sensor_temp = 0.0
        self.sensor_vlaga = 0.0
        self.sensor_ph = 0.0
        self.sensor_lux = 0.0
        self.biljka = None
        self.list_senzori = [0.0, 0.0, 0.0, 0.0]
        self.limit = 10

    def __iter__(self):
        self.x = self.id
        return self
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
 
        # Store current value ofx
        x = self.x
 
        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
 
        # Else increment and return old value
        self.x = x + 1
        return x
    
    def dodaj_biljku(self, b):
        self.biljka = b

    def osvjezi_senzore(self):
        self.sensor_temp = np.random.randn(-10, 40)
        self.sensor_vlaga = np.random.randn(0, 100)
        self.sensor_ph = np.random.randint(1, 14)
        self.sensor_lux = np.random.randint(200, 1200)

    def promijeni_status(self, status):
        self.status = status

    def vrati_status(self):
        return self.status

    def vrati_listu_senzora(self):
        self.list_senzori = [self.sensor_temp, self.sensor_vlaga, self.sensor_ph, self.sensor_lux]
        return self.list_senzori
