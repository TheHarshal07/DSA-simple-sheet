def nextPermutation( nums):
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 2:
            return nums.reverse()
        pointer = n - 2

        while pointer >= 0 and nums[pointer] >= nums[pointer+1]:
            pointer -= 1
        
        if pointer == -1:
            return nums.reverse()
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

ar = "132465"
ar= list(map(int,ar))
nextPermutation(ar)
