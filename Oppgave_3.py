# Karakterkaklulator
# Målet er å kunne bruke if,elif og else til å velge mellom alterantiver. 
# Python stopper med første betingelse som er sann

poeng = int(input("Hvor mange poeng fikk du ?"))

if poeng < 0 or poeng > 100:
    print("Feil, poeng må være mellom 0 og 100")
else:
    if poeng >= 90:
        print("A")
    elif poeng >= 80:
        print("B")
    elif poeng >= 60:
        print("C")
    elif poeng >= 50:
        print("D")
    elif poeng >= 40:
        print("E")
    else:
        print("F")
# tester programmet med 95,72,40 og 12 poeng.
# For 95 poeng karakter A, 72 karakter C, 40 karakter E, 12 karakter F.
if poeng < 0 or poeng > 100:
    print("Feil, poeng må være mellom 0 og 100")
else:
    if poeng >= 90:
        print("E")
    elif poeng >= 80:
        print("D")
    elif poeng >= 60:
        print("C")
    elif poeng >= 50:
        print("B")
    elif poeng >= 40:
        print("A")
    else:
        print("F")
#E gir 95, C gir 72, A gir 40, F gir 12

#Bytt ut alle elif med if

if poeng < 0 or poeng > 100:
    print("Feil, poeng må være mellom 0 og 100")
else:
    if poeng >= 90:
        print("A")
    if poeng >= 80:
        print("B")
    if poeng >= 60:
        print("C")
    if poeng >= 50:
        print("D")
    if poeng >= 40:
        print("E")
    else:
        print("F")
 # Får opp en melding som sier: feil, poeng må være mellom 0 og 100
 
# --- Refleksjon Oppgave 3 ---
#Da rekkefølgen ble snudd (steg 4), fikk 95 poeng "E" fordi sjekken (poeng >= 40) 
#kom først og var sann. 
#En `if/elif`-kjede stopper ved første sanne betingelse, mens 
#flere `if` etter hverandre sjekker alle linjene uansett. 
#Vi slipper å sjekke om poeng < 90 for "B", fordi alle med 90 eller mer 
#allerede ble fanget opp av den første `if`-sjekken. 
#`else`delen kjører bare dersom hverken`if` eller noen av 
#`elif`-betingelsene over var sanne.
            