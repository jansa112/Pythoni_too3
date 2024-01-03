# failist lugemine
f = open("Rintamäki.txt", "r")
nimed = list()
riik = list()
sugu = list()
tehnika = list()
komponendid = list()
karistused = list()

for rida in f:
    andmed = rida.split()
    nimed.append(andmed[0])
    riik.append(andmed[1])
    sugu.append(andmed[2])
    tehnika.append(float(andmed[3]))
    komponendid.append(float(andmed[4]))
    karistused.append(int(andmed[5]))

f.close()

# Meeste ja naiste keskmiste punktide arvutamine
m_tehnikapunktid_sum = 0
n_tehnikapunktid_sum = 0
m_mitu = 0
n_mitu = 0

for i in range(len(sugu)):
    if (sugu[i]) == "M":
        m_tehnikapunktid_sum = m_tehnikapunktid_sum + tehnika[i]
        m_mitu += 1
        
    else:
        n_tehnikapunktid_sum = n_tehnikapunktid_sum + tehnika[i]
        n_mitu += 1


m_tehnikapunktid_keskmine = m_tehnikapunktid_sum / m_mitu
n_tehnikapunktid_keskmine = n_tehnikapunktid_sum / n_mitu

print("Meeste tehnikapunktide keskmine on ", round(m_tehnikapunktid_keskmine, 2))
print("Naiste tehnikapunktide keskmine on ", round(n_tehnikapunktid_keskmine, 2))

if m_tehnikapunktid_keskmine < n_tehnikapunktid_keskmine:
    print("Naiste tehnikapunktide keskmine on kõrgem.")
    
elif m_tehnikapunktid_keskmine > n_tehnikapunktid_keskmine:
    print("Meeste tehnikapunktide keskmine on kõrgem.")
        
else:
    print("Meeste ja naiste tehnikapunktide keskmised on võrdsed.")
    

print("KESKMISEST KÕRGEMAD TULEMUSED TEHNIKAPUNKTIDES:")

for i in range(len(sugu)):
    if (sugu[i]) == "M":
        if tehnika[i] > m_tehnikapunktid_keskmine:
            erinevus = tehnika[i] - m_tehnikapunktid_keskmine
            # print(str(nimed[i]) + " ; mees " + " ; tehnikapunktid: " + str(tehnika[i]) + " ; erinevus keskmisest " + str(erinevus))
            
        else:
            continue
    if (sugu[i]) == "N":
        if tehnika[i] > n_tehnikapunktid_keskmine:
            erinevus = tehnika[i] - n_tehnikapunktid_keskmine
            # print(str(nimed[i]) + " ; naine" + " ; tehnikapunktid: " + str(tehnika[i]) + " ; erinevus keskmisest " + str(erinevus))
            nimi_n = nimed[i]
            skoor_n = tehnika[i]
            sugu_n = sugu[i]
            print(nimi_n, skoor_n, sugu_n)
            

for i in range(len(riik)):
    if (riik[i]) == "EST":
        est_tulemus = tehnika[i]
        indeks = riik.index("EST")
        est_sugu = sugu[indeks]
        est_nimi = nimed[indeks]
        break

koht = 1
vordseid = 0

for i in range(len(sugu)):
    if est_sugu == "M":
        if sugu[i] == "M":
            if est_tulemus < tehnika[i]:
                koht += 1
            else:
                if est_tulemus == tehnika[i]:
                    vordseid += 1
                    
        else:
            if sugu[i] == "N":
                continue
    else:
        if (sugu[indeks]) == "N":
            break

for i in range(len(sugu)):
    if sugu[indeks] == "N":
        if sugu[i] == "N":
            if est_tulemus < tehnika[i]:
                koht += 1
            else:
                if est_tulemus == tehnika[i]:
                    vordseid += 1
                    
        else:
            if sugu[i] == "M":
                continue
    
    else:
        if (sugu[indeks]) == "M":
            break
    
koht_loplik = koht + 1

print("Eestlastest andmestikus esimene on " + str(est_nimi) + " jäädes " + str(est_sugu) + " arvestuses " + str(koht_loplik) + ".kohale, punktisummaga " + str(est_tulemus)) 






        