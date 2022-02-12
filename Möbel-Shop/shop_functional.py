# Möbel Shop Kommandozeilenprogramm - funktional
# Autor: Florian Lorch

import json
import os
# Funktion zum leeren der Kommandozeile
clear = lambda: os.system('cls')

# Definition Eingabemöglichkeiten
auswahlmöglichkeiten = [
        "Verlassen",
        "Nächtes Möbelstück",
        "Zu Warenkorb hinzufügen",
        "Aus Warenkorb entfernen",
        "Warenkorb Anzeigen",
        "Bestellung abschließen",
    ]

def main():
    # Einlesen der Warendatei
    warendatei = open("Möbel-Shop\waren.json","r")
    warenkatalog = json.loads(warendatei.read())["Waren"]

    # Aufruf der shop Funktion mit leerem warenkorb und erstem Artikel
    shop([], warenkatalog, 0)

def shop(warenkorb, warenkatalog, index):
    clear()
    # Falls das Ende des warenkatalogs erreicht ist,
    # wird wieder am Anfang begonnen
    if index > len(warenkatalog) - 1:
        index = 0
    # Auswahl des aktuellen Möbelstücks
    möbelstück = warenkatalog[index]

    # Anzeigen des Aktuellen Produkts
    print("Möbelstück:")
    print(json.dumps(möbelstück, indent=2))

    # Anzeigen der Auswahlmöglichkeiten
    print("Optionen:")
    for nummer, auswahl in enumerate(auswahlmöglichkeiten):
        print(f"{nummer}. {auswahl}")

    # Eingabe der Auswahl
    auswahl = input("Auswahl: ")

    # Lambda Funktion zur identifikation vom
    # aktuellen Möbelstück im Warenkorb
    möbelfilter = lambda x: x["Id"] == möbelstück["Id"]

    # Shop Verlassen
    if auswahl == "0":
        return

    # Nächstes Möbelstück
    elif auswahl == "1":
        # Erhöhung des Katalogindexes um 1
        shop(warenkorb, warenkatalog, index + 1)

    # Zu Warenkorb hinzufügen
    elif auswahl == "2":
        neu_warenkorb = hinzufügen(warenkorb, möbelstück, möbelfilter)
        shop(neu_warenkorb, warenkatalog, index)

    # Aus Warenkorb entfernen
    elif auswahl == "3":
        neu_warenkorb = entfernen(warenkorb, möbelfilter)
        shop(neu_warenkorb, warenkatalog, index)

    # Warenkorb Anzeigen 
    elif auswahl == "4":
        if warenkorb:
            menü(menü_warenkorb, warenkorb=warenkorb)
        shop(warenkorb, warenkatalog, index)

    # Bestellung abschließen
    elif auswahl == "5":
        if warenkorb:
            warenkorb_neu = menü(menü_bestellung,warenkorb=warenkorb)
            shop(warenkorb_neu, warenkatalog, 0)
        else:
            shop(warenkorb, warenkatalog, index)
    else:
        shop(warenkorb, warenkatalog, index)
    
def hinzufügen(warenkorb, möbelstück, möbelfilter):
    neu_warenkorb = warenkorb
    # Falls die Ware bereits im Warenkorb vorhanden -> Posten erhöhen
    vorhanden = list(filter(möbelfilter, neu_warenkorb))
    
    def posten_erhöhen(ware):
        ware["Menge"] += 1
        ware["Kosten"] += möbelstück["Preis"]

    list(map(posten_erhöhen, vorhanden))

    if not vorhanden:
        neu_warenkorb.append({
                "Id": möbelstück["Id"],
                "Name": möbelstück["Name"],
                "Menge": 1,
                "Kosten": möbelstück["Preis"]
            })
    
    print("> Ware \"" + möbelstück["Name"] + "\" zu Warenkorb hinzugefügt.")
    input()
    return neu_warenkorb

def entfernen(warenkorb, möbelfilter):
    neu_warenkorb = warenkorb
    vorhanden = list(filter(möbelfilter, neu_warenkorb))

    # Falls die Ware bereits im Warenkorb vorhanden
    def entfernen_warenkorb(ware):
        # Weniger als zwei mal -> Posten löschen
        if ware["Menge"] < 2:
            neu_warenkorb.remove(ware)
        # Mehr als ein mal -> Posten vermindern
        else:
            ware["Menge"] -= 1
        print("> Ware \"" + ware["Name"] + "\" aus Warenkorb entfernt.")
    list(map(entfernen_warenkorb, vorhanden))
    if not vorhanden:
        return neu_warenkorb
    input()
    return neu_warenkorb

# Wrapper Funktion für menüs
def menü(menü_funktion, **parameter):
    """
    Funktion die eine menü funktion ausführt, dessen wiedergabe Wert zurück gibt und die Kommandozeile verwaltet.
    
            Parameter: 
                        menü(funktion): Eine Menüfunktion
                        parameter(objekt): 
            
            Rückgabe:
                        result(objekt): Der Rückgabewert der Menüfunktion
    """
    clear()
    result = menü_funktion(**parameter)
    input()
    return result

def menü_warenkorb(**parameter):
    warenkorb = get_param("warenkorb", **parameter)
    
    print("Warenkorb:")
    print(json.dumps(warenkorb, indent=2))

def menü_bestellung(**parameter):
    warenkorb = get_param("warenkorb", **parameter)
    print("Bestellt:")
    total = 0
    for ware in warenkorb:
        name = ware["Name"]
        menge = ware["Menge"]
        kosten = ware["Kosten"]
        print(f"\n{name} (x{menge}) -> Preis: {kosten}")
        total += kosten
    print(f"Total: {total}")
    warenkorb = []
    return warenkorb

def get_param(name, **parameter):
    # Nach ausgewähltem Parameter filtern
    param = list(filter(lambda x: x == name, parameter))
    return parameter[param[0]]

if __name__ == "__main__":
    main()
