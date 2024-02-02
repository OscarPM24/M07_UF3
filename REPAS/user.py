# Crear un arxiu de nom user.py. En aquest arxiu s’ha de crear una class de nom user. Aquesta class ha de tindre:
# Constructor
# Atributs (mínim 6)
# Getters/Setters
# Mètode de nom saltuacio on es mostren, per pantalla, totes les dades (atributs) del user.
# Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

class user:
    def __init__ (self, nom, cognom, email, contrasenya, telefono, dni):
        self.nom = nom
        self.cognom = cognom
        self.email = email
        self.contrasenya = contrasenya
        self.telefono = telefono
        self.dni = dni
    
    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getCognom(self):
        return self.cognom

    def setCognom(self, cognom):
        self.cognom = cognom

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getContrasenya(self):
        return self.contrasenya

    def setContrasenya(self, contrasenya):
        self.contrasenya = contrasenya

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getDni(self):
        return self.dni

    def setDni(self, dni):
        self.dni = dni
        
    def salutacio(self):
        print("Nom:", self.nom)
        print("Cognom:", self.cognom)
        print("Email:", self.email)
        print("Contrasenya:", self.contrasenya)
        print("Telèfon:", self.telefono)
        print("DNI:", self.dni)

    def to_dict(self):
        return {
            "nom": self.nom,
            "cognom": self.cognom,
            "email": self.email,
            "contrasenya": self.contrasenya,
            "telefono": self.telefono,
            "dni": self.dni
        }
        
user1 = user("Oscar", "Perez", "oscar@gmail.com", "mondongo", 123456789, "123456789A")
user1.salutacio()