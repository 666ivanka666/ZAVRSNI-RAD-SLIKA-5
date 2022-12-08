import numpy as np
import posuda as Posuda
from PIL import ImageTk, Image
import random

def random_vrijednosti(self):
        var = []
        for x in range(4):
            if x == 0:
                var.append(np.random.randn(21, 30))
            if x == 1:
                var.append(np.random.randn(50, 100))
            if x == 2:
                var.append(np.random.randn(5, 8))
            if x == 3:
                var.append(np.random.randn(500, 1200))
        return var

class Biljka:
    def __init__(self, id, name, posuda, image_path):
        self.id = id
        self.name = name
        self.posuda = posuda
        self.min_vrijednosti_senzora = random_vrijednosti(self)
        self.karakteristike = []
        self.image = ImageTk.PhotoImage(Image.open(image_path))

    def dodaj_karakteristiku(self, karak):
        self.karakteristike.append(random.choice(karak))
    