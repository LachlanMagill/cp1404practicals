colour_to_code = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff",
                  "ALIZARIN CRIMSON": "#e32636", "AMARANTH": "#e52b50", "AMBER": "#ffbf00", "AMETHYST": "#9966cc",
                  "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1": "#ffefdb", "ANTIQUEWHITE2": "#eedfcc",
                  "ANTIQUEWHITE3": "#cdc0b0"
                  }

print(colour_to_code)

colour = input("Enter colour name: ").upper()
while colour != "":
    if colour in colour_to_code:
        print("The code for ", colour, "is", colour_to_code[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").upper()
