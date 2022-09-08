import os
from dictionary import letter_dict
import pyperclip

# Morse code translator
print("Welcome to the Morse Code translator!\n")


# Convertor Function
def convert(text):
    morse_str = ""
    for letter in text:
        if letter in letter_dict:
            morse_str += letter_dict[letter]
            morse_str += " "
        else:
            # For unadmitted characters
            morse_str += "*?*"
    return morse_str


# Translate Function

def translate(code):
    code = code.split(" ")
    text = ""
    for letter in code:
        value = [i for i in letter_dict if letter_dict[i] == letter]
        if value:
            text += value[0]
    return text


def using():
    response = input("Do you wish to keep using the morse translator?(Y/N):\n").lower().strip()
    if response == "y":
        using = True
    elif response == "n":
        using = False
    else:
        print("Not a valid answer, please restart the program")
        using = False
    return using


result = False
run = True

while run:

    mode = input("Which mode you want to use?\n1 Text insert\n2 Morse Code translation\n").strip()

    if mode == "1":
        text = input("Input your text:\n").lower().strip()
        result = convert(text)
        print(f"Your converted text to morse is:\n\n{result}")
        question = input("Do you wish to copy the code to clipboard? (Y/N)").lower().strip()
        if question == "y":
            pyperclip.copy(result)
            print("Code copied!")
        run = using()

    elif mode == "2":
        if result:
            answer = input("Do you wish to translate your last encoded message for checking?(Y/N)").lower().strip()
            if answer == "y":
                print(f"Your converted morse to text is:\n{translate(result)}")

            elif answer == "n":
                code = input("Input your code:\n").strip()
                print(f"Your converted morse to text is:\n{translate(code)}")

        else:
            code = input("Input your code:\n").strip()
            print(f"Your converted morse to text is:\n{translate(code)}")

        run = using()
    else:
        os.system("cls")
        print("That's not a valid option! Please put options only with numbers 1 or 2!")

print("Goodbye! 👋")