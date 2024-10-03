def nextPermutation( nums):
        n = len(nums)
        pointer = -1
        for i in range(n-2, -1,-1):
             if nums[i] < nums[i+1]:
                  pointer = i
                  break
        
        if pointer == -1:
            nums.reverse()
            return nums
        for j in range(n-1,pointer,-1):
            if nums[pointer] < nums[j]:
                nums[pointer],nums[j] = nums[j],nums[pointer]
                break
        nums[pointer+1:] = reversed(nums[pointer+1:])
        

    #Converting list into the array
        a = 0
        for k in range(n):
            a = a*10 + nums[k]
        print(a)

ar = "321"
ar= list(map(int,ar))
print(nextPermutation(ar))
