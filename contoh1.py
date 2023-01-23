#contoh program rekursif nilai maksimal
def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        m = find_max(arr[1:])
        return m if m > arr[0] else arr[0]

print(find_max([1, 3, 5, 2, 8, 10])) # hasilnya akan mencetak 10

#contoh program rekrusif nilai rata rata 
def find_average(arr, len_arr=0, total=0):
    if len(arr) == 0:
        return total/len_arr
    else:
        return find_average(arr[1:], len_arr+1, total+arr[0])
    
print(find_average([1,3,5,7])) # hasilnya akan mencetak 4.5
