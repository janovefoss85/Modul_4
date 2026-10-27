# Kombinere alt fra denne modulen: input (), f-strenger, if/elif/else, osv
# sammenliginingsoperatorer og logiske operatorer

riktig_brukernavn = "michael"
riktig_passord = "python123"

brukernavn = input("Skriv inn brukernavn: ")
passord = input("Skriv inn passord: ")  
alder = int(input("Hva er din alder? "))    

if brukernavn != riktig_brukernavn:
    print("ukjent bruker.")
elif passord != riktig_passord:
    print("feil passord.")
elif alder < 13:
    print("Du er for ung til å logge inn.")
else:
    print(f"Velkommen,{brukernavn}!")

# --- Refleksjon --- # 
#Løsningen bruker en if/elif/else-kjede. Dette er best her
#fordi vi ønsker å gi en spesifikk beskjed ut fra hva 
#som sviktet først. 
#Rekkefølgen krever at brukernavnet sjekkes før passordet,
#slik at vi ikke ber om passord/sjekker passord for en bruker 
#som ikke finnes. 
#Ekte nettsider gir ofte den generelle beskjeden. 
#«Feil brukernavn eller passord» av sikkerhetsgrunner, 
#slik at angripere ikke kan sjekke om et brukernavn eksisterer
#i systemet. 
#Det er viktig å teste alle kombinasjoner for å verifisere at koden
#håndterer både gyldige og ugyldige inndata riktig.