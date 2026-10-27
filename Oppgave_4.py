# Billettluka, mål: kombinere betingelser med logiske operatorer
#alder = 25
#er_student = True
#har_medlemskort = False

# skriv ut resultatet av hvert uttrykk under. Skriv først en kommentar med hva du tror svaret blir, og sjekk deretter
# 1. False 
#print(alder < 12 or alder > 67) 
# 2. True
#print(er_student and alder < 30)
# 3. False
#print(not har_medlemskort)
# 4. False siden ikke begge sidene er sanne.
#print(er_student and har_medlemskort)
# 5. True siden minst den ene siden er sann
#print(er_student or har_medlemskort)
# True snur verdien av uttrykket, og siden er_student er True, blir det False 
#print(not er_student or alder < 30)

#Del 2
## Et museum har disse prisene.
#barn under 12 og pensjonister over 67 år = gratis
#studenter under 30 år = 50 
#alle andre = 120 



alder = int(input("Hvor gammel er du? "))
er_student = input("Er du student? (ja/nei) ").lower() == "ja"

print(er_student)

#Barn under 12 og pensjonister over 67 år = gratis
#studenter under 30: 50kr
#alle andre 120kr

if alder < 12 or alder > 67:
    print("Du får gratis inngang.")
elif er_student and alder < 30:
    print("Du skal betale 50 kr for inngang.")
else:
    print("Du skal betale 120 kr for inngang.")

if not er_student:
    print("Tips: Studenter under 30år får rabatt")

#8år og ikke student = Gratis
#70år og ikke student = Gratis
#22år og student = 90kr
#35år og student = 120kr
#25år og ikke student = 120kr

# --- Refleksjon Oppgave 4 --- 
#'and' krever at begge betingelsene er sanne, mens 'or' holder at 
#minst én av dem er sann. 
#35-åringen fikk ordinær pris (120 kr) fordi studentrabatten krever
#at du er under 30 år. 
#'not' snur True til False. Uten 'not' kunne vi skrevet:
#if er_student == False:
#70-åringen får gratis billett fordi den første sjekken (alder > 67)
#slår inn før studentsjekken.