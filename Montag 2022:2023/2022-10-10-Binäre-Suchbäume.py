class Knoten:
    def __init__(self, wert: int, links: "Knoten" = None, rechts: "Knoten" = None):
        self.wert = wert
        self.anzahl = 1
        self.links = links
        self.rechts = rechts

    def größe(self) -> int:
        größe_linker_teilbaum = self.links.größe() if self.links else 0
        größe_rechter_teilbaum = self.rechts.größe() if self.rechts else 0
        return größe_linker_teilbaum + 1 + größe_rechter_teilbaum

    def grafisch(self, f) -> None:
        if self.links:
            f.write(str(self.wert) + " -> " + str(self.links.wert) + "\n")
        if self.rechts:
            f.write(str(self.wert) + " -> " + str(self.rechts.wert) + "\n")
        if self.links:
            self.links.grafisch(f)
        if self.rechts:
            self.rechts.grafisch(f)

    def höhe(self) -> int:
        #höhe_links = ???
        #höhe_rechts = ???
        #return ???
        pass
    # TODO Die Spezialfälle, wo das hier noch nicht funktioniert, einbauen

    def abwickeln(self) -> list:
        liste = []
        if self.links:
            liste += self.links.abwickeln()
        liste.append(self.wert)
        if self.rechts:
            liste += self.rechts.abwickeln()
        return liste

class Baum:
    def __init__(self) -> None:
        self.wurzel = None

    def hinzufügen(self, wert: int) -> None:
        if not self.wurzel:
            self.wurzel = Knoten(wert)
        else:
            current = self.wurzel
            while True:
                if wert < current.wert:
                    if current.links:
                        current = current.links
                    else:
                        current.links = Knoten(wert)
                        return
                elif wert == current.wert:
                    current.anzahl += 1
                    return
                else:
                    if current.rechts:
                        current = current.rechts
                    else:
                        current.rechts = Knoten(wert)
                        return

    # Gibt True zurück, falls wert im Baum enthalten ist, ansonsten False
    def enthalten(self, wert: int) -> bool:
        current = self.wurzel
        if not current:
            return False
        while True:
            if wert == current.wert:
                return True
            if wert < current.wert:
                if not current.links:
                    return False
                else:
                    current = current.links
            elif wert > current.wert:
                if not current.rechts:
                    return False
                else:
                    current = current.rechts

    # Gibt zurück, wie oft wert im Baum enthalten ist
    def anzahl(self, wert: int) -> int:
        pass

    # Gibt zurück, wie viele Knoten im Baum enthalten sind
    def größe(self) -> int:
        return self.wurzel.größe() if self.wurzel else 0

    # Gibt die Höhe des Baumes zurück, d.h. die Anzahl der Kanten in einem längsten Pfad von der Wurzel zu einem Blatt
    def höhe(self) -> int:
        if not self.wurzel:
            return -1
        return self.wurzel.höhe()

    # Gibt eine (sortierte) Liste aller Werte im Baum zurück
    def abwickeln(self) -> list:
        if not self.wurzel:
            return []
        else:
            return self.wurzel.abwickeln()

    # Erstellt eine dot-Version des Baumes
    def grafisch(self) -> None:
        with open("baum.dot", "w") as f:
            f.write("digraph {\n")
            if self.wurzel:
                self.wurzel.grafisch(f)
            f.write("}")

    # Löscht ein Vorkommis von wert aus dem Baum
    # Wenn der Wert nur einmal vorkommt, soll der ganze Knoten gelöscht werden
    def löschen(self, wert: int) -> bool:
        liste = self.abwickeln
        liste.remove(wert)
        self.wurzel = None
        self.hinzufügen(wert)
        # Achtung Sehr ineffizient

    # Fügt wert in den Baum ein
    # Falls dieser dadurch unbalanciert wird, wird dies behoben (rebalanciert)
    # Ein Baum ist unbalanciert genau dann, wenn es einen Knoten in ihm gibt, dessen linker und rechter Teilbaum einen Höhenunterschied von mehr als 1 haben
    def hinzufügen_balanciert(self, wert: int) -> None:
        pass

k1 = Knoten(5)
k1.größe()

baum1 = Baum()
baum1.hinzufügen(50)
print(baum1.wurzel.wert)
print(baum1.wurzel.links)
print(baum1.wurzel.rechts)
baum1.hinzufügen(75)
print(baum1.wurzel.rechts.wert)
baum1.hinzufügen(25)
baum1.hinzufügen(100)
baum1.grafisch()