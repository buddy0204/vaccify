def intersect_sorted_arrays(arr1, arr2):
    # Initialize pointers for both arrays
    i, j, comparisons = 0, 0, 0
    intersection = []

    # Loop until either array ends
    while i < len(arr1) and j < len(arr2):
        # Increment comparison counter
        comparisons += 1
        
        # If the current elements are equal, add to the result and move both pointers
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        # If the element in arr1 is smaller, move the pointer in arr1
        elif arr1[i] < arr2[j]:
            i += 1
        # If the element in arr2 is smaller, move the pointer in arr2
        else:
            j += 1

    return intersection, comparisons

# Function to take sorted array input
def input_sorted_array():
    return list(map(int, input("Enter sorted numbers separated by space: ").strip().split()))

# Taking input from the user
print("Input for the first sorted array")
arr1 = input_sorted_array()
print("Input for the second sorted array")
arr2 = input_sorted_array()

intersection, comparisons = intersect_sorted_arrays(arr1, arr2)

print("Intersection:", intersection)
print("Total comparisons:", comparisons)
