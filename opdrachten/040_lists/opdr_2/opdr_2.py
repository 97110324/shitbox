# Opdracht 2 lists
# Naam student: [ Jouw naam ]
# Groep: [ Jouw groep ]


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Print de naam van de 1e rivier
# Print het 2e land waar de 1e rivier doorheen stroomt
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")

# Print de naam van de 2e rivier
# Print het 1e land waar de 1e rivier doorheen stroomt
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][0].capitalize()}")

# Print de naam van de 3e rivier
# Print het 3e land waar de 3e rivier doorheen stroomt
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info[rivieren[2]][2].capitalize()}")