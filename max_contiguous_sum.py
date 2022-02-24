#Kadane's Algo
#Initialize:
#    max_so_far = INT_MIN
#    max_ending_here = 0
#
#Loop for each element of the array
#  (a) max_ending_here = max_ending_here + a[i]
#  (b) if(max_so_far < max_ending_here)
#            max_so_far = max_ending_here
#  (c) if(max_ending_here < 0)
#            max_ending_here = 0
#return max_so_far


def maxSubArray(nums):
    max_value = float('-inf')
    current_max = 0

    for i in range(0, len(nums)):
        current_max = max(current_max+nums[i],nums[i])
        max_value=max(current_max,max_value)
    return max_value


def main():
    array = [-4, 20, -1, 4, -4, -1, -2, 7, -4, 3, -5]
    print(maxSubArray(array))

main()