# Aksels Mežis, 10.M

# 1. Izveido un izsauc funkciju "m-uz-km", kas kā parametru saņem metrus un pārveido tos kilometros!
def m_uz_km(x): # 1m = 0,001 kilometers
    return x * 0.001



# 2. Izveido šai funkcijai pretēju funkciju km_uz_m, taču šoreiz 
#    funkcija pati pieprasa lietotājam ievadīt vērtību! Pēc tam ar 
#    TRY-EXCEPT palīdzību pārbaudi, vai mainīgais, kas satur 
#    kilometrus patiešām ir skaitlis!
def km_uz_m(km):
        try:
            return km * 1000
        except ValueError:
            print("ievadita vertiba nav skaitlis!!!!")        
while True:
    huh = input("Izvelies m_uz_km, km_uz_m vai done:")
    if huh == "done":
        break
    x = int(input("M:"))
    if huh == "m_uz_km":
        print(x, "*", 0.001, "=", m_uz_km(x))
    if huh == "km_uz_m":
        y = int(input("KM:"))
        print(y, "*", 1000, "=", km_uz_m(y))


        
# 3. Izveido funkciju count_negative, kas saskaita negatīvo skaitļu skaitu masīvā!
masivs = [114, 23.15, 0, -6, 93, -37, -1050.03, 72, -1, -273.15, 2048, -885, 1000, -0.001]
def count_negative(masivs):
        for value in masivs:
           if value < 0:
            print(value)