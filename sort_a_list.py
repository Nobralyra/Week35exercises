# 1. Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])

list_with_names = ["Claus", "Ib", "Per"]

# 2. Sort this list by using the sorted() build in function.

sorted_names = sorted(list_with_names)
print(sorted_names)

# 3. Sort the list in reversed order.

sorted_names_reversed = sorted(list_with_names, reverse=True)
print(sorted_names_reversed)

# 4. Sort the list on the length of the name.

sorted_names_length = sorted(list_with_names, key=len)
print(sorted_names_length)

# 5. Sort the list based on the last letter in the name.

def reverse_names(name):
    return name[::-1]


print(sorted(list_with_names, key=reverse_names))

# 6. Sort the list with the names where the letter ‘a’ is in the name first.

def find_a_in_names(name):
    if "a" in name.lower():
        return True

    return False

print(sorted(list_with_names, key=find_a_in_names, reverse=True))
