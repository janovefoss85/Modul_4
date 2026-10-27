# Mål hente data fra bruker

#be bruker skrive inn navnet sitt
navn = input ("Hva heter du? ")
# Skrive ut hilsen til brukeren
print("Hei,", navn)

#annen måte å skrive ut hilsen til brukeren med f-string
print(f"Hei, {navn}!")
#Be brukeren skrive inn alderen sin, og skrive ut datatype:
alder = input("Hvor gammel er du? ")
alder = int(alder)
print(type(alder))
#prøver å regne ut hva alder blir til neste år:
print(alder + 1)
# får da feilmelding "can only concatenate str (not int) to str" retter dette opp med å skrive
# inn alder = int(alder) i linje 12
print(f"Du er {alder + 1} gammel til neste år")

#Utvidelse med å be bruker skrive høyden sin i meter. 
høyde = input ("hvor høy er du? ")
høyde = float(høyde)
print(høyde)
# hvis du bruker int får du feilmelding. Du må bruke float siden svaret har desimaler

# --- Refleksjon ---
# Har reflektert underveis i kodingen 
# Håper det går fint:)




