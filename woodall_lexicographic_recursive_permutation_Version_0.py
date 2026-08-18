# Written by: SMIDA Houcine L. (2025)
# Woodall (1977) lexicographic recursive permutation algorithm.
# Program: generate permutations using the Woodall (1977) lexicographic recursive permutation algorithm.
# The elements of the array must be distinct.

# ================================================================
# Begin Woodall (1977) lexicographic recursive permutation algorithm
# ================================================================
def LEXPERM(A, n):
    # Additional case for n = 1
    # I added this case to handle a single-element array.
    # The original Woodall algorithm begins with the case n = 2.
    if n == 1:
        print(A[::-1])  # Display the array in reverse order
        return
    # Case n = 2
    if n == 2:
        print(A[::-1])  # Display the array in reverse order
        # Exchange the two elements
        A[0], A[1] = A[1], A[0]
        print(A[::-1])  # Display the array in reverse order
        return
    # Generate permutations recursively
    for mp in range(n - 2, -1, -1):  # mp = n - 2, ..., 0
        # Generate permutations of the first n - 1 elements
        LEXPERM(A, n - 1)
        # Calculate hlen
        hlen = (n - 2) // 2
        # Exchange symmetric elements
        for i in range(0, hlen + 1, 1):  # i = 0, ..., hlen
            A[i], A[n - 2 - i] = A[n - 2 - i], A[i]
        # Exchange the element at position mp
        # with the last element of the current part
        A[mp], A[n - 1] = A[n - 1], A[mp]
    # Generate the final set of permutations
    LEXPERM(A, n - 1)
# ================================================================
# End Woodall (1977) lexicographic recursive permutation algorithm
# ================================================================           

# ================================================================
# Display the purpose of the program
# ================================================================
print("Woodall (1977) lexicographic recursive permutation")
print("Written by: SMIDA Houcine L. (2025)")

# ================================================================
# Generate and display all the permutations
# ================================================================
# LEXPERM() generates and displays all permutations according to
# the Woodall (1977) lexicographic recursive algorithm.
Tab = [4, 3, 2, 1] 
print("\nLexicographic permutations:")
LEXPERM(Tab,  len(Tab))
