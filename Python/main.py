from car import Car
from pprint import pprint
if __name__ == "__main__":
    print("Hola mundo")
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    pprint(vars(car))
    
    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Andrea Herrera"
    pprint(vars(car2))