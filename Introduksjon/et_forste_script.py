#oppgåve:rekne ut arealet til eit rom

#pseudokode
# Be brukar om lengde
# Be brukar om breidde
# Rekn ut areal
# skriv ut areal

lengde_streng=input("lengda til rommet: ")
lengde_flytall=float(lengde_streng)
breidde_streng=input("Breidden til rommet: ")
breidde_flyttal=float(breidde_streng)
areal=lengde_flytall*breidde_flyttal
areal_runda=round(areal,3)
print("arealet vart: "+str(areal_runda))


# Eksempel: Ønsker å skrive ut en forkant av stjerner, hvor brukeren
# angir høyde og bredde
#
# Bredde 5, høyde 3
# *****
# *****
# *****

bredde = int(input("Bredde: "))
hoyde = int(input("Høyde: "))
for linje in range(hoyde):
    for tall in range(bredde):
        print("*", end="")
    print()
