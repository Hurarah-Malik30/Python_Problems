import random
random_list = [[random.randint(0,100) for _ in range(4)]for rows in range(4)]
print(random_list)
def changevalues(random_list_param,threshold):
    new_res = [[threshold if x > threshold else x for x in row]for row in random_list_param]
    return new_res
print(changevalues(random_list,50))