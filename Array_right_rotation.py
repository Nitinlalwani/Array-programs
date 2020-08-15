#This program is to rotate the array value in the right index.

def Reverse(arr): 
    return [ele for ele in reversed(arr)] 

def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
  
# Function to left Rotate arr[] of size n by 1*/  
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 
          
  
# utility function to print an array */ 
def printArray(arr, size): 
    for i in range(size): 
        print (arr[i])

# Driver program to test above functions */ 
arr = [1, 2, 3, 4, 5, 6, 7] 

arr = Reverse(arr)
leftRotate(arr, 2, 7) 
arr = Reverse(arr)
printArray(arr, 7)
