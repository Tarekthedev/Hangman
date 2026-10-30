#Hangman
#Copyright (c) Tarekthedev 2026 
# Licensed under the MIT License.

from random import choice
import tkinter as tk

VERSUCHE = 6 #Settings
WORT = None
WORT_DATEI = "Woerter.txt"

class Hangmanspiel():
    def __init__(self):
        self.versuche=VERSUCHE

        if WORT != None:
            self.wort=WORT
        else:
            self.wörterdatei=open(WORT_DATEI,mode="r",encoding="UTF-8")
            self.wörterliste=self.wörterdatei.read()
            self.wörterdatei.close()
            self.wörterliste=self.wörterliste.split(",")
            self.wörterliste=[wort.strip() for wort in self.wörterliste] #entfernt whitespace 
            self.wort=choice(self.wörterliste)
        self.geraten=[]
        self.gewonnen=False
        self.versuche=VERSUCHE
        self.erzeuge_GUI()
        self.windows.mainloop() 
 
              
    def erzeuge_GUI(self):
        self.windows=tk.Tk()
        self.windows.title("Hangman")
        self.windows.geometry("600x500") #windows size
        self.windows.configure(bg="black") #Bg colour black
        tk.Label(self.windows,text="HANGMAN",font=("Arial", 30), fg="white", bg="black").pack() #write Hangman
        self.text = tk.Label(self.windows,text=f"Wilkommen bei Hangman!\nDu hast {VERSUCHE} Versuche um jeden Buchstaben zu raten\n",font=("Arial", 10), fg="white", bg="black")
        self.text.pack()
        self.wort_anzeige=tk.Label(self.windows,text=self.zeige_wort(),font=("Arial", 10), fg="white", bg="black")
        self.wort_anzeige.pack() #platziert es auf windows
        self.geratene_buchstaben_anzeige=tk.Label(self.windows,text=self.geraten,font=("Arial", 10), fg="white", bg="black")
        self.geratene_buchstaben_anzeige.pack()
        self.eingabe = tk.Entry(self.windows,width=10,font=("Arial", 18),bg="gray",fg="black")
        self.eingabe.pack()
        self.eingabe.bind("<Return>",self.spiel) #wenn enter: überprüfe ergebnis
        self.versuche_anzeige=tk.Label(self.windows,width=20,font=("Arial",10),bg="black",fg="white")
        self.versuche_anzeige.pack()


    def neue_runde(self):
        if WORT != None:
            self.wort=WORT
        else: 
            self.wort=choice(self.wörterliste)
        self.geraten=[]
        self.gewonnen=False
        self.versuche=VERSUCHE
        self.wort_anzeige.config(text=self.zeige_wort())
        self.geratene_buchstaben_anzeige.config(text=self.geraten)
        self.versuche_anzeige.config(text="")
        self.button.destroy()
        self.button2.destroy()



    def spiel(self,event=None):
        if not self.gewonnen and self.versuche != 0:
            self.buchstabe=self.eingabe.get().strip().lower()
            self.geratene_buchstaben_anzeige.config(text=self.geraten)
            if self.buchstabe in self.wort.lower() and self.buchstabe not in self.geraten and self.buchstabe != "" and len(self.buchstabe) == 1:
                self.text.config(text="Richtig!")
                self.geraten.append(self.buchstabe.lower())
                self.geratene_buchstaben_anzeige.config(text=self.geraten)
                self.wort_anzeige.config(text=self.zeige_wort())
            elif len(self.buchstabe) > 1:
                self.text.config(text="Tippe nur einen Buchstaben!")
            elif self.buchstabe.lower() in self.geraten:
                self.text.config(text="Diesen Buchstaben hast du schon geraten!")
            elif self.buchstabe == "":
                self.text.config(text="Tippe einen Buchstaben ein!")
            elif not self.buchstabe.isalpha():
                self.text.config(text="Tippe nur Buchstaben ein!")
            else:
                self.text.config(text="Falsch")
                self.versuche-=1
                if self.versuche <= 0:
                    self.text.config(text=f"Du hast verloren!\nDas Wort wäre {self.wort}!")
                    self.geratene_buchstaben_anzeige.config(text="Noch eine Runde?(j/n)")
                    self.button=tk.Button(self.windows,text="Ja",command=self.neue_runde)
                    self.button.pack()
                    self.button2=tk.Button(self.windows,text="Nein",command=self.windows.destroy)
                    self.button2.pack()
                else:
                    self.versuche_anzeige.config(text=f"Du hast noch {self.versuche} Versuche")
                    self.geraten.append(self.buchstabe.lower())
                    self.geratene_buchstaben_anzeige.config(text=self.geraten)
                    self.zeige_wort()
            self.eingabe.delete(0,tk.END)
        
            
    def zeige_wort(self):
        """Zeigt die _ mit den schon geratenen Buchstaben"""
        self.zwort="" #zeigenwort
        for buchstabe in self.wort:
            if buchstabe.lower() in self.geraten:
                self.zwort+=buchstabe
            else:
                self.zwort+="_ "
        if not "_" in self.zwort and self.versuche != 0: #da ist noch irgendein fehler
            self.gewonnen=True
            self.text.config(text=f"Du hast gewonnen!🎉")
            self.geratene_buchstaben_anzeige.config(text="Noch eine Runde?(j/n)")
            self.button=tk.Button(self.windows,text="Ja",command=self.neue_runde)
            self.button.pack()
            self.button2=tk.Button(self.windows,text="Nein",command=self.windows.destroy)
            self.button2.pack()

        return self.zwort


if __name__=="__main__":
    spiel=Hangmanspiel()

