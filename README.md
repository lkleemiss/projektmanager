# Projektmanager

Mit dieser Webanwendung kannst du deine Projekte und Aufgaben planen und deine jeweilige Arbeitszeit für das Projekt tracken.

Demo-Webseite: https://lkleemiss.pythonanywhere.com/

Login-Daten: oos2022

***
## Kontakt
Line Kleemiß

Mail: [line.kleemiss@stud.th-luebeck.de](mailto:line.kleemiss@stud.th-luebeck.de) // [line.kleemiss@gmail.com](mailto:line.kleemiss@gmail.com)

***
## Nutzungsinformation

Die Webanwendung ist auf die Desktop-Nutzung ausgerichtet. Bei Geräten unter 1600px Breite kommt es zu Darstellungsfehlern.

***
## Development

### Dependencies

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
### Admin Dashboard

Superuser: line.kleemiss@gmail.com / PW: meinpasswort
```
python manage.py createsuperuser
```

***

## Funktionen der Anwendung

### Login/Registrierung

Registriere dich oder logge dich einfach mit deiner E-Mail und deinem Passwort auf https://lkleemiss.pythonanywhere.com/login ein. 

Falls du ein Passwort vergessen hast, kannst du auch ein neues über https://lkleemiss.pythonanywhere.com/passwort-vergessen/ anfordern, du bekommst die Anleitung dann per E-Mail.

### Allgemein

Die Anwendung ist sehr schlicht gehalten, rechts findest du den Seiten-Content, auf der linken Seite das Menü. Dieses kann mit dem türkisenen Button im Header des Contents auf- und zugeklappt werden.

Das Menü enthält die Buttons für das Dashboard, dein Profil, einen Button zum Ausloggen und die Projekt-Übersicht. Bei Klick auf den Dropdown-Pfeil bei den Projekten gibt es noch ein Menü mit deinen 3 zuletzt bearbeiteten Projekten, damit du diese möglichst schnell erreichen kannst.

### Dashboard
Auf dem Dashboard erhältst du alle wichtigen Informationen auf einem Blick.

Ein kurzer Überblick über die Anzahl an Aufgaben und eine Auflistung der geplanten Aufgaben für den Heute, Morgen und Demnächst. Aufgaben dessen Deadline bereits fällig war werden unter Überfällig angezeigt. Zusätzlich gibt es auch noch eine kleine Statistik, wie weit dein Fortschritt beim Bearbeiten deiner Aufgaben sind.

Danach folgt ein kurzer Überblick über die Anzahl an Projekten und die Auflistung deiner 3 zuletzt bearbeiten Projekte. Alle anderen kannst du in der Projekt-Übersicht einsehen.
Bei Klick auf das Bild deiner Projekt-Mitglieder kommst du auf dessen Profil.

Neben den Projekten befindet sich noch die Information wie viele Stunden du heute und wie viele insgesamt gearbeitet hast.

### Profil
Hier hast du eine Übersicht zu deinen Profil-Daten und kannst diese bearbeiten.

### Projekte

In der Projekt-Übersicht findest du alle deine erstellten Projekte. Diese werden nach Zeitpunkt der letzten Änderung sortiert. Zusätzlich gibt es die wichtigsten Informationen auf einem Blick. Rechts befinden sich jeweils das Bearbeiten und Löschen Button. Mit Klick auf den Titel kommst du in die Projekt-Ansicht und das Stift-Icon führt dich in die Bearbeitung. Mit dem X kannst du das Projekt löschen.

### Projekt-Ansicht

Das Herz-Stück der Anwendung, hier kannst du dein Projekt planen. Bist du Projektmanager kannst du das Projekt bearbeiten und löschen. Team-Mitglieder können nur die Aufgaben des Projektes bearbeiten.

Im Aufgabenbereich kannst du alle Aufgaben einsehen, eine neue Aufgabe hinzufügen und Aufgaben als erledigt markieren. 

Auf der rechten Seite finden sich alle Daten zum Zeit-Tracking. Eine Stoppuhr zum aktiven tracken deiner Arbeitszeit und ein Formular zum Nachtragen von Zeiten, falls du mal vergessen hast auf Play zu drücken. Für die Uhr einfach auf Play drücken und wenn du fertig bist deine Zeit abspeichern. Wenn du die App zwischendurch schließt, ist das auch kein Problem.

Darunter folgt noch die Tabelle mit allen bisher getrackten Zeiten, alte Einträge können auch nochmal bearbeitet oder gelöscht werden.

### Projekt bearbeiten
Hier können die Projekte bearbeitet werden. Füge eine Beschreibung hinzu, setzte eine Deadline und wähle den aktuellen Status deines Projektes aus. 
Möchtest du im Team arbeiten? Einfach die Checkbox auswählen, speichern und dann die Mitglieder hinzufügen.

Sofern dein Projekt ein Team-Projekt ist, öffnet sich in der Bearbeitungs-Ansicht noch ein weiteres Feld, wo alle Mitglieder aufgeführt werden. Diese kannst du dort mit dem x auch löschen. Ein neues Mitglied einfach hinzufügen, indem du dessen Mail angibst. 

