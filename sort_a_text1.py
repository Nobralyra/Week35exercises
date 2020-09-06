# Create a function that takes a string as a parameter and returns a list.
#
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

def remove_all_vowels_and_alphabetic_sort_consonants(stringText):
    vowels = ("aeiou")

    for character in stringText:
        if character.lower() in vowels:
            stringText = stringText.replace(character, '')

    print(sorted(stringText))


remove_all_vowels_and_alphabetic_sort_consonants("This is a test text")

