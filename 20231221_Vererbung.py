class Person:
    def __init__(self, name, istmaennlich):
        self.name = name
        self.istmaennlich = istmaennlich

class Mitarbeiter(Person):
    def __init__(self, name, istmaennlich):
        super().__init__(name, istmaennlich)

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, istmaennlich):
        super().__init__(name, istmaennlich)

class Abteilung:
    def __init__(self, name):
        self.name = name
        self.abteilungsleiter = None
        self.mitarbeiter = []
    def abteilungsleitersetzen(self, abteilungsleiter):
        self.abteilungsleiter = abteilungsleiter
    def mitarbeiterhinzufuegen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
    def allemitarbeiter(self):
        return len(self.mitarbeiter)

class Firma:
    def __init__(self):
        self.abteilungen = []
    def abteilunghinzufuegen(self,abteilung):
        self.abteilungen.append(abteilung)
    def allemitarbeiter(self):
        mitarbeiter = 0
        for i in self.abteilungen:
            mitarbeiter = mitarbeiter + i.allemitarbeiter()
        return mitarbeiter
    def alleabteilungsleiter(self):
        abteilungsleiter = 0
        for i in self.abteilungen:
            if i.abteilungsleiter != None:
                abteilungsleiter = abteilungsleiter + 1
        return abteilungsleiter
    def alleabteilungen(self):
        return len(self.abteilungen)
    def groesteabteilung(self):
        mitarbeiter = 0
        abteilung = None
        for i in self.abteilungen:
            if i.allemitarbeiter() > mitarbeiter:
                abteilung = i
        return abteilung.name
    def maennlichweiblich(self):
        maennlich = 0
        weiblich = 0
        for i in self.abteilungen:
            for y in i.mitarbeiter:
                if y.istmaennlich:
                    maennlich = maennlich + 1
                else:
                    weiblich = weiblich + 1
        if maennlich > weiblich:
            return "Mehr Männer"
        elif weiblich > maennlich:
            return "Mehr Frauen"
        else:
            return "Beide Gleich"
  
def firmainstanzieren():
    firma = Firma()
    
    abteilung1 = Abteilung('ab1')
    abteilung2 = Abteilung('ab2')
    abteilung3 = Abteilung('ab3')

    mitarbeiter1 = Mitarbeiter('ma1', True)
    mitarbeiter2 = Mitarbeiter('ma2', True)
    mitarbeiter3 = Mitarbeiter('ma3', True)
    mitarbeiter4 = Mitarbeiter('ma4', True)
    mitarbeiter5 = Mitarbeiter('ma5', False)
    mitarbeiter6 = Mitarbeiter('ma6', False)

    abteilungsleiter1 = Abteilungsleiter('ma7', True)
    abteilungsleiter2 = Abteilungsleiter('ma8', False)
    abteilungsleiter3 = Abteilungsleiter('ma9', False)

    abteilung1.mitarbeiterhinzufuegen(mitarbeiter1)
    abteilung2.mitarbeiterhinzufuegen(mitarbeiter2)
    abteilung2.mitarbeiterhinzufuegen(mitarbeiter3)
    abteilung3.mitarbeiterhinzufuegen(mitarbeiter4)
    abteilung3.mitarbeiterhinzufuegen(mitarbeiter5)
    abteilung3.mitarbeiterhinzufuegen(mitarbeiter6)
    
    abteilung1.abteilungsleitersetzen(abteilungsleiter1)
    abteilung2.abteilungsleitersetzen(abteilungsleiter2)
    abteilung3.abteilungsleitersetzen(abteilungsleiter3)

    firma.abteilunghinzufuegen(abteilung1)
    firma.abteilunghinzufuegen(abteilung2)
    firma.abteilunghinzufuegen(abteilung3)
    
    return firma

if __name__ == "__main__":
    firma = firmainstanzieren()
    
    print(str(firma.allemitarbeiter()))
    print(str(firma.alleabteilungsleiter()))
    print(str(firma.alleabteilungen()))
    print(str(firma.groesteabteilung()))
    print(str(firma.maennlichweiblich()))
    