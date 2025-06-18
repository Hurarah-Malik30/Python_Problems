list_unique = [1, 2, 3, 2, 4, 1, 5, 4, 6]

unique_elems = list(set(list_unique))

counts = {x:list_unique.count(x) for x in unique_elems}

print(counts)