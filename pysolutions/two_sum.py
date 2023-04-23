def two_sum(nums, target):
    indices = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indices.append(i)
                indices.append(j)
                return indices
num_list = [1, 2, 43, 5, 453, 54, 354, 3, 23, 23, 3, 23, 54, 3]
k = 6
print(two_sum(num_list, k))
