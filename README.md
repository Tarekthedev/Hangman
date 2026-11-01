# Hangman

<a href="#english">English</a> | <a href="#deutsch">Deutsch</a>

![Python](https://img.shields.io/badge/Python-3-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Hangman](Screenshot1.png)

## English

A Hangman game with a graphical interface, written in Python and Tkinter. Guess the randomly selected word one letter at a time before you run out of attempts.

### Requirements

- Python 3
- Tkinter

On Linux, Tkinter may need to be installed separately, depending on your distribution. If you see an error related to `tkinter` when starting the game, install your distribution's Tkinter package.

### Run the game

Make sure `Hangman.py` and `Words.txt` are in the same folder. Open a terminal in that folder and run:

```bash
python Hangman.py
```

On some systems, use `python3 Hangman.py` instead.

### How to play

1. The game displays the hidden word as underscores.
2. Enter a letter in the input field and press Enter.
3. Correct letters are revealed in the word. Each incorrect guess costs one attempt.
4. Previously guessed letters, empty input, and entries containing more than one character do not count as incorrect guesses.
5. Once you guess the word or run out of attempts, you can start a new round or close the window.

### Customise the word list

The words are stored in `Words.txt`. You can add your own words, separated by commas. For example:

```text
Apple,Tree,Python,Computer
```

The file is read as UTF-8. Keep it in the same folder as `Hangman.py` and make sure it contains at least one word.

### Settings

| Setting | What it does | Values |
| --- | --- | --- |
| `MAX_ATTEMPTS` | Sets the number of attempts per round. | Any positive number; default: `6` |
| `WORD` | Uses a fixed word instead of choosing one at random. | `None` for a random word, or a word in quotation marks; default: `None` |
| `WORD_FILE` | Selects the file containing the words. | A file name; default: `"Words.txt"` |
| `LANGUAGE` | Selects the language used by the interface. | `"en"` for English, `"de"` for German, or `"es"` for Spanish; default: `"en"` |
| `LANGUAGE_FILE` | Selects the file containing the interface text. | A file name; default: `"languages.json"` |

### Licence

This project is distributed under the MIT Licence. See [LICENSE](LICENSE) for details.

© 2026 Tarekthedev


## Deutsch

Ein Hangman-Spiel mit grafischer Oberfläche, geschrieben in Python und Tkinter. Errate das zufällig ausgewählte Wort Buchstabe für Buchstabe, bevor dir die Versuche ausgehen.

### Voraussetzungen

- Python 3
- Tkinter

Unter Linux kann Tkinter je nach Distribution separat installiert werden. Falls beim Start ein Fehler zu `tkinter` erscheint, installiere das Tkinter-Paket deiner Distribution.

### Starten

Speichere `Hangman.py` und `Woerter.txt` im selben Ordner. Öffne ein Terminal in diesem Ordner und starte das Spiel mit:

```bash
python Hangman.py
```

Auf manchen Systemen lautet der Befehl stattdessen `python3 Hangman.py`.

### Spielen

1. Das Spiel zeigt das gesuchte Wort zunächst als Unterstriche an.
2. Gib einen Buchstaben in das Eingabefeld ein und drücke Enter.
3. Richtige Buchstaben werden im Wort aufgedeckt. Bei einem falschen Buchstaben verlierst du einen Versuch.
4. Bereits geratene Buchstaben, leere Eingaben und Eingaben mit mehr als einem Zeichen werden nicht als Fehlversuch gezählt.
5. Errätst du das Wort oder sind alle Versuche aufgebraucht, kannst du eine neue Runde starten oder das Fenster schließen.

### Wörter anpassen

Die Wörter stehen in `Words.txt`. Du kannst auch deine eigenen hinzufügen. Trenne sie dann durch Kommas (","). Beispiel:

```text
Apfel,Baum,Python,Computer
```

Die Datei wird als UTF-8 gelesen. Achte darauf, dass sie neben `Hangman.py` liegt und mindestens ein Wort enthält.

### Einstellungen

| Funktion | Was sie macht | Werte |
| --- | --- | --- |
| `MAX_ATTEMPTS` | Legt die Anzahl der Versuche pro Runde fest. | Jede positive Zahl; Standard: `6` |
| `WORD` | Verwendet ein festes Wort, statt zufällig eines auszuwählen. | `None` für ein zufälliges Wort oder ein Wort in Anführungszeichen; Standard: `None` |
| `WORD_FILE` | Legt die Datei mit den Wörtern fest. | Ein Dateiname; Standard: `"Words.txt"` |
| `LANGUAGE` | Legt die Sprache der Benutzeroberfläche fest. | `"en"` für Englisch, `"de"` für Deutsch oder `"es"` für Spanisch; Standard: `"en"` |
| `LANGUAGE_FILE` | Legt die Datei mit den Texten der Benutzeroberfläche fest. | Ein Dateiname; Standard: `"languages.json"` |

### Lizenz

Dieses Projekt steht unter der MIT License. Weitere Informationen sind in der Datei [LICENSE](LICENSE).

© 2026 Tarekthedev
