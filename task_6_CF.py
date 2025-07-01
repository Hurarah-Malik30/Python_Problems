nums = (1,2,3,4,5,6,7,8,9)
even_count = 0
odd_count = 0
for i in nums:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print("Even Count:",even_count,"Odd Count:",odd_count)