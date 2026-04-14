def partition(nums,high,low):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        if nums[i]<=pivot and i<=high-1:
            i=i+1

    while nums[j]>=pivot and j>=low+1:
        j=j-1


    if i<j:
        nums[i],nums[j]=nums[j],nums[i]
    
    nums[low],nums[j]=nums[j],nums[low]


    return j