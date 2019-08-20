import numpy as np

def parent(i):
    return int((i-1)/2)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * (i + 1)


def max_heapify(A, i):
    l = left(i)
    r = right(i)

    if l + 1 <= A_heapsize and A[l] > A[i]:
        largest = l

    else:
        largest = i

    if r + 1 <= A_heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        temp_2 = A[i]
        A[i] = A[largest]
        A[largest] = temp_2

        max_heapify(A, largest)


def build_max_heap(A):
    for i in reversed(range(int(len(A)/2))):
        max_heapify(A, i)


if __name__ == '__main__':
    A_size = 16
    A = list(np.random.randint(-100, 100, size=A_size))
    print('Unsorted list:', A)

    A_heapsize = len(A)

    build_max_heap(A)

    for i in reversed(range(1, len(A))):
        temp_1 = A[0]
        A[0] = A[i]
        A[i] = temp_1

        A_heapsize -= 1

        max_heapify(A, 0)

    print('Sorted list:', A)