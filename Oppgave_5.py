#Oppgave 5 finn feilen 2.0
riktig_svar = "Oslo"
svar = input("Hva er hovedstaden i Norge? ")
            
if svar == riktig_svar:
    print("Riktig!")
else:
    print("Feil!, svaret var", riktig_svar)

int()   
alder = int(input("Hvor gammel er du? "))

  
if alder == (18):
    print("Du er akkurat myndig.!")
else:
    print("Du er ikke 18.")

# --- Refleksjon Oppgave 5 --- 
#Feilene var: tildeling (=) i stedet for sammenligning (==), manglende 
#kolon (:), manglende innrykk, og at alder var tekst i stedet for tall. 
#Den siste feilen ga ingen feilmelding fordi det er lov å sammenligne
#tekst og tall i Python, men det blir alltid False. 
#En syntaksfeil stopper koden med en feilmelding, mens en logisk feil gjør
#at koden kjører men gir feil svar. Logiske feil er farligst fordi de er 
#vanskeligere å oppdage. 
#Det er lurt å teste med grenseverdier, som akkurat 18, 
#tall over/under 18,og feil case på teksten.

