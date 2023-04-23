def twoSum(nums,target):
        indices = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    indices.append(i)
                    indices.append(j)
                    return indices
list=[1,2,43,5,453,54,354,3,23,23,3,23,54,3]
sum=6
print(twoSum(list,sum))