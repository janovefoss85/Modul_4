# Gammel nok?
aldersgrense = 18
# Be bruker om å skrive alderen sin, og gjør den om til et heltall.
alder = input("Hvor gammel er du ?")
alder = int(alder)
print(alder)
#Skriv en if/else som sjekker alderen til bruker:
if alder >= aldersgrense:
    print (f"Du er {alder} år, og gammel nok.")
else:
    print(f"Du er {alder}år, og ikke gammel nok.")
#4.tester programmet med flere aldere.
#alder 17, forventer å få svar: Du er 17år, og ikke gammel nok.
#alder 18, froventer å få svar: Du er 18 år, og gammel nok.
#alder 19, forventer å få svar: DU er 19 år, og gammel nok.
#5.>Fjerner innrykket i den første printlinjen.
print("Takk for at du sjekket!")
#Utvidelse: bytter ut <= med >. tester med alderen 18. Det som skjer er at alder 18 ikke er innefor lengre.

#--- Refleksjon Oppgave 2 --- 
#Kolonet forteller Python hvor blokken starter, 
#og innrykket viser hvilke linjer som hører til inne i if/else. 
#Den siste linjen skrives ut uansett fordi den står helt uten innrykk på utsiden av if/else. 
#3Uttrykket (alder >= aldersgrense) gir True eller False. Hvis det er True, kjører if-koden. 
#>=er riktig fordi en på akkurat 18 år også skal regnes som gammel nok.






