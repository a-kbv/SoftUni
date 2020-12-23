# def permutations(string, step = 0):
#     if step == len(string):
#         # we've gotten to the end, print the permutation
#         print("".join(string))
#     for i in range(step, len(string)):
#         # copy the string (store as array)
#         string_copy = [c for c in string]
#          # swap the current index with the step
#         string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
#          # recurse on the portion of the stringthat has not been swapped yet
#         permutations(string_copy, step + 1)
#
# permutations(input())

# HEAPS ALGORITHM for combinations
permutations = set()

def generate(k: int, A: list):
    if k == 1:
        permutations.add(''.join(A))
    else:
        generate(k - 1, A)

        for i in range(k):
            # Swap choice dependent on parity of k (even or odd)
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]

            generate(k - 1, A)


s = list(input())
generate(len(s), s)
print('\n'.join(list(permutations)))
