# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:



def encrypteer(tekst):
    encrypted_tekst = ""
    for char in tekst:
        if 'a' <= char <= 'z':  # Kleine letters
            encrypted_tekst += chr((ord(char) - ord('a') + 5) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':  # Hoofdletters
            encrypted_tekst += chr((ord(char) - ord('A') + 5) % 26 + ord('A'))
        else:  # Overige tekens (spaties, punctuatie, etc.)
            encrypted_tekst += char
    return encrypted_tekst


def decrypteer(encrypted_tekst):
    decrypted_tekst = ""
    for char in encrypted_tekst:
        if 'a' <= char <= 'z':  # Kleine letters
            decrypted_tekst += chr((ord(char) - ord('a') - 5) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':  # Hoofdletters
            decrypted_tekst += chr((ord(char) - ord('A') - 5) % 26 + ord('A'))
        else:  # Overige tekens (spaties, punctuatie, etc.)
            decrypted_tekst += char
    return decrypted_tekst


tekst = input("Geef de tekst die je wilt encrypteren: ")

encrypted_tekst = encrypteer(tekst)
print(f"Geëncrypteerde tekst: {encrypted_tekst}")

decrypted_tekst = decrypteer(encrypted_tekst)
print(f"Ondecrypteerde tekst: {decrypted_tekst}")

with open("encryptie_resultaten.txt", "w") as bestand:
    bestand.write(f"Originele tekst: {tekst}\n")
    bestand.write(f"Geëncrypteerde tekst: {encrypted_tekst}\n")
    bestand.write(f"Ondecrypteerde tekst: {decrypted_tekst}\n")

print("De resultaten zijn opgeslagen in 'encryptie_resultaten.txt'.")