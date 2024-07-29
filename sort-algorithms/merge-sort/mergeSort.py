def mergeSort(arr: list):
  if len(arr) > 1: 
    middle = int(len(arr) / 2)
    left = arr[:middle]
    right = arr[middle:]
    
    arr1 = mergeSort(left)
    arr2 = mergeSort(right)
    
    arr = merge(arr1, arr2)
    
  return arr

def merge(left: list, right: list):
  resultArray = []
  leftIndex = rightIndex = 0
  
  while leftIndex < len(left) and rightIndex < len(right):
    if left[leftIndex] < right[rightIndex]:
      resultArray.append(left[leftIndex])
      leftIndex += 1
    else:
      resultArray.append(right[rightIndex])
      rightIndex += 1
    
  resultArray.extend(left[leftIndex:])
  resultArray.extend(right[rightIndex:])
  return resultArray


arr = [30,20,34,40,23,50,1,0]
print(mergeSort(arr))