# Øving 1
# Oppgåve 1a
# a) Lese inn et tall fra brukeren, som er antall sekunder objektet har falt.
tid=float(input("Antal sekund objektet har falt: "))
# b) Regne ut farten i meter pr. sekund
AKSELERASJON=9.81
fart=AKSELERASJON*tid
round(fart,3)
# c) Distansen objektet har falt i meter
distanse = 0.5*fart*tid
round(distanse,3)
# d) skrive ut fart og distanse
print(f"Etter{tid} sekund har objektet falt {distanse:.2f}m og fell med farten {fart} m/s") #.2f fører til 2 desimalar


# Oppgåve 1b
tid=float(input("Antal sekund objektet har falt: "))
if tid>=0.0:
    AKSELERASJON=9.81
    fart=AKSELERASJON*tid
    round(fart,3)
    distanse = 0.5*fart*tid
    round(distanse,3)
    print(f"Etter{tid} sekund har objektet falt {distanse:.2f}m og fell med farten {fart} m/s")
else:
    print("tid må vera over 0")
print()


# Oppgåve 2c
pris_streng=input("Pris på vare:  ")
pris_flyt=float(pris_streng)
Sum=float(0)
while pris_flyt>0:
    Sum+=pris_flyt
    print("Foreløpig sum av varene er: "+str(Sum))
    pris_streng=input("Pris på vare:  ")
    pris_flyt=float(pris_streng)
else:
    print("Endelig sum av varene er: "+str(Sum))
    print("Avslutter")

# Alternativ
fortset=True
sum=0.0
while fortset:
    pris_streng=input("Pris på vare:  ")
    pris_flyt=float(pris_streng)
    if pris_flyt>0:
        sum += pris_flyt
        print("Foreløpig sum av varene er: "+str(sum))
    else:
        print("Endelig sum av varene er: "+str(sum))
        print("Avslutter")
        fortset=False

# Oppgåve 1d
tidsintervall=int(input("Velg tidsintervallstørrelsen: "))
antal_intervall=int(input("Velg antal intervall: "))
tidsintervall_slutt=tidsintervall*antal_intervall+1
if antal_intervall>=0.0 and tidsintervall>0.0:
    for tidint in range(tidsintervall,tidsintervall_slutt,tidsintervall):
        AKSELERASJON=9.81
        fart=AKSELERASJON*tidint
        print(f"Tid: {tidint} Fart: {fart:.2f}")
        distanse = 0.5*fart*tidint
        print(f"Tid: {tidint} Distanse: {distanse:.2f}")
else:
    print("Antal intervall og intervallstørrelse må vera positivt")

# oppgåve 1f
tid=float(input("Antal sekund objektet har falt: "))
while tid<0:
    print("tid må vera over 0")
    tid=float(input("Prøv på nytt: "+"Antal sekund objektet har falt: "))

akselerasjon=9.81
fart=akselerasjon*tid
round(fart,3)
distanse = 0.5*fart*tid
round(distanse,3)
print(f"Etter {tid} sekund har objektet falt {distanse:.2f} m og fell med farten {fart} m/s")
print()






