def saskaiti(x, y):
    return x + y
def atnemt(x, y):
    return x - y
def reizinat(x, y):
    return x * y
def dalits(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("nedali ar nuli monkey")
while True:
        darbiba = input("Izvelies operaciju: skaitisana (1), atnemt (2), reizinat (3), dalit (4), ieraksti balls , lai aizvert programmu: ")
        if darbiba == "balls":
            break

        x = int(input("pirmais:"))
        y = int(input("otrais:"))

        if darbiba == "1":
            print(x, "+", y, "=", saskaiti(x, y))
        elif darbiba == "2":
            print(x, "-", y, "=", atnemt(x, y))
        elif darbiba == "3":
            print(x, "*", y, "=", reizinat(x, y))
        elif darbiba == "4":
            print(x, "/", y, "=", dalits(x, y))
