list_of_elemnts = [1,5,12,2]

def concatenate(elements_list):
    res = ''
    for i in elements_list:
        res = res + str(i)
    return res
print(concatenate(list_of_elemnts))