import random

class Hrac():

    def __init__ (self, penize):
        self.penize = penize
        self.jmeno = jmeno
        self.kostka= kostka

    def hodKostkou(self):
        hod = random.randint(1, self.kostka.pocetSten)
        return hod

class Kostka():
    def __init__(self, pocetSten):
        self.pocetSten = pocetSten

def hra():
    kostka = Kostka(6)
    hrac = Hrac(10000,kostka)
    pocitac = Hrac(0,kostka)
    while hrac.penize > 0:
        
        sazka = int(input("Kolik vsadis?"))
        while sazka > hrac.penize:
            print(f"Tolik nemas, mas jen {hrac.penize}")
            sazka = int(input("Kolik vsadis?"))
        hh = hrac.hod()
        ph = pocitac.hod()
        print("Tys hodil {hh}, pocitac hodil {ph}")
        if hh > ph:
            print ("Vyhral jsi")
            hrac.penize += sazka
        elif ph > hh:
            print ("Prohral jsi")
            hrac.penize -=sazka
        elif hh == ph:
            print ("Remiza")
        print(f"Mas {hrac.penize}")
            

if __name__ == "__main__":
    hra()
