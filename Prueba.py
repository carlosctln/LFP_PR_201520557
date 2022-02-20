def burbuja(B):
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j];
                A[j]=A[j+1];
                A[j+1]=aux;
    for i in A:
        i = i.reverse()

    print(B)
    print()
A = [['"producto 2"', 35.75, 10, 357.5], ['"producto 1"', 50.0, 133, 6650.0], ['"producto 4"', 50.0, 133, 6650.0], ['"producto 3"', 15.0, 170, 2550.0]]
for i in A:
    i = i.reverse()
print(A)

burbuja(A)