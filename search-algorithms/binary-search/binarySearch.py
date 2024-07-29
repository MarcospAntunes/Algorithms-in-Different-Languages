from operator import concat

def binarySearch(itens: list, left, right, elem, middle = None):
  if middle == None:
    middle = (left + right) / 2
  
  current = itens[int(middle)]

  if left > right:
    return "Element not found."

  if current == elem:
    return concat("The searched item was found in the index: ", str(int(middle)))
  elif current < elem:
    left = middle + 1
    return binarySearch(itens, left, right, elem, middle=(left + right) / 2)
  elif current > elem:
    right = middle - 1
    return binarySearch(itens, left, right, elem, middle=(left  + right) / 2)
    
  return


array1 = [1,2,3,4,5,6,7,8,10]
array2 = ["a","b","c","d","e","f","g","h","i"]

print(binarySearch(array1, 0, len(array1) - 1, 5))
print(binarySearch(array2, 0, len(array2) - 1, "a"))
print(binarySearch(array2, 0, len(array2) - 1, "f"))