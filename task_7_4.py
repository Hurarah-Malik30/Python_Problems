lst_3 = list(range(1,11))

replaced_list = [-x  if x%2==0 else x for x in lst_3]
        
print(replaced_list)