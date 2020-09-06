def remove_all_vowels_and_alphabetic_sort_consonants (stringText):
    vowels = ["a", "e", "i", "o", "u"]
    endResult = []
    for i in stringText:
        if i.lower() not in vowels:
            endResult += i

    print(sorted(endResult))


remove_all_vowels_and_alphabetic_sort_consonants("This is a test text")