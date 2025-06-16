import itertools

string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}

def get_combinations(digits):
    if digits == "":
        return []
    result = [""]
    for digit in digits:
        temp = []
        for res in result:
            for char in string_maps[digit]:
                temp.append(res + char)
        result = temp
    return result

digit_string = "47"
print(get_combinations(digit_string))
digit_string = "29"
print(get_combinations(digit_string))