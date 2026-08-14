import numpy as np

np.random.seed(42)

A = np.random.randint(1, 101, 100)

print(A)

print("Minimum:",np.min(A))
print("Maximum:",np.max(A))
print("Mean:",np.mean(A))
print("Median:",np.median(A))
print("Standard Deviation:",np.std(A))

B = np.arange(100)
print(B)
#print("Number of elements in B:",B.size)

zeros_array = np.zeros(5)
ones_array = np.ones(5)

print("Zeros array:",zeros_array)
print("Zeros shape:",zeros_array.shape)
print("Zeros data type:",zeros_array.dtype)

print("Ones array:",ones_array)
print("Ones shape:",ones_array.shape)
print("Ones data type:",ones_array.dtype)

C = np.linspace(0,10,11)
print("Array C:",C)

array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(array_2d)   
print(array_2d.shape)
print("2D array dimensions:",array_2d.ndim)
print("2D array first element:",array_2d[0,0])

array_3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(array_3d)
print(array_3d.shape)
print("3D array dimensions:",array_3d.ndim)
print("3D array first element:",array_3d[0,0,0])