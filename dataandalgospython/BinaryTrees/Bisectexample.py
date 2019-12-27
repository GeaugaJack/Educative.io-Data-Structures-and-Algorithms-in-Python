import bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

print(A)
bisect.insort_left(A, 108)
print(A)

bisect.insort_right(A, 108)
print(A)