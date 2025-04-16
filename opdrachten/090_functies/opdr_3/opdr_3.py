# Opdracht 1 functies
# Naam student:
# Groep:


def kubus_vol(m):
    return m ** 3


def bol_vol(r):
    return (4/3) * math.pi * (r ** 3)

import math

zijde = 5
radius = 4

if __name__ == "__main__":
    volume_kubus = kubus_vol(5)
    print(f"De inhoud van deze kubus is: {volume_kubus}")

    volume_bol = bol_vol(4)
    print(f"De inhoud van deze bol is: {volume_bol}")
