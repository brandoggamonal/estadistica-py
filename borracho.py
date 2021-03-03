import random


class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return (
            random.choice([
                (random.random(), random.random() * -1),
                (random.random() * -1, random.random()),
                (random.random() * -1, random.random() * -1),
                (random.random(), random.random()),
            ])
        ) #selecciona al azar los pasos que dara el borracho (x, y)


