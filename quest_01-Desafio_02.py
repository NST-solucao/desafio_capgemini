# Mediana sem usar biblioteca 

arr = [9,2,1,4,6]
a = len(arr) // 2
arr.sort()
if not len(arr) % 2:
    print((arr[a-1]+arr[a])/2)
print(arr[a])


#  Mediana usando biblioteca 

import statistics # Documentação em https://docs.python.org/pt-br/3/library/statistics.html

arr = [9,2,1,4,6]

print(statistics.median(arr))
