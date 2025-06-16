import itertools
X = [1 , 2 , 3]
final_list = []

for i in range(1,len(X)+1):
    list_of_perms = [x for x in itertools.permutations(X,i)]
    final_list.append(list_of_perms)

for i in final_list:
    print(i)