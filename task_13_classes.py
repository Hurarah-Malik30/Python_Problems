from roman import roman

class RomanNumeral:
    def __init__(self,num:int):
        self.num = num

    def Convert(self):
        return roman(self.num)


rn_1 = RomanNumeral(30)
print(rn_1.Convert())