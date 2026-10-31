def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět",
                "šest", "sedm", "osm", "devět"]

    desitky = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

   
    cele_desitky = ["", "", "dvacet", "třicet", "čtyřicet",
               "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if cislo < 0 or cislo > 100:
        return "číslo musí být od 0 do 100"
    if cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return desitky[cislo - 10]
    elif cislo == 100:
        return "sto"
    elif cislo < 100:
        desitka = cislo // 10
        jednotka = cislo % 10

        if jednotka == 0:
            return cele_desitky[desitka]
        else:
            return cele_desitky[desitka] + " " + jednotky[jednotka]
    else:
        return "jiné číslo"




if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)
