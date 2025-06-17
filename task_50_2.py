def swapwords(a):
    text = a.split()
    for i in range(len(text)):
        if "Python" in text[i]:
            n = text[i].index("Python")
            text[i] = text[i][:n] + "Java" + text[i][n+6:]
        elif "Java" in text[i]:
            n = text[i].index("Java")
            text[i] = text[i][:n] + "Python" + text[i][n+4:]
    print(*text)
swapwords('I love Python Not Java')