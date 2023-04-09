from tries import Trie

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

def rabin_karp_hash(s, a=101, q=10**9+9):
    n = len(s)
    h = 0
    for i in range(n):
        h = (h * a + ord(s[i])) % q
    return h

def rabin_karp(text, pattern, a=101, q=10**9+9):
    n = len(text)
    m = len(pattern)
    pattern_hash = rabin_karp_hash(pattern, a, q)
    text_hash = rabin_karp_hash(text[:m], a, q)
    for i in range(n - m + 1):
        if text_hash == pattern_hash:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * pow(a, m-1, q)) % q
            text_hash = (text_hash * a + ord(text[i+m])) % q
    return -1

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    
    # Build the prefix function
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j-1]
        if pattern[j] == pattern[i]:
            j += 1
        prefix[i] = j
    
    # Use the prefix function to search for the pattern in the text
    j = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = prefix[j-1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

def finite_automata(text, pattern):
    n = len(text)
    m = len(pattern)
    
    # Build the transition function for the pattern
    transitions = {0: {pattern[0]: 1}, 1: {}}
    j = 0
    for i in range(1, m):
        for c in set(pattern[:i+1]):
            if c not in transitions[i]:
                if pattern[:i] + c in pattern[:i+1]:
                    transitions[i][c] = i + 1
                else:
                    transitions[i][c] = 0
        j = transitions[j].get(pattern[i], 0)
        transitions[i+1] = {}
    
    # Use the transition function to search for the pattern in the text
    j = 0
    for i in range(n):
        j = transitions[j].get(text[i], 0)
        if j == m:
            return i - m + 1
    return -1


if __name__ == "__main__":
    a = [84, 23, 62, 44, 16, 30, 95, 51]
    sorted_arr = counting_sort(a)
    radix_arr = radix_sort(a)
    print("running counting sort:")
    print(sorted_arr)
    print("running radix sort:")
    print(radix_arr)
    text = "timecomplexityisfunalgorithmisfun"
    pattern = "fun"
    index = rabin_karp(text, pattern)
    print("running rabin karp algorithm:")
    if index == -1:
        print("Pattern not found")
    else:
        print("Pattern found at index", index)
    index = kmp(text, pattern)
    print("running kmp algorithm:")
    if index == -1:
        print("Pattern not found")
    else:
        print("Pattern found at index", index)
    index = finite_automata(text, pattern)
    print("running finite automata algorithm:")
    if index == -1:
        print("Pattern not found")
    else:
        print("Pattern found at index", index)
    trie = Trie()
    trie.insert(text)
    print("running trie algorithm:")
    matches = trie.search(pattern)
    print(matches)

