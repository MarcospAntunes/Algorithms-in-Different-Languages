function binarySearch(itens, left, right, elem, middle = null) {
  if (middle == null) middle = Math.floor((left + right) / 2);

  current = itens[middle];

  if(left > right) {
    return "Element not found.";
  }

  if(current == elem) {
    return `The searched item was found in the index: ${middle}.`;
  } else if(current < elem) {
    left = middle + 1;
    return binarySearch(itens, left, right, elem, middle=Math.floor((left + right) / 2));
  } else if(current > elem) {
    right = middle - 1;
    return binarySearch(itens, left, right, elem, middle=Math.floor((left + right) / 2));
  }

  return
}


const array1 = [1,2,3,4,5,6,7,8,10]
const array2 = ["a","b","c","d","e","f","g","h","i"]

console.log(binarySearch(array1, 0, array1.length - 1, 5))
console.log(binarySearch(array2, 0, array2.length - 1, "a"))
console.log(binarySearch(array2, 0, array2.length - 1, "f"))