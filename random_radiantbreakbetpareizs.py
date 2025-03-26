import random
dators = random.randint(1,10)
lietotajs = 0
while lietotajs != dators:
    lietotajs=int(input("ievadi skaitili "))
if lietotajs > dators:
    print("par lielu")
elif lietotajs < dators:
    print("par zemu")
else:
    print("uzmineji")

