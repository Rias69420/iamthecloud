import random
dators = random.randint(1,10)
lietotajs = 0
lietotajs=int(input("ievadi skaitili "))
if lietotajs > dators:
    print("par lielu")
elif lietotajs < dators:
    print("par zemu")
elif lietotajs == dators:
    print("pareiza atbilde")
while lietotajs != dators:
    print(dators)
    break
