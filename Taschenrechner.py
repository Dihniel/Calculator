print("Bitte wählen Sie aus was Sie machen wollen:")
print("1=Addieren")
print("2=Subtrahieren")
print("3=Multiplizieren")
print("4=Dividieren")

wahl=input("Ihre Auswahl: ")

zahl_1=int(input("Bitte erste Zahl eingeben:"))
zahl_2=int(input("Bitte zweite Zahl eingeben:"))

if wahl=="1":
    ergebnis=zahl_1+zahl_2
    print("Ergebnis:", ergebnis)
elif wahl=="2":
    ergebnis=zahl_1-zahl_2
    print("Ergebnis:",ergebnis)
elif wahl=="3":
    ergebnis=zahl_1*zahl_2
    print("Ergebnis:",ergebnis)
elif wahl=="4":
    if zahl_2 !=0:
        ergebnis=zahl_1/zahl_2
        print("Ergebnis:",ergebnis)
    else:
        print("Division durch 0 ergibt das selbe was Du eingegeben hast Du Dummkopf!")
else:
    print("Ungültige Eingabe.")

