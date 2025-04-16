# Opdracht 1 functies
# Naam student:
# Groep:

CONVERSIEFACTOR = 1.609344

def kilometers_naar_miles(km):
    return km / CONVERSIEFACTOR
    # het woordje pass hieronder kun je weghalen


def miles_naar_kilometers(miles):
    return miles * CONVERSIEFACTOR    # het woordje pass hieronder kun je weghalen


kilometers = 1223
miles = 867

miles_resultaat = kilometers_naar_miles(kilometers)
print(f"{kilometers} kilometers = {miles_resultaat} miles")

km_resultaat = miles_naar_kilometers(miles)
print(f"{miles} miles = {km_resultaat} kilometers")