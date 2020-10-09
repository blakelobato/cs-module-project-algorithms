'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Check not zeros
    not_zero = [x for x in arr if x != 0]
    z = [0]*(len(arr)-len(not_zero))
    not_zero.extend(z)
    return not_zero


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")