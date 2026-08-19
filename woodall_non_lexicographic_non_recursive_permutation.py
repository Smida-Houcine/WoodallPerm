"""
Written by: SMIDA Houcine L. (2025)

Woodall (1977) non-lexicographic non-recursive permutation algorithm.

Program: generate permutations using the Woodall (1977)
non-lexicographic non-recursive permutation algorithm.

Additional case for n <= 1:
I added this case to handle an empty or single-element array.

The elements of the array must be distinct.

The elements can be integers, characters, words, or sentences.

If sentences are to be treated as individual elements,
they must be enclosed in double quotes (" ").

Examples:
    1 2 3 4
    A B C D
    Blue Green Red Yellow
    "Drink more water" "Get regular exercise" "Sleep better"

Woodall specifies that A is indexed from right to left.
Therefore, A[::-1] is used to display the permutations
in Woodall's left-to-right reading order.
"""

# ================================================================
# Display the purpose of the program
# ================================================================
print("Woodall (1977) non-lexicographic non-recursive permutation")
print("Written by: SMIDA Houcine L. (2025)")
print()

# ================================================================
# Begin Woodall (1977) non-lexicographic non-recursive permutation
# algorithm
# ================================================================
def PERM(A, n):
    # Additional case for n <= 1
    # I added this case to handle an empty or single-element array.
    if n <= 1:
        print(*A[::-1], sep=", ")
        return
    # Initialize the auxiliary arrays.
    M = [0] * (n + 1)
    KM = [0] * (n + 1)
    ret = [0] * (n + 2)
    # Initialize M and KM.
    for i in range(4, n + 1, 2):
        M[i - 1] = KM[i - 1] = i - 1
        M[i - 2] = KM[i - 2] = 2 - i
    # Additional initialization when n is odd.
    if (n // 2) * 2 != n:
        KM[n - 1] = M[n - 1] = 1 - n
    # Initialize ret.
    for i in range(2, n + 1):
        ret[i - 1] = i + 1
    # Initialize p.
    p = ret[1]
    # Generate permutations iteratively.
    while p <= n:
        # Update ret[1] when p > 3.
        if p > 3:
            ret[1] = 3
        # Display the current permutation.
        # A is indexed from right to left in Woodall's algorithm.
        print(*A[::-1], sep=", ")
        # Exchange the first two elements.
        A[0], A[1] = A[1], A[0]
        # Determine the exchange position.
        Mp = M[p - 1]
        if Mp < 0:
            swpt = 1
            Mp = Mp + 1
        else:
            swpt = Mp
            Mp = Mp - 1
        # Update M and ret.
        if Mp == 0:
            M[p - 1] = KM[p - 1]
            ret[p - 2] = ret[p - 1]
            ret[p - 1] = p + 1
        else:
            M[p - 1] = Mp
        # Display the next permutation.
        print(*A[::-1], sep=", ")
        # Exchange the selected elements.
        A[p - 1], A[swpt - 1] = A[swpt - 1], A[p - 1]
        # Update p.
        p = ret[1]
    # Display the final permutation.
    print(*A[::-1], sep=", ")
    # Final exchange.
    A[0], A[1] = A[1], A[0]
    # Display the final permutation.
    print(*A[::-1], sep=", ")
# ======================================================================
# End Woodall (1977) non-lexicographic non-recursive permutation
# algorithm
# ======================================================================

# ================================================================
# Read the elements entered by the user
# ================================================================
def read_elements(input_text):
    parsed_elements = []
    current = ""
    quoted = False
    # Spaces separate the elements.
    # Spaces inside " " are part of the current element.
    # The double quotes " " themselves are not part of the element.
    for character in input_text:
        # A double quote " marks the beginning or the end
        # of an element containing spaces.
        if character == '"':
            quoted = not quoted
        # A space separates elements only when it is outside " ".
        elif character.isspace() and quoted == False:
            if current:
                parsed_elements.append(current)
                current = ""
        # All other characters are added to the current element.
        else:
            current = current + character
    # Check for an unclosed pair of double quotes.
    if quoted == True:
        print("\nError: invalid double quotes.")
        exit()
    # Add the last element.
    if current:
        parsed_elements.append(current)
    return parsed_elements

# ================================================================
# Ask the user to enter the elements of the array
# ================================================================
# Spaces separate the elements.
# Spaces inside double quotes (" ") do not separate the elements.
# Double quotes (" ") are used only as delimiters.
values = input(
    "Enter the elements separated by spaces "
    '(use double quotes for sentences): '
)

# ================================================================
# Check the input
# ================================================================
# Check if the input contains at least one element.
if len(values.strip()) == 0:
    print("\nError: the array must contain at least one element.")
    exit()
# Read the elements entered by the user.
elements = read_elements(values)
# Count the number of elements.
number_of_elements = len(elements)

# ================================================================
# Check that the elements are distinct
# ================================================================
# set(elements) contains only distinct elements.
# If its length differs from the original number of elements,
# at least two elements are identical.
if len(set(elements)) != number_of_elements:
    print("\nError: all elements must be distinct.")
    exit()

# ================================================================
# Check whether all elements are integers before sorting
# ================================================================
# This check is used to distinguish numerical input from
# non-numerical input.
all_integers = True
# Check each element by trying to convert it to an integer.
for element in elements:
    try:
        int(element)
    except ValueError:
        # The element is not an integer.
        all_integers = False
        break

# ================================================================
# Create the permutation array
# ================================================================
# Use the parsed elements as the permutation array.
Tab = elements

# ================================================================
# Display the input array before sorting
# ================================================================
# If all elements are integers, display them as integers.
if all_integers:
    print(
        "\nInput array:",
        [int(element) for element in Tab],
    )
# Otherwise, display the elements as strings.
else:
    print(f"\nInput array: {Tab}")

# ================================================================
# Sort the elements according to their ordering
# ================================================================
# The Woodall non-lexicographic algorithm does not generate
# permutations in lexicographic order.
# The initial array is arranged in decreasing order because
# Woodall's array A is indexed from right to left.
try:
    if all_integers:
        # For integers, key=int ensures numerical ordering.
        Tab.sort(
            key=int,
            reverse=True,
        )
    else:
        # For non-integer elements, use their lexicographic order.
        Tab.sort(reverse=True)
except (TypeError, ValueError):
    print(
        "\nError: the elements must be comparable "
        "to determine their order."
    )
    exit()

# ================================================================
# Display the number of elements
# ================================================================
# Display the total number of elements in the array.
print(f"\nNumber of elements: n = {number_of_elements}")

# ================================================================
# Calculate and display the number of permutations
# ================================================================
# Calculate n! by multiplying all integers from 1 to n.
number_of_permutations = 1
for factor in range(1, number_of_elements + 1):
    number_of_permutations = number_of_permutations * factor
# Display the total number of permutations.
# The number of permutations is equal to n!.
print(
    f"Number of permutations: "
    f"{number_of_elements}! = {number_of_permutations}"
)

# ================================================================
# Generate and display all the permutations
# ================================================================
# PERM() generates and displays all permutations according to
# the Woodall (1977) non-lexicographic non-recursive algorithm.
print("\nNon-lexicographic non-recursive permutations:")
PERM(Tab, number_of_elements)