#this program is to showcase the left rotation of array by 2 index.

def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
   
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 
          
  
def printTheArray(arr, arrsize): 
    for i in range(arrsize): 
        print (arr[i])

arr = [1, 2, 3, 4, 5, 6, 7] 

leftRotate(arr, 2, 7) 
printTheArray(arr, 7)
