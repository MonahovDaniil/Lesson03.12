def find_min(numbers):
  if not numbers:
    return None
  else:
    return min(numbers)
  numbers = [float(x) for x in input_str.split()]
  min_value = find_min(numbers)
  if min_value is None:
    print("The list is empty.")
  else:
    print("The minimum value is:", min_value)

