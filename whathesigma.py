class car:
    def __init__(self, motora_tilpums, gads, virsb_tips, zirgspeki, turbinu,):
            self.motora_tilpums = motora_tilpums
            self.gads = gads
            self.virsb_tips = virsb_tips
            self.zirgspeki = zirgspeki
            self.turbinu = turbinu

    def cipot(self):
            self.zirgspeki += 50

    def pieklikt_turbinu(self):
            self.turbinu -= 30
bembis = car(2.0, 2000, "Universālis", 60, 101)

print(bembis.zirgspeki)
bembis.cipot()
print(bembis.zirgspeki)

bembis.pieklikt_turbinu()
print(bembis.zirgspeki)

