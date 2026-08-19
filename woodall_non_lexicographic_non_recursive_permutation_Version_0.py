# Written by: SMIDA Houcine L. (2025)
# Woodall (1977) non-lexicographic non-recursive permutation algorithm.
# Program: generate permutations using the Woodall (1977)
# non-lexicographic non-recursive permutation algorithm.
# The elements of the array must be distinct.
# Woodall specifies that A is indexed from right to left.
# Therefore, A[::-1] is used to display the permutations
# in Woodall's left-to-right reading order.

# ======================================================================
# Begin Woodall (1977) non-lexicographic non-recursive permutation algorithm
# ======================================================================
def PERM(A, n):
    # Additional case for n <= 1
    # I added this case to handle an empty or single-element array.
    if n <= 1:
        print(A)
        return
    # Initialize the auxiliary arrays
    M = [0] * (n + 1)
    KM = [0] * (n + 1)
    ret = [0] * (n + 2)
    # Initialize M and KM
    for i in range(4, n + 1, 2):
        M[i - 1] = KM[i - 1] = i - 1
        M[i - 2] = KM[i - 2] = 2 - i
    # Additional initialization when n is odd
    if (n // 2) * 2 != n:
        KM[n - 1] = M[n - 1] = 1 - n
    # Initialize ret
    for i in range(2, n + 1):
        ret[i - 1] = i + 1
    # Initialize p
    p = ret[1]
    # Generate permutations iteratively
    while p <= n:
        if p > 3:
            ret[1] = 3
        # Display the current permutation
        print(A[::-1])
        # Exchange the first two elements
        A[0], A[1] = A[1], A[0]
        # Determine the exchange position
        Mp = M[p - 1]
        if Mp < 0:
            swpt = 1
            Mp += 1
        else:
            swpt = Mp
            Mp -= 1
        # Update M and ret
        if Mp == 0:
            M[p - 1] = KM[p - 1]
            ret[p - 2] = ret[p - 1]
            ret[p - 1] = p + 1
        else:
            M[p - 1] = Mp
        # Display the next permutation
        print(A[::-1])
        # Exchange the selected elements
        A[p - 1], A[swpt - 1] = A[swpt - 1], A[p - 1]
        # Update p
        p = ret[1]
    # Display the final permutation
    print(A[::-1])
    # Final exchange
    A[0], A[1] = A[1], A[0]
    # Display the final permutation
    print(A[::-1])
# ======================================================================
# End Woodall (1977) non-lexicographic non-recursive permutation algorithm
# ======================================================================

# ================================================================
# Display the purpose of the program
# ================================================================
print("Woodall (1977) non-lexicographic non-recursive permutation")

# ================================================================
# Generate and display all the permutations
# ================================================================
# PERM() generates and displays all permutations according to
# the Woodall (1977) non-lexicographic non-recursive algorithm.
Tab = [4, 3, 2, 1]
print("\nNon-lexicographic non-recursive permutations:")
PERM(Tab, len(Tab))