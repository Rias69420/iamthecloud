class skolens:
    def __init__(self, vards, uzvards, atzime):
        self.vards = vards
        self.uzvards = uzvards
        self.atzime = atzime
    def display_info(self):
        self.__init__ = print()

    def sekmigs(self):
        if self.atzime >= 4:
            print("Skolens ir sekmigs")

Skolens1 = skolens("Ralfs", "Stabins", 8.9)
Skolens2 = skolens("Aksels", "Mezis", 7.8)
Skolens3 = skolens("Patriks", "Princis", 7.3)

darbiba= input("Izvelies darbibu: display_info, sekmigs:")

x = int(input("izvelies skolenu 1,2 vai 3:"))
if darbiba == "1":
    print(Skolens1)
elif darbiba == "2":
    print(Skolens2)
elif darbiba == "3":
    print(Skolens3)