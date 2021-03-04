# Jaanus Paasoja
# 04.03.2021
# Kodutöö 3
# Ülikooli vastuvõetud
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
aastad = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
if aasta in aastad:
    i = aastad.index(aasta)
    print(str(aasta) + " aastal võeti vastu " + str(vastuvõetud[i])+ " inimest")
else :  print ("Selle aasta kohta andmeid ei ole")
print('')
#Jänesevanemate mure ver.3
ringide_arv = abs(int(input("Sisestage ringide arv: ")))
porgandite_arv = 0
for i in range(1,ringide_arv+1):
    if i %2 ==0:
        porgandite_arv = porgandite_arv + i
print(f"Saadavate porgandite koguarv on {porgandite_arv}.")
print('')
#Sissetulekud
sissetulekud = [] 
fail = open('konto.txt','r')
for rida in fail:
    sissetulekud.append(float(rida))
fail.close()
for sissetulek in sissetulekud:
    if sissetulek > 0:
        print(sissetulek)
print('')
#Jukebox
muusika=[]
lugu=[]
jrk=1
faili_loend=("jukebox.txt","80ndad.txt","eesti_muusika.txt","edm.txt")
failinimi=""
while not failinimi.endswith(faili_loend):
        failinimi = input("Palun sisestage õige faili nimi koos laiendiga (jukebox.txt, 80ndad.txt, eesti_muusika.txt, edm.txt): ")
else:
    print("Muusikapalade valik:")
fail=open(failinimi, encoding='UTF-8')
for rida in fail:
    rida=rida.rstrip()
    muusika.append(rida)
    print(jrk,'.',rida)
    lugu.append(jrk) 
    jrk+=1
fail.close()
print("")
laul=int(input("Valige laulu järjekorranumber: "))
for i in range(len(lugu)):
    if laul==lugu[i]:
        print("Mängitav muusikapala on:",muusika[i],'.')
print('')
#Tahvli juurde
from datetime import *
nimekiri = []
kuupaev = []
jrk = 1
faili_loend=("nimekiri.txt")
nr = datetime.now().day
failinimi = input("Sisestage failinimi (nimekiri.txt): ")
while not failinimi.endswith(faili_loend):
        failinimi = input("Sisestage failinimi (nimekiri.txt): ")
else:
    fail = open(failinimi, encoding='UTF-8')
for rida in fail:
    rida = rida.rstrip()
    nimekiri.append(rida)
    print(jrk,'. ',rida)
    kuupaev.append(jrk)
    jrk += 1
fail.close()
for i in range(len(kuupaev)):
    if nr == kuupaev[i]:
        print("Täna tuleb vastama:",nimekiri[i])
