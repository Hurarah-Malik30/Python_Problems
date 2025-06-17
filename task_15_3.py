def checklongest(long_list):
    longest_word = ''
    for i in long_list:
        if len(i) > len(longest_word):
            longest_word = i

    return longest_word

print(checklongest(['cat', 'car', 'fear', 'center']))

print(checklongest(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']))