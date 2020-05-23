def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            translation += "g"
        elif letter in "AEIOU":
            translation += "G"
        else:
            translation += letter
    return translation

exit = False
while not(exit):
    print("Enter a phrase to translate...")
    phrase = input("Enter nothing to shut down: ")
    if phrase == "":
        exit = True
        continue
    print(translate(phrase))

print("Shutting down...")
