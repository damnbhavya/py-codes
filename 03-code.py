import numpy as np

def array_to_machine_values(arr):
    machine_values = np.array(arr)
    return machine_values

def machine_values_to_array(machine_values):
    return machine_values.tolist()

arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

machine_values = array_to_machine_values(arr)
print("Array of machine values:", machine_values)

converted_array = machine_values_to_array(machine_values)
print("Converted back to array:", converted_array)


