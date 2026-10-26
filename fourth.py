def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    aktualni_radek, aktualni_sloupec = aktualni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice

    # 1. KROK: Je cílová pozice na šachovnici?
    if not (1 <= cilovy_radek <= 8 and 1 <= cilovy_sloupec <= 8):
        return False

    # 2. KROK: Je cílová pozice volná?
    if cilova_pozice in obsazene_pozice:
        return False

    # Rozdíly mezi aktuální a cílovou pozicí
    rozdil_radku = abs(cilovy_radek - aktualni_radek)
    rozdil_sloupcu = abs(cilovy_sloupec - aktualni_sloupec)

    # 3. KROK: Pohyb podle typu figury
    if typ == "král":
        return (
            rozdil_radku <= 1
            and rozdil_sloupcu <= 1
            and (rozdil_radku + rozdil_sloupcu > 0)
        )

    elif typ == "jezdec":
        return (
            (rozdil_radku == 2 and rozdil_sloupcu == 1)
            or (rozdil_radku == 1 and rozdil_sloupcu == 2)
        )

    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice))  # False
  
