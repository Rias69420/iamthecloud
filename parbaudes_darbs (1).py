# Aksels Mezis, 06.12.2024

# Jums ir dots masīvs "detalas" ar dažādām datoru komponentēm:
detalas = ["CPU", "GPU", "Cietais disks", "RAM", "Mātes plate"]
# Izpildi zemāk dotos uzdevumus, pēc katra uzdevuma izpildes izvadot visu masīvu ar funkciju print()!

# Izvadi pirmo masīva elementu! (1 p.)
print (detalas[0])

# Izvadi pēdējo masīva elementu vismaz divos veidos! (2 p.)
print (detalas[4])
print (detalas[-1])
# Dzēs otro masīva elementu! (1,5 p.)
detalas.pop(1)

# Izvadi masīva elementu skaitu! (1 p.)
x = len(detalas)
print(x)

# Pievieno masīvam jaunu elementu pēc savas izvēles! Ievieto elementu starp elementiem "RAM" un "Mātes plate"! (2,5 p.)
detalas.insert(3, "Assembly")
print(detalas)
# Vēlreiz izvadi masīva elementu skaitu, bet šoreiz izdari to ar cikla palīdzību! (3 p.)
for i in detalas:
    if (i=="CPU"):
        print(len(detalas))

## Hello World!("print") ##

# Tagad jums ir dots masīvs ar atzīmēm
atzimes = [8, 6, 9, 10, 5, 8, 8, 7, 9]

# Izveido algoritmu, kas aprēķina masīva vidējo aritmētisko vērtību! (3 p.)
average = sum(atzimes) / len(atzimes)
print(average)
# vid. aritm. vērtība = atzīmju summa / atzīmju skaits (rezultātam vajadzētu būt 7.777777777777778)


