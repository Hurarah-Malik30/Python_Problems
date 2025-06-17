words = {
    'one' : 1,
    'two' : 2,
    'three': 3,
    'four':4,
    'five': 5,
    'six': 6,
    'seven':7,
    'eight':8,
    'nine':9,
    'zero':0
}
num_to_word = {v: k for k, v in words.items()}

def getvalues(list_string_nums):
    list_string_nums = list_string_nums.split()
    res_list = [words[word] for word in list_string_nums] 
    res_list.sort()
    sorted_list = [num_to_word[num] for num in res_list]
    return sorted_list
print(getvalues('six four one two three'))
print(getvalues('six one four three two nine eight'))



