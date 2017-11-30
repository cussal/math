# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)

#brute force:
def b_find_pairs(arr):
    pairs = [] # keeps track of values
    for i in range(len(arr)):
        to_find = 10 - arr[i]
        for j in range(i+1,len(arr)):
            if (arr[j] == to_find):
                pairs.append((arr[i],arr[j]))
    return(pairs)

#optimized
def find_pairs(arr):
    visited = {} # keeps track of previously visited values
    pairs = [] # keeps track of values (should I be doing indices here?
    for i in range(len(arr)):
        needed = 10-arr[i]
        if(needed in visited):
            pairs.append((i,visited[needed]))
        elif(arr[i] not in visited):
            visited[arr[i]] = [i]
    return pairs
