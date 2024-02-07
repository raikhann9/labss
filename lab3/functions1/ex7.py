#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, n-1):
        if int(nums[i])==3 and int(nums[i+1])==3:
            return True
    return False

nums=input().split()
n=len(nums)
print(has_33(nums))
