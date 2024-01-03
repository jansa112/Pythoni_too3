# 06.01.22 Programmeerimise alused eksamitöö - Renat Ränk, RIF21

fail_sisse = open("covid19_vac.txt", "r")
haldusyksused = list()
liigid = list()
naised = list()
mehed = list()
yksdoosN = list()
yksdoosM = list()
t2ielikultN = list()
t2ielikultM = list()

for rida in fail_sisse:
    ajutine = rida.split()
    haldusyksused.append(ajutine[0])
    liigid.append(ajutine[1])
    naised.append(int(ajutine[2]))
    mehed.append(int(ajutine[3]))
    yksdoosN.append(int(ajutine[4]))
    yksdoosM.append(int(ajutine[5]))
    t2ielikultN.append(int(ajutine[6]))
    t2ielikultM.append(int(ajutine[7]))
fail_sisse.close()

# Kõige suurem elanike osakaal, kel vaktsineerimine pooleli
mitu = len(haldusyksused)
suurim_protsent = 0.0
for i in range(mitu):
    protsentN = ((yksdoosN[i] - t2ielikultN[i]) / naised[i]) * 100
    protsentM = ((yksdoosM[i] - t2ielikultM[i]) / mehed[i]) * 100
    protsent_kokku = protsentN + protsentM
    if protsent_kokku > suurim_protsent:
        suurim_protsent = protsent_kokku
        indeks = i
poolikult_vaktsineeritud = yksdoosM[indeks] + yksdoosN[indeks]    
print("Kõige suurema pooliku vaktsineeritusega inimese osakaal on järgmises haldusüksuses: ", haldusyksused[indeks], liigid[indeks], "Selles kohas on poolikult vaktsineeritud", poolikult_vaktsineeritud, "inimest ja nende osakaal elanikest on ", "{0:0.2f}".format(suurim_protsent), "protsenti.")

# Täielikult vaktsineeritud Eesti valdades kokku
ajutine1 = 0
t2ielikult_MN = 0
for j in range(mitu):
    if liigid[j] == "vald":
        ajutine1 = ajutine1 + (naised[j] + mehed[j])
        t2ielikult_MN = t2ielikult_MN + (t2ielikultM[j] + t2ielikultN[j])
protsent_valdades = t2ielikult_MN / ajutine1 * 100
print("Täielikult vaktsineeritute protsent Eesti valdades on", "{0:0.2f}".format(protsent_valdades), "protsenti.")

# Tabel
t2ielikult_vallaosakaal = 0.0
tulemus = ""
for i in range(mitu):
     if liigid[i] == "vald":
         
         t2ielikult_vallaosakaal = (t2ielikultN[i] + t2ielikultM[i]) / (naised[i] + mehed[i]) * 100
         erinevus = t2ielikult_vallaosakaal - protsent_valdades
         if erinevus > 0:
             
             tulemus = "parem"
             print("{0:15} {1:0.2f}  {2:0.2f}  {3:10}".format(haldusyksused[i], t2ielikult_vallaosakaal, erinevus, tulemus))
         else:
             tulemus = "kehvem"
             print("{0:15} {1:0.2f}  {2:0.2f}  {3:10}".format(haldusyksused[i], t2ielikult_vallaosakaal, erinevus, tulemus))
