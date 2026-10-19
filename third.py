def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo
    a vrati True nebo False.
    """
    if cislo < 2:
        return False

    delitel = 2

    while delitel * delitel <= cislo:
        if cislo % delitel == 0:
            return False
        delitel += 1

    return True


def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum
    a vrati je jako seznam.
    """
    prvocisla = []

    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)

    return prvocisla


if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
