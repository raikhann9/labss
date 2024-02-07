#Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    for i in range(0, n-2):
        if int(nums[i])==0 and int(nums[i+1])==0 and int(nums[i+2])==7:
            return True
    return False

nums=input().split()
n=len(nums)
print(spy_game(nums))