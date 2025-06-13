def intvalidator(a,b):
    if ((type(a) == int) and (type(b) == int)):
        return a+b
    else:
        return ("NOT AN INTEGER...")

print(intvalidator(2,10))
print(intvalidator(2.10,10))