"""
Written by: SMIDA Houcine L. (2025)

Woodall (1977) non-lexicographic recursive permutation algorithm.

Program: generate permutations using the Woodall (1977)
non-lexicographic recursive permutation algorithm.

Additional case for n = 1:
I added this case to handle a single-element array.
The original Woodall algorithm begins with the case n = 2.

The elements of the array must be distinct.

The elements can be integers, characters, words, or sentences.

If sentences are to be treated as individual elements,
they must be enclosed in double quotes (" ").

Examples:
    1 2 3 4
    A B C D
    Blue Green Red Yellow
    "Drink more water" "Get regular exercise" "Sleep better"
"""

# ================================================================
# Display the purpose of the program
# ================================================================
print("Woodall (1977) non-lexicographic recursive permutation")
print("Written by: SMIDA Houcine L. (2025)")
print()

# ================================================================
# Begin Woodall (1977) non-lexicographic recursive permutation 
# algorithm
# ================================================================
def PERMALL(A, n):
    # Additional case for n = 1
    # I added this case to handle a single-element array.
    # The original Woodall algorithm begins with the case n = 2.
    if n == 1:
        print(*A[::-1], sep=", ")  # Display the array in reverse order
        return
    # Case n = 2
    if n == 2:
        print(*A[::-1], sep=", ")  # Display the array in reverse order
        # Exchange the two elements
        A[0], A[1] = A[1], A[0]
        print(*A[::-1], sep=", ")  # Display the array in reverse order
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
# ================================================================
# End Woodall (1977) non-lexicographic recursive permutation
# algorithm
# ================================================================

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
# This check is used only to display and initially order
# numerical input consistently.
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
#
# The initial array is nevertheless arranged in decreasing order,
# consistently with the implementation used here.
try:
    if all_integers:
        # For integers, key=int ensures numerical ordering.
        Tab.sort(
            key=int,
            reverse=True,
        )
    else:
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
# PERMALL() generates and displays all permutations according to
# the Woodall (1977) non-lexicographic recursive algorithm.
print("\nNon-lexicographic permutations:")
PERMALL(Tab, number_of_elements)