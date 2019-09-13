

#Given sorted array of nums 


nums = [1 ,2 ,3 ,3 , 4, 4,4 , 5, 5, ]
# nums = [1,1 ,2]


# Return the length of the new array without the duplicates
length = 0 
prev = None
for i in range(len(nums)): 
	# If we've already seen this number
    if prev == nums[i]:
    	continue

    # If the number is new
    else:
       prev = nums[i]
       nums[length] = nums[i]
       length +=1 

print (length , nums) 
