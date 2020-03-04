# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)): #make new for loop to compair
            if arr[j] < arr[smallest_index]: #see if the current index of j is less then the current index of i
                smallest_index = j #reset the smallest_index to the value of j



        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] 


    print(arr, 'this is the selection sort\n\n')
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    done = True
    while done:
        done = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                done = True
    print(arr, 'this is the bubble sort\n\n')
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    

    return arr