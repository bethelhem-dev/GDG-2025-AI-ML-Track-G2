#Create a list of 5 numbers in Python.

#Convert this list into a NumPy array.

#Using NumPy, calculate:

#The mean of the numbers

#The maximum value

#The sum of the numbers

#Print all the results clearly. 

import numpy as np

numbers = [10, 20, 30, 40, 50]
array = np.array(numbers)

mean_value = np.mean(array)
max_value = np.max(array)
sum_value = np.sum(array)

print("NumPy Array:", array)
print("Mean:", mean_value)
print("Maximum Value:", max_value)
print("Sum:", sum_value)
