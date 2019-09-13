

#Given sorted array of nums 


nums = [1 ,2 ,3 ,3,3,3 , 4, 4,4 , 5, 5,5,5,5,5,6,7,7 ]
# nums = [1,1 ,2]
# nums = [1, 1, 1, 2, 2 ,3]


# Return the length of the new array with duplicates appearing at most twice.
length = 0 
prev = None
seenTwice = 0 

for i in range(len(nums)):

	# If we've already seen this number
    if prev == nums[i]:
    	# If we've seen it twice, we can skip it 
    	if seenTwice == 2 :
    		continue
    	# We've seen it only once
    	else :
    		# Twice = 2
    		seenTwice +=1
    		# Add it to the final list
    		nums[length] = nums[i]
    		length +=1 

    # If the number is new
    else:

    	prev = nums[i]
    	nums[length] = nums[i]
    	length +=1 
    	seenTwice = 1




print (length , nums) 

print(nums[:length])
