import collections

def getResult(a):
    list_words = list(map(str,a.split()))
    sc = collections.Counter((list_words))
    common_word = sc.most_common()[0][0]

    max_char = ""
    for s in list_words:
        if len(max_char) < len(s):
            max_char = s

    print("\nMost frequent text and the word which has the maximum number of letters.")
    print(common_word, max_char)

getResult("Thank you for your comment and your participation")
