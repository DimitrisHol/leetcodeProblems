


input1 = [2 , 7, 11, 15]
input2 = [3 , 2, 4]
target = 9
target2 = 6


def twoSum( nums , target) : 

    h= dict()

    for i, num in enumerate(nums):
    
        print ( h) 
        n = target - num
        if n not in h:
            h[num] = 1
        else : 

            return [h[n] , i]


x = twoSum(input2 , target2)

print( x)
