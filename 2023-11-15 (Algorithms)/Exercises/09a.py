def mirror_insertion_sort(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key


a = [5, 2, 4, 6, 1, 3]
mirror_insertion_sort(a)
print(a)
