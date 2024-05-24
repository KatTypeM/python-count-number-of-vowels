
# Python algorithm

# Count the number of vowels within a string


def countVowels(stringInput):
    strArray = list(stringInput.lower())
    vowelCount = 0
    consonantsCount = 0
    for x in strArray:
        if( x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
            vowelCount +=1
        elif(x == " "):
            continue
        else:
            consonantsCount +=1
    return "There are " + str(vowelCount) + " vowels and " + str(consonantsCount) + " consonants in the phrase: \"" + str(stringInput) + "\""


print(countVowels("Count the number of vowels within a string"))
print(countVowels("You can use triple quotes to enclose strings with more than one line"))