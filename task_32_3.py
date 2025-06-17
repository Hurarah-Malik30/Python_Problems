def scaleNums(list_scale):
    max_num = max(list_scale)
    min_num = min(list_scale)
    for i in range(len(list_scale)):
        list_scale[i] = (list_scale[i] - min_num)/(max_num-min_num)
    return list_scale

print(scaleNums([18.5, 17.0, 18.0, 19.0, 18.0]))
print(scaleNums([13.0, 17.0, 17.0, 15.5, 2.94]))