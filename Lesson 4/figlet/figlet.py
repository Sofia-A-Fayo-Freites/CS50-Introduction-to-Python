import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(f"Output: {figlet.renderText(text)}")

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--":
        if sys.argv[2] in figlet.getFonts():
            f = sys.argv[2]
            figlet.setFont(font=f)
            text = input("Input: ")
            print(f"Output: {figlet.renderText(text)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
