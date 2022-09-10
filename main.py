import os
import pyperclip
from convert import Convert
from translate import Translate

# Morse code translator
print("Welcome to the Morse Code translator! 📄\n")


# Keep using program
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


cv = Convert()
ts = Translate()

result = False
run = True

while run:

    mode = input("Which mode you want to use?\n1 Text insert\n2 Morse Code translation\n").strip()

    if mode == "1":
        text = input("Input your text:\n").lower().strip()
        result = cv.convert(text)
        print(f"Your converted text to morse is:\n\n{result}")
        question = input("Do you wish to copy the code to clipboard? (Y/N)\n").lower().strip()
        if question == "y":
            pyperclip.copy(result)
            print("Code copied!")

    elif mode == "2":
        if result:
            answer = input("Do you wish to translate your last encoded message for checking?(Y/N)\n").lower().strip()
            if answer == "y":
                print(f"Your converted morse to text is:\n{ts.translate(result)}")

            elif answer == "n":
                code = input("Input your code:\n").strip()
                print(f"Your converted morse to text is:\n{ts.translate(code)}")

        else:
            code = input("Input your code:\n").strip()
            print(f"Your converted morse to text is:\n{ts.translate(code)}")

    else:
        os.system("cls")
        print("That's not a valid option! Please put options only with numbers 1 or 2!")

    run = using()

print("Goodbye! 👋")