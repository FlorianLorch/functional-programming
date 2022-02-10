import json
import os
# Funktion zum leeren der Kommandozeile
clear = lambda: os.system('cls')

# Initialisierung globaler variablen
warenkorb = []
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

    auswahl = None
    i = 0
    while auswahl != "0":
        clear()
        # Akutuelles Möbelstück
        möbelstück = warenkatalog[i]
        # Anzeigen des Aktuellen Produkts
        print("Möbelstück:")

        print(json.dumps(möbelstück,indent=2))

        # Anzeigen der Auswahlmöglichkeiten
        print("Optionen:")
        for index, auswahl in enumerate(auswahlmöglichkeiten):
            print(f"{index}. {auswahl}")

        # Eingabe der Auswahl
        auswahl = input("Auswahl: ")

        # Nächstes Möbelstück
        if auswahl == "1":
            if i < len(warenkatalog)-1:
                i += 1
            else:
                i = 0

        # Zu Warenkorb hinzufügen
        if auswahl == "2":
            vorhanden = False
            # Falls die Ware bereits im Warenkorb vorhanden -> Posten erhöhen
            for ware in warenkorb:
                if ware["Id"] == möbelstück["Id"]:
                    vorhanden = True         
                    ware["Menge"] += 1
                    ware["Kosten"] += möbelstück["Preis"]

            # Falls nicht -> Neuen Posten hinzufügen
            if not vorhanden:    
                warenkorb.append({
                    "Id": möbelstück["Id"],
                    "Name": möbelstück["Name"],
                    "Menge": 1,
                    "Kosten": möbelstück["Preis"]
                })
            print(
                "> Ware \"" + 
                möbelstück["Name"]
                + "\" zu Warenkorb hinzugefügt."
            )
            input()

        # Aus Warenkorb entfernen
        if auswahl == "3":
            # Falls die Ware bereits im Warenkorb vorhanden
            for ware in warenkorb:
                if ware["Id"] == möbelstück["Id"]:
                    # Weniger als zwei mal -> Posten löschen
                    if ware["Menge"] < 2:
                        warenkorb.remove(ware)
                    # Weniger mehr als ein mal -> Posten vermindern
                    else:
                        ware["Menge"] -= 1
                    print("> Ware \"" + ware["Name"] + "\" aus Warenkorb entfernt.")
                    input()

        # Warenkorb Anzeigen 
        if auswahl == "4":
            clear()
            print("Warenkorb:")
            print(json.dumps(warenkorb, indent=2))
            input()
        
        # Bestellung abschließen
        if auswahl == "5":
            if warenkorb:
                clear()
                print("Bestellt:")
                total = 0
                for ware in warenkorb:
                    name = ware["Name"]
                    menge = ware["Menge"]
                    kosten = ware["Kosten"]
                    print(f"\n{name} (x{menge}) -> Preis: {kosten}")
                    total += kosten
                print(f"Total: {total}")
                warenkorb.clear()
                input()

if __name__ == "__main__":
    main()
