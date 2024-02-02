# Crear un arxiu de nom vehicle.py. En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
# Constructor
# Atributs (mínim 6)
# Getters/Setters
# Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
# Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

class vehicle:
    def __init__ (self, marca, model, preu, cavalls, color, velocitat):
        self.marca = marca
        self.model = model
        self.preu = preu
        self.cavalls = cavalls
        self.color = color
        self.velocitat = velocitat
    
    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getModel(self):
        return self._model

    def setModel(self, model):
        self._model = model

    def getPreu(self):
        return self._preu

    def setPreu(self, preu):
        self._preu = preu

    def getCavalls(self):
        return self._cavalls

    def setCavalls(self, cavalls):
        self._cavalls = cavalls
        
    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def getVelocitat(self):
        return self._velocitat

    def setVelocitat(self, velocitat):
        self._velocitat = velocitat
        
    def parts(self):
        print("Marca:", self.marca)
        print("Model:", self.model)
        print("Preu:", self.preu)
        print("Cavalls:", self.cavalls)
        print("Color:", self.color)
        print("Velocitat:", self.velocitat)

    def to_dict(self):
        return {
            "marca":self.marca,
            "model":self.model,
            "preu":self.preu,
            "cavalls":self.cavalls,
            "color":self.color,
            "velocitat":self.velocitat
        }

vehicle1 = vehicle("McLaren", "720S", 330000, 720, "Naranja", 341)
vehicle1.parts()