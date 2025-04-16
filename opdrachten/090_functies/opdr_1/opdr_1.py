# Opdracht 1 functies
# Naam student:
# Groep:


# Functie om tekst naar een bestand te schrijven
def write_to_file(file_name, text):
    """
    Schrijft tekst naar een bestand. Als het bestand al bestaat, wordt de tekst toegevoegd.

    :param file_name: De naam van het bestand (string)
    :param text: De tekst die moet worden weggeschreven (string)
    """
    try:
        # Open het bestand in append-modus ('a') om tekst toe te voegen
        with open(file_name, "a") as file:
            file.write(text + "\n")  # Schrijf de tekst en voeg een nieuwe regel toe
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")


# Voorbeeldgebruik van de functie
if __name__ == "__main__":
    my_tekst = "Schrijf dit maar even in een bestandje"
    my_file = "test.txt"
    write_to_file(my_file, my_tekst)

    # Nog een keer aanroepen om te tonen dat tekst wordt toegevoegd
    my_tekst2 = "Dit is nog een extra regel!"
    write_to_file(my_file, my_tekst2)
