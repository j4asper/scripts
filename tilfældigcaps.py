from os import system, name
from random import randint
import pyperclip

def close():
    exitornot = input("Skal du skrive noget mere? J/N: ")
    if exitornot.lower() == "j":
        clear()
        generate()
    else:
        exit()
def clear():
    # Hvis maskinen er windows 
    if name == 'nt': 
        _ = system('cls') 
    # Hvis maskinen er mac elelr linux 
    else: 
        _ = system('clear')
def generate():
    print("-----------------------------")
    print("|                           |")
    print("|  Tekst til Tilfældig Caps |")
    print("|      Lavet af: JAZPER     |")
    print("|    github.com/j4asper/    |")
    print("-----------------------------")
    print("")
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']
    #numbers = ["0" , "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    færdig = []

    tekst = input("Skriv din tekst her: ")

    for letter in tekst:
        if letter in alfabet:
            random = randint(1,2)
            if random == 1:
                newletter = letter.capitalize()
                færdig.append(newletter)
            else:
                færdig.append(letter)
        elif letter == " ":
            færdig.append(letter)
        else:
            færdig.append(letter)


    print("")
    print("")

    slut = ''.join(f'{letter}' for letter in færdig)
    print("Her er din færdige tekst:")
    print("Teksten er blevet kopieret, du skal bare indsætte den på Discord!")
    print("----------------------------")
    print("")
    print(slut)
    print("")
    print("----------------------------")
    print("")
    pyperclip.copy(slut)
    close()
generate()
