def innerRanges(nums, l, r):
    if len(nums) == 0:
        if r - l > 1:
            return [str(l) + '->' + str(r)]
        return [str(r - l + 1) ]

    ranges = []
    prev = l - 1
    for i in range(0, len(nums)):

        if i == len(nums):
            curr = r + 1 
        else:
            curr = nums[i]

        if curr - prev >= 2:
            if prev + 1 == curr - 1:
                ranges.append(str(prev + 1))
            else:
                ranges.append(str(prev + 1) + '->' + str(curr - 1))
        prev = curr
        
    if r - max(nums) == 1:
        ranges.append(str(r))
    elif r - max(nums) > 0:
        ranges.append(str(nums[len(nums)-1] + 1) + '->' + str(r))
        
    return ranges
    
l = int(raw_input().strip())
r = int(raw_input().strip())
nums = map(int, raw_input().strip().split(' '))

print innerRanges(nums, l, r)

