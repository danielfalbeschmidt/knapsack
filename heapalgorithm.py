class HeapAlgorithm:

    item_count = 0
    permutations = []

    def heapPermutation(a, size):
        # if size becomes 1 then prints the obtained
        # permutation
        if size == 1:
            temp = []
            for x in a: # how to actually persist the permutations :)
                temp.append(x)
            HeapAlgorithm.permutations.append(temp)
            return

        for i in range(size):
            HeapAlgorithm.heapPermutation(a, size-1)

            # if size is odd, swap 0th i.e (first)
            # and (size-1)th i.e (last) element
            # else If size is even, swap ith
            # and (size-1)th i.e (last) element
            if size & 1:
                a[0], a[size-1] = a[size-1], a[0]
            else:
                a[i], a[size-1] = a[size-1], a[i]


    def generate():
        a = []

        for i in range(HeapAlgorithm.item_count):
            a.append(i)

        n = len(a)
        HeapAlgorithm.heapPermutation(a, n)


    def getPermutations(item_count):
        HeapAlgorithm.item_count = item_count
        HeapAlgorithm.generate()
        return HeapAlgorithm.permutations


    # This code is contributed by ankush_953
    # This code was cleaned up to by more pythonic by glubs9
    # class created by danielfalbeschmidt
