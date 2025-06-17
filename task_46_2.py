from datetime import date

inp = input("Input month and date (separated by a single space): ")
m, d = map(int, inp.split())

days = {1: 'Monday', 2: "Tuesday",3:"Wednesday", 4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}

w = date.isoweekday(date(2016,m,d))
print("Day: ",days[w])
