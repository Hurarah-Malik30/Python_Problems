class get2nums:
    def getnums(self,arr,tar):
        lookup = {}
        for i,val in enumerate(arr):
            if tar-val in lookup:
                return(lookup[tar-val],i)
            lookup[val] = i
            
get_1 = get2nums()
print(get_1.getnums([10,20,10,40,50,60,70],50))