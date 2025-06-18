lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

ans = sum(x*y for x , y in zip(lst1,lst2))
print(ans)