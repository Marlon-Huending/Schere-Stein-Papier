# Importieren
from random import choice
from importieren import ungerader_integer_prüfen, eingabe_prüfen, begrüßung

# Begrüßung
begrüßung("Herzlich Willkommen bei Schere-Stein-Papier!")

# Variablen
handzeichen = ["Schere", "Stein", "Papier"]
punkte_mensch = 0
punkte_computer = 0
runde = 1
spielsiege_mensch = 0
spielsiege_computer = 0


# Regeln?
antwort = eingabe_prüfen("Möchtest du die Regeln von diesem Spiel erfahren? ",
                        'Nur "ja" oder "nein" als Antwort nutzen! Bitte Antwort erneut eingeben. ',
                        ["ja", "nein"])
print()

if antwort == "ja":
   print("Bei Schere-Stein-Papier wählen beide Spieler ein Symbol.\n"
         "Jedes Symbol kann gegen das Symbol des anderen gewinnen oder verlieren.\n"
         "Dabei gilt: Stein schlägt Schere, Schere schlägt Papier und Papier schlägt Stein.\n"
         "Zu einem Unentschieden kommt es, wenn beide Spieler dasselbe Symbol wählen.\n"
         "Die Runde wird in diesem Fall wiederholt.\n")
   input("Zum fortsetzten drücke Enter\n")
elif antwort == "nein":
   print("Okay, dann geht es sofort los!\n")

# Wie viele Runden im ersten Spiel?
anzahl = ungerader_integer_prüfen("Wie viele Runden möchtest Du spielen (nur ungerade Rundenanzahl möglich, damit es einen Gewinner gibt)? ",
                                 "Deine Eingabe war keine Zahl! Bitte gebe die Rundenanzahl erneut ein. ",
                                 "Deine Eingabe war keine ungerade Zahl! Bitte gebe die Rundenanzahl erneut ein. ")
print()

# Schnick-Schnack-Schnuck läuft solange, bis es abgebrochen wird
while True:

   # ein Spiel ist nach den eingegebenen Runden beendet
   while runde != anzahl+1:

       # Rundenanzeige
       print("*** Runde", runde, "***")

       # Spielerhandzeichen und Computerhandzeichen
       mensch = eingabe_prüfen("Bitte wähle Dein Handzeichen. ",
                               str('Nur "Schere", "Stein" oder "Papier" als Antwort nutzen! Bitte Auswahl erneut eingeben. '),
                               handzeichen)
       computer = choice(handzeichen)

       # Rundenausgang ermitteln
       ausgaenge = {
           "SchereStein": False,
           "ScherePapier": True,
           "SteinPapier": False,
           "SteinSchere": True,
           "PapierSchere": False,
           "PapierStein": True,
       }

       if mensch == computer:
           print("Unentschieden! Der Computer wählte ebenfalls", computer, "\n",
                 "Es steht ", punkte_mensch, ":", punkte_computer, "\n",
                 "Die Runde wird nun wiederholt!\n")

       else:
           gewonnen = ausgaenge[str(mensch + computer)]
           if gewonnen:
               print("Gewonnen! Der Computer wählte", computer)
               punkte_mensch += 1
               print("Es steht ", punkte_mensch, ":", punkte_computer, "\n")
           else:
               print("Verloren! Der Computer wählte", computer)
               punkte_computer += 1
               print("Es steht ", punkte_mensch, ":", punkte_computer, "\n")
           runde += 1

   # Spielsieger ermitteln
   if punkte_mensch > punkte_computer:
       spielsiege_mensch += 1
       print("Du hast das Spiel", punkte_mensch, ":", punkte_computer, "gewonnen!\n"
             "In Spielen steht es somit nun ", spielsiege_mensch, ":", spielsiege_computer, "\n")
   elif punkte_mensch < punkte_computer:
       spielsiege_computer += 1
       print("Du hast das Spiel leider", punkte_mensch, ":", punkte_computer, "verloren!\n"
             "In Spielen steht es somit nun ", spielsiege_mensch, ":", spielsiege_computer, "\n")


   # nochmal spielen?
   antwort = eingabe_prüfen("Möchtest du nochmal spielen? ",
                            'Nur "ja" oder "nein" als Antwort nutzen! Bitte Antwort erneut eingeben. ',
                            ["ja", "nein"])
   print()
   if antwort == "nein":
       print("Okay. Auf Wiedersehen!\n")
       break
   else:
       punkte_mensch = 0
       punkte_computer = 0
       runde = 1

       # Spielsiege zurücksetzen?
       antwort = eingabe_prüfen("Möchtest du die Spielsiege von dir und dem Computer zurücksetzen? ",
                                'Nur "ja" oder "nein" als Antwort nutzen! Bitte Antwort erneut eingeben. ',
                                ["ja", "nein"])
       print()
       if antwort == "nein":
           print("Okay! Das nächste Spiel startet jetzt.\n")
       elif antwort == "ja":
           spielsiege_computer = 0
           spielsiege_mensch = 0
           print("Spielsiege wurden erfolgreich zurückgesetzt! Das nächste Spiel startet jetzt.\n")

       # Wie viele Runden in darauffolgenden Spielen?
       anzahl = ungerader_integer_prüfen(
           "Wie viele Runden möchtest Du dieses Mal spielen (zur Erinnerung: nur eine ungerade Rundenanzahl ist möglich)? ",
           "Deine Eingabe war keine Zahl! Bitte gebe die Rundenanzahl erneut ein. ",
           "Deine Eingabe war keine ungerade Zahl! Bitte gebe die Rundenanzahl erneut ein. ")
       print()