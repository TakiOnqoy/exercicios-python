#Giraffe language
#vowels -> g

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Write here your word to be translated into Giraffe Language: ")))
