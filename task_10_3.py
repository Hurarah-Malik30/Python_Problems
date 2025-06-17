def separtedbreckets(s):
    holder = []
    s1 = ""
    for i in s.replace(' ',''):
        s1+=i
        if s1.count("(") == s1.count(")"):
            holder.append(s1)
            s1 = ""
    return holder
print(separtedbreckets("( ()) ((()()())) (()) ()"))