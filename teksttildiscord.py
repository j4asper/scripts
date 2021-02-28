from os import system, name
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
    print("| Tekst til Discord letters |")
    print("|      Lavet af: JAZPER     |")
    print("|    github.com/j4asper/    |")
    print("-----------------------------")
    print("")
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ["0" , "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    færdig = []

    tekst = input("Skriv din tekst her: ")

    for letter in tekst:
        if letter.lower() in alfabet:
            færdig.append(f":regional_indicator_{letter.lower()}:")
        elif letter == " ":
            færdig.append("     ")
        elif letter == "æ":
            færdig.append(":regional_indicator_a:")
            færdig.append(":regional_indicator_e:")
        elif letter == "ø":
            færdig.append(":regional_indicator_o:")
            færdig.append(":regional_indicator_e:")
        elif letter == "å":
            færdig.append(":regional_indicator_a:")
            færdig.append(":regional_indicator_a:")
        elif letter == "?":
            færdig.append(":question:")
        elif letter == "!":
            færdig.append(":exclamation:")
        elif letter == ".":
            færdig.append("**.**")
        elif letter == ",":
            færdig.append("**,**")
        elif letter == "-":
            færdig.append("**-**")
        elif letter == "/":
            færdig.append("**/**")
        elif letter == "\\":
            færdig.append("**\**")
        elif letter in numbers:
            if letter == "0":
                færdig.append(":zero:")
            elif letter == "1":
                færdig.append(":one:")
            elif letter == "2":
                færdig.append(":two:")
            elif letter == "3":
                færdig.append(":three:")
            elif letter == "4":
                færdig.append(":four:")
            elif letter == "5":
                færdig.append(":five:")
            elif letter == "6":
                færdig.append(":six:")
            elif letter == "7":
                færdig.append(":seven:")
            elif letter == "8":
                færdig.append(":eight:")
            elif letter == "9":
                færdig.append(":nine:")
            else:
                pass
        else:
            pass
    print("")
    print("")

    slut = ' '.join(f'{letter}' for letter in færdig)
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
