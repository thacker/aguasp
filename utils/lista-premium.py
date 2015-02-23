import csv

a = open("../dados/lista-premium-sabesp.txt", "r").readlines()
b = [i.strip() for i in a]

f = open("../dados/lista-premium.csv", "w")
w = csv.writer(f)
w.writerow(["id", "nome", "agua", "esgoto", "tarifa"])
print("Linhas ignoradas:")
for i in b:
    div = [x.strip() for x in i.split("   ") if x]
    if len(div) == 5:
        id_ = div[0]
        nome = div[1]
        agua = div[2]
        end = div[3]
        tarifa = div[4]
        w.writerow(div)
    else:
        print(div)
        print(len(div))
