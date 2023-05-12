class Car:
    def __init__(self, wheels, make, model):
        self._wheel = wheels
        self._make = make
        self._model = model
    
    def get_model(self):    # granded access to the model
        return self._model
    
car1 = Car(4, "Opel", "Corsa")
print(car1)
print(car1.get_model())