# 1. Based on this list of tuples: [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

list_of_tuples = [(1, 2), (2, 2), (3, 2), (2, 1), (2, 2), (1, 5), (10, 4), (10, 1), (3, 1)]

# 2. Sort the list so the result looks like this: [(1, 2), (1, 5), (2, 1), (2, 2), (2, 2), (3, 1), (3, 2), (10, 1), (10, 4)]

sorted_tuples_after_first_number = sorted(list_of_tuples)
print(sorted_tuples_after_first_number)
