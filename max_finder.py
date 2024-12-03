def find_max(numbers):
  if not numbers:
    return None
  else:
    return max(numbers)
  numbers = [float(x) for x in input_str.split()]
  max_value = find_max(numbers)
  if max_value is None:
    print("The list is empty.")
  else:
    print("The maximum value is:", max_value)

