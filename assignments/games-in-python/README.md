# 📘 Assignment: Hangman Game

## 🎯 Objetivos

Build a classic word-guessing game in Python using strings, loops, conditionals, and user input while practicing game state management.

## 📝 Tarefas

### 🛠️ Create the main game logic

#### Descrição
Develop a hangman game where the player guesses letters to reveal a hidden word before running out of attempts.

#### Requisitos
O programa concluído deve:

- select a random word from a predefined list
- display the hidden word as underscores or blanks, such as `_ _ _ _`
- receive one letter at a time as user input
- check whether the guessed letter is in the secret word
- update the current state of the word as correct letters are found
- track remaining attempts and record incorrect guesses

### 🛠️ Define win and loss conditions

#### Descrição
Implement the end-of-game rules so the program clearly tells the player whether they won or lost.

#### Requisitos
O programa concluído deve:

- show a victory message when all letters are guessed correctly
- show a defeat message when the player runs out of attempts
- display the correct word at the end of the game
- end the round in a clear, readable way for the user
- use friendly, well-formatted terminal output