# Written by: SMIDA Houcine L. (2025)
# Woodall (1977) non-lexicographic recursive permutation algorithm.
# Program: generate permutations using the non-lexicographic recursive permutation algorithm.
# The elements of the array must be distinct.

# ======================================================================
# Begin Woodall (1977) non-lexicographic recursive permutation algorithm
# ======================================================================
def PERMALL(A, n):
    # Additional case for n = 1
    # I added this case to handle a single-element array.
    # The original Woodall algorithm begins with the case n = 2.
    if n == 1:
        print(A)  # Display the array
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
        PERMALL(A, n - 1)
        # Determine the position to be exchanged
        if n & 1:  # If n is odd
            swpt = 0
        else:      # If n is even
            swpt = mp
        # Exchange the selected element with the last element
        A[swpt], A[n - 1] = A[n - 1], A[swpt]
    # Generate the final set of permutations
    PERMALL(A, n - 1)
# ====================================================================
# End Woodall (1977) non-lexicographic recursive permutation algorithm
# ====================================================================

# ================================================================
# Display the purpose of the program
# ================================================================
print("Woodall (1977) non-lexicographic recursive permutation")
print("Written by: SMIDA Houcine L. (2025)")

# ================================================================
# Generate and display all the permutations
# ================================================================
# PERMALL() generates and displays all permutations according to
# the Woodall (1977) non-lexicographic recursive algorithm.
Tab = [4, 3, 2, 1]
print("\nNon-lexicographic permutations:")
PERMALL(Tab, len(Tab))
