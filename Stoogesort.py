def stoogesort(arr, start, end): 
     
    # Checar si hay elementos en el arreglo
    if start >= end: 
        return
     
    # Cheacr primero con el ultimo eleemnto
    if arr[start]>arr[end]: 
        temp = arr[start] 
        arr[start] = arr[end] 
        arr[end] = temp 
     
    # CChecar si el numero de elemntos es mayor a 2
    if end-start+1 > 2: 
        temp = (int)((end-start+1)/3) 
        # Recursivamente llamar a las partes del arreglo para que sean ordenados
        stoogesort(arr, start, (end-temp)) 
        stoogesort(arr, start+temp, (end)) 
        stoogesort(arr, start, (end-temp)) 
 
# Tomar entrada de la lista desordenada
arr = list(map(int,input("Enter all the numbers of array separated by a space: ").split()))
n = len(arr)
           
# Imprime el arreglo desordenado
print("The original unsorted array is: ")
for i in range(0, n): 
    print(arr[i], end = ' ')
 
stoogesort(arr, 0, n-1) 
           
#Imprime el arreglo ordenado
print("\nThe sorted array is: ")
for i in range(0, n): 
    print(arr[i], end = ' ')

#De acuerdo al teorema del Maestro este algoritmo tiene una complejidad de O(n^log3/2(3)) ya que primero "a" tiene una cantidad de llamados recursivos de 3, después n/b es igual a 2/3
#ya que el tamaño de la entrada siempre busca dividirse en 2/3, por lo tanto b=3/2 y finalmente tenemos que O(1) ya que las operaciones son en tiempo constante, por lo tanto c=0
#Finalmente sustituyendo tenemos que O(n^log3/2(3)).
