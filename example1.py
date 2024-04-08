from algo import Sort

l = [64, 25, 12, 22, 11]
print(f"Init list: {l}")

Sort.selection_sort(l)
print(f"Selection Sort: {l}")

Sort.bubble_sort(l)
print(f"Bubble Sort: {l}")

Sort.insertion_sort(l)
print(f"Insertion Sort: {l}")
