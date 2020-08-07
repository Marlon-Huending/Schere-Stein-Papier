# prüft, ob es sich bei einem Input um eine Zahl handelt
def integer_prüfen(text, zweittext):
    eingabe = input(text)
    while not eingabe.isdigit():
        eingabe = input(zweittext)
    return int(eingabe)

# prüft, ob es sich bei einem Input um eine ungerade Zahl handelt
def ungerader_integer_prüfen(text, zweittext, dritttext):
    eingabe = input(text)
    while True:
        if not eingabe.isdigit():
            eingabe = input(zweittext)
        elif int(eingabe) % 2 == 0:
            eingabe = input(dritttext)
        else:
            break
    return int(eingabe)

# prüft, ob es sich bei einem Input um ein erlaubtes Wort handelt
def eingabe_prüfen(text, zweittext, wörterliste):
    eingabe = input(text)
    while not eingabe in wörterliste:
        eingabe = input(zweittext)
    return eingabe

# Begrüßung
def begrüßung(text):
    print("*" * (len(text) + 3) + "*\n" +
          "* " + text + " *\n" +
          "*" * (len(text) + 3) + "*\n")