class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #return the list of number - this is correct
        list_of_nums = []
        zero_count = 0
        sum = 1

        # rather than multiply each number by itself divide by number
        # could have 0 count

        for i in nums:
            if i == 0:
                zero_count +=1
        #print("Zero count: " + str(zero_count))

        if zero_count > 1:
            for i in nums:
                list_of_nums.append(0)
        elif zero_count == 1:
            position = nums.index(0)
            #print("0 is located at " + str(position))
            for k in nums:
                if k != 0:
                    sum *= k
            for l in nums:
                list_of_nums.append(0)
            list_of_nums[position] = sum
        else:
            for i in nums:
                sum*=i
            for m in nums:
                list_of_nums.append(int(sum / m))
                
        
    
        return list_of_nums