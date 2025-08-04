import numpy as np

# same data type values
a = [1, 2, 3, 4, 5, 6]
np_a = np.array(a)

print("values: ", np_a)  # values:  [1 2 3 4 5 6]
print("type: ", type(np_a))  # type:  <class 'numpy.ndarray'>

# mixed data type values
b = [11, 22, "33", 44, "55"]
np_b = np.array(b)

print("values: ", np_b)  # values:  ['11' '22' '33' '44' '55']
print("type: ", type(np_b))  # type:  <class 'numpy.ndarray'>
