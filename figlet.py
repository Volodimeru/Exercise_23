import sys
from random import choice
from pyfiglet import Figlet
figlet = Figlet()
figlet.getFonts()
if len(sys.argv) == 1:
    figlet.setFont(font=choice(figlet.getFonts()))
    c = input("Input: ")
    print(figlet.renderText(c))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") :
    figlet.setFont(font=sys.argv[2])
    c = input("Input: ")
    print(figlet.renderText(c))
else:
    print("Invalid usage")
    sys.exit()