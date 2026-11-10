# Hangman
# Copyright (c) Tarekthedev 2026
# Licensed under the MIT License.

import json
from random import choice
import tkinter as tk
from tkinter import messagebox

SETTINGS_FILE = "assets/settings.json"


class HangmanGame:
    def __init__(self):
        self.load_settings()
        self.texts = self.load_language()

        if WORD is not None:
            self.word = WORD
        else:
            try:
                with open(WORD_FILE, mode="r", encoding="UTF-8") as word_file:
                    self.words = word_file.read().split(",")
                self.words = [word.strip() for word in self.words]
                self.word = choice(self.words)
            except:
                messagebox.showerror("File not found", "word.json was not found. Make sure it is located in the assets/ folder.")
        self.guessed_letters = []
        self.has_won = False
        self.attempts = MAX_ATTEMPTS
        self.create_gui()
        self.window.mainloop()

    def load_language(self):
        try:
            with open(LANGUAGE_FILE, mode="r", encoding="UTF-8") as language_file:
                languages = json.load(language_file)
            return languages.get(LANGUAGE, languages["en"])
        except FileNotFoundError:
            messagebox.showerror("File not found", "assets/languages.json was not found. Make sure it is located in the assets/ folder.")

    def load_settings(self):
        try:
            with open(SETTINGS_FILE, mode="r", encoding="UTF-8") as settings_file:
                settings = json.load(settings_file)
            global LANGUAGE, MAX_ATTEMPTS, WORD, WORD_FILE, LANGUAGE_FILE,COLOR_MODE
            LANGUAGE = settings.get("Language", "en")
            MAX_ATTEMPTS = settings.get("MaxAttempts", 6)
            WORD = settings.get("Word", None)
            WORD_FILE = settings.get("WordListFile", "assets/Words.txt")
            LANGUAGE_FILE = settings.get("LanguageFile", "assets/languages.json")
            COLOR_MODE = settings.get("ColorMode","dark")
        except FileNotFoundError:
            messagebox.showerror("File not found", "assets/settings.json was not found. Make sure it is located in the assets/ folder.")
            

    def create_gui(self):
        self.window = tk.Tk()
        self.window.title(self.texts["title"])
        self.window.geometry("600x400")
        if COLOR_MODE == "dark": 
            self.fgc="white"
            self.bgc="black"
        else:
            self.fgc="black"
            self.bgc="white"
        self.window.configure(bg=self.bgc)
        try:
            self.window.iconbitmap("assets/icon.ico")
        except tk.TclError:
            ...
        self.window.resizable(False, False)
        self.title=tk.Label(self.window, text=self.texts["title"], font=("Arial", 30), fg=self.fgc, bg=self.bgc)
        self.title.pack()
        self.status_label = tk.Label(
            self.window,
            text=self.texts["welcome"].format(attempts=MAX_ATTEMPTS),
            font=("Arial", 10),
            fg=self.fgc,
            bg=self.bgc,
        )
        self.status_label.pack()
        self.word_label = tk.Label(
            self.window, text=self.display_word(), font=("Arial", 10), fg=self.fgc, bg=self.bgc
        )
        self.word_label.pack()
        self.guessed_letters_label = tk.Label(
            self.window, text=self.guessed_letters, font=("Arial", 10), fg=self.fgc, bg=self.bgc
        )
        self.guessed_letters_label.pack()
        self.change_language_button = tk.Button(
            self.window, text=self.texts["change_language"], command=self.change_language,bg=self.bgc, fg=self.fgc
        )
        self.change_language_button.place(x=10, y=10)
        self.change_color_mode_button=tk.Button(
            self.window,text="🌙",command=self.change_color_mode,bg=self.bgc, fg=self.fgc, font=("Segoe UI Emoji",10)
        )
        self.play_again_button = tk.Button(
        self.window, text=self.texts["yes"], command=self.start_new_round
                    )
        self.quit_button = tk.Button(self.window, text=self.texts["no"], command=self.window.destroy)
        self.change_color_mode_button.place(x=10, y=40)
        self.restart_game_button=tk.Button(self.window,text="🔄️",command=self.start_new_round,fg=self.fgc, bg=self.bgc, font=("Segoe UI Emoji",10))
        self.restart_game_button.place(x=50,y=40)
        self.letter_entry = tk.Entry(self.window, width=10, font=("Arial", 18), bg="gray", fg="black",)
        self.letter_entry.pack()
        self.letter_entry.bind("<Return>", self.play)
        self.attempts_label = tk.Label(self.window, width=20, font=("Arial", 10), bg=self.bgc, fg=self.fgc)
        self.attempts_label.pack()

    def change_color_mode(self):
        if self.fgc == "white": self.fgc = "black";self.change_color_mode_button.config(text=" ☀️") 
        else: self.fgc = "white";self.change_color_mode_button.config(text=" 🌙")
        if self.bgc == "white": self.bgc = "black"; 
        else: self.bgc = "white"

        self.window.configure(bg=self.bgc)
        self.status_label.config(bg=self.bgc, fg=self.fgc)
        self.word_label.config(bg=self.bgc, fg=self.fgc)
        self.guessed_letters_label.config(bg=self.bgc, fg=self.fgc)
        self.change_language_button.config(bg=self.bgc, fg=self.fgc)
        self.letter_entry.config(bg="gray", fg="black")
        self.attempts_label.config(bg=self.bgc, fg=self.fgc)
        self.change_color_mode_button.config(bg=self.bgc, fg=self.fgc)
        self.title.config(bg=self.bgc, fg=self.fgc)
        self.restart_game_button.config(bg=self.bgc, fg=self.fgc)
        self.window.update_idletasks() #?

    def change_language(self):
        global LANGUAGE
        LANGUAGE = {"en": "de", "de": "es", "es": "en"}.get(LANGUAGE, "en")
        self.texts = self.load_language()
        self.window.title(self.texts["title"])
        self.status_label.config(text=self.texts["welcome"].format(attempts=MAX_ATTEMPTS))
        self.word_label.config(text=self.display_word())
        self.guessed_letters_label.config(text=self.guessed_letters)
        self.change_language_button.config(text=self.texts["change_language"])
        self.attempts_label.config(text="")

    def start_new_round(self):
        if WORD is not None:
            self.word = WORD
        else:
            self.word = choice(self.words)
        self.guessed_letters = []
        self.has_won = False
        self.attempts = MAX_ATTEMPTS
        self.word_label.config(text=self.display_word())
        self.guessed_letters_label.config(text=self.guessed_letters)
        self.attempts_label.config(text="")
        self.status_label.config(text=self.texts["welcome"].format(attempts=MAX_ATTEMPTS))
        self.play_again_button.destroy()
        self.quit_button.destroy()

    def play(self, event=None):
        if not self.has_won and self.attempts != 0:
            self.guessed_letter = self.letter_entry.get().strip().lower()
            self.guessed_letters_label.config(text=self.guessed_letters)
            if (
                self.guessed_letter in self.word.lower()
                and self.guessed_letter not in self.guessed_letters
                and self.guessed_letter != ""
                and len(self.guessed_letter) == 1
            ):
                self.status_label.config(text=self.texts["correct"])
                self.guessed_letters.append(self.guessed_letter)
                self.guessed_letters_label.config(text=self.guessed_letters)
                self.word_label.config(text=self.display_word())
            elif len(self.guessed_letter) > 1:
                self.status_label.config(text=self.texts["single_letter"])
            elif self.guessed_letter in self.guessed_letters:
                self.status_label.config(text=self.texts["already_guessed"])
            elif self.guessed_letter == "":
                self.status_label.config(text=self.texts["empty"])
            elif not self.guessed_letter.isalpha():
                self.status_label.config(text=self.texts["not_alpha"])
            else:
                self.status_label.config(text=self.texts["wrong"])
                self.attempts -= 1
                if self.attempts <= 0:
                    self.status_label.config(text=self.texts["lose"].format(word=self.word))
                    self.guessed_letters_label.config(text=self.texts["play_again"])
                    self.play_again_button.pack()
                    self.quit_button.pack()
                else:
                    self.attempts_label.config(
                        text=self.texts["attempts_left"].format(attempts=self.attempts)
                    )
                    self.guessed_letters.append(self.guessed_letter)
                    self.guessed_letters_label.config(text=self.guessed_letters)
                    self.display_word()
            self.letter_entry.delete(0, tk.END)

    def display_word(self):
        self.displayed_word = ""
        for letter in self.word:
            if letter.lower() in self.guessed_letters:
                self.displayed_word += letter
            else:
                self.displayed_word += "_ "
        if "_" not in self.displayed_word and self.attempts != 0:
            self.has_won = True
            self.status_label.config(text=self.texts["win"])
            self.guessed_letters_label.config(text=self.texts["play_again"])
            self.play_again_button = tk.Button(self.window, text=self.texts["yes"], command=self.start_new_round)
            self.play_again_button.pack()
            self.quit_button = tk.Button(self.window, text=self.texts["no"], command=self.window.destroy)
            self.quit_button.pack()

        return self.displayed_word


if __name__ == "__main__":
    game = HangmanGame()