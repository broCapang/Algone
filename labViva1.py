def counting_sort(arr):
    # Find the range of values in the array
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Initialize count array with all zeros
    count = [0] * range_val
    
    # Count the frequency of each element in the array
    for val in arr:
        count[val - min_val] += 1
        
    # Calculate cumulative sum of the count array
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
    # Create the sorted array
    sorted_arr = [0] * len(arr)
    for val in arr:
        sorted_arr[count[val - min_val] - 1] = val
        count[val - min_val] -= 1
        
    return sorted_arr

def radix_sort(arr):
    # Find the maximum number of digits in the array
    max_digits = len(str(max(arr)))
    
    # Sort the array by each digit, from LSD to MSD
    for i in range(max_digits):
        buckets = [[] for _ in range(10)]
        for val in arr:
            digit = (val // 10**i) % 10
            buckets[digit].append(val)
        arr = [val for bucket in buckets for val in bucket]
        
    return arr


if __name__ == "__main__":
    a = [84, 23, 62, 44, 16, 30, 95, 51]
    sorted_arr = counting_sort(a)
    radix_arr = radix_sort(a)
    print(sorted_arr)
    print(radix_arr)