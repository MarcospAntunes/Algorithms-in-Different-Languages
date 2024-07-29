def bubbleSort(arr):
  for i in range(len(arr)):
    temp = None
    
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp