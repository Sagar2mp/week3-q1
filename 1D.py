print("--------OPERATIONS ON 1D ARRAY--------")
arr = [2,4,6,8,10,12]
print("Element at index 2:", arr[2])
print("Element at index 5:", arr[5])
print("Last element:", arr[-1])
print("Elements from index 0 to 4:", arr[0:5])
print("First three elements:", arr[:3])
print("Elements from index 2 :", arr[2:])
arr[2] = 14
print("Modified array:", arr)
import numpy as np
npa=np.array(arr)
print("sum of elements : ",np.sum(npa))
print("maximum element in the array : ",np.max(arr))
print("minimum element in the array : ",np.min(arr))
print("average of elements in the array : ",np.mean(arr))
print("standard deviation of elements in the array : ",np.std(arr))
print("after multiplying with 2 with the array elements : ",arr*2)