# Written by: SMIDA Houcine L. (2025)
# Woodall (1977) non-lexicographic recursive permutation algorithm.
# Program: generate permutations using the non-lexicographic recursive permutation algorithm.
# The elements of the array must be distinct.

# ================================================================
# Begin Woodall (1977) non-lexicographic recursive permutation algorithm
# ================================================================
def PERMALL(A, n):
    if n == 2:
        print(A[::-1])
        A[0], A[1] = A[1], A[0]
        print(A[::-1])
        return

    for mp in range(n - 2, -1, -1):
        PERMALL(A, n - 1)

        if n & 1:
            swpt = 0
        else:
            swpt = mp

        A[swpt], A[n - 1] = A[n - 1], A[swpt]

    PERMALL(A, n - 1)

# ================================================================
# End Woodall (1977) non-lexicographic recursive permutation algorithm
# ================================================================


# ================================================================
# Display the purpose of the program
# ================================================================
print("Woodall (1977) non-lexicographic recursive permutation")
print("Written by: SMIDA Houcine L. (2025)")


# ================================================================
# Generate and display all the permutations
# ================================================================
Tab = [4, 3, 2, 1]

print("\nNon-lexicographic permutations:")
PERMALL(Tab, len(Tab))