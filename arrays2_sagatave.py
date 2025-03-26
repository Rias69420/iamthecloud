# Dots masīvs ar dažādām programmēšanas valodām
progr_valodas = ["Python", "C++", "PHP", "C+", "SQL", "Javascript", "Typesscript", "Java"]
valodas=len(progr_valodas)
# Izvadi pirmo masīva elementu
print (progr_valodas[0])

# Izvadi trešo masīva elementu
print (progr_valodas[3])

# Izvadi Pēdējo masīva elementu
print (progr_valodas[4])

# Dzēs pēdējo masīva elementu
progr_valodas.pop(5)

# Pievieno masīva beigās jaunu valodu "Kotlin"
progr_valodas.append("Kotlin")

# Izveido programmu, kas pārbauda, vai masīvā ievietots elements "Typescript". Ja jā: print("Success!"), ja nē: print("Not found")
if "Typesscript" in progr_valodas:
    print("Success!")
else:
    print("Not Found")
# Remove Java
progr_valodas.pop(7)
# Add C# starp C++ un PHP
progr_valodas.insert (2, "C#")
print(progr_valodas)
