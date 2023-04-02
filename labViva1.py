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

def rabin_karp(text, pattern):
    # Choose a prime number as the base for the hash function
    prime = 31
    
    # Calculate the hash value of the pattern
    p_hash = 0
    for char in pattern:
        p_hash = p_hash * prime + ord(char)
        
    # Create a rolling hash for the text
    s_hash = 0
    for i in range(len(pattern)):
        s_hash = s_hash * prime + ord(text[i])
        
    # Check if the hash values match and compare substrings
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        if s_hash == p_hash and text[i:i+len(pattern)] == pattern:
            matches.append(i)
        if i < len(text) - len(pattern):
            s_hash = s_hash - ord(text[i]) * (prime**(len(pattern)-1))
            s_hash = s_hash * prime + ord(text[i+len(pattern)])
    return matches


if __name__ == "__main__":
    a = [84, 23, 62, 44, 16, 30, 95, 51]
    sorted_arr = counting_sort(a)
    radix_arr = radix_sort(a)
    print(sorted_arr)
    print(radix_arr)
    text = "timecomplexityisfunalgorithmisfun"
    patterns = ["algorithm", "fun"]
    result = rabin_karp(text, patterns)
    print(result)
