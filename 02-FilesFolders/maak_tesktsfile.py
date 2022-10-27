import io 

# Zo open je een bestand om naar te schrijven 
bestand2 = open("test.txt", "r")

# Een tekst naar het bestand schrijven
bestand2.write("Lekker alles overschrijven");  

# Vergeet bestand niet te sluiten!
bestand2.close()