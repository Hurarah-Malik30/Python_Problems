
def getsepartes(string):
    import re
    list_separated = re.split(r"([ ,]+)", string)      
    return [list_separated[0::2],list_separated[1::2]]

print(getsepartes("W3resource Python, Exercises.")) 