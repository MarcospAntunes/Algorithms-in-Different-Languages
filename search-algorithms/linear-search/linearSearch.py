def linearSearch(arr, elem):
  index = 0
  for item in arr:
    if item == elem:
      return "The element is in the index: {}".format(index)
    index += 1
  return "Not found."


print(linearSearch([1,2,3,4,5,6], 7))