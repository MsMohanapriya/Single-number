def SingleNumber(array):
    result=0
    for i in range(len(array)):
        result=result^array[i]
    return result
array=list(map(int,input("enter the array: ").split()))
print(SingleNumber(array))