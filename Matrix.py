def Print_matrix(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()


def Print_upper_triangle(mat):
    n=len(mat)
    for i in range(0,n):
        for j in range(0,n):
            if i>j:
                print("*",end=" ")    
            else:
                print(mat[i][j],end=" ")
        print()        


def Print_lower_triangle(mat):
    n=len(mat)
    for i in range(0,n):
        for j in range(0,n):
            if i<j:
                print("*",end=" ")
            else:
                print(mat[i][j],end=" ")
        print()



def get_transpose(mat):
    row=len(mat)
    col=len(mat[0])
    trans=[[0]*row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            trans[j][i]=mat[i][j]

    return trans



met=[[1,2,3],[4,5,6],[7,8,9]]
Print_matrix(met)      
print("Upper triangle of matrix is:")
Print_upper_triangle(met)  
print("Lower triangle of matrix is:")
Print_lower_triangle(met)
print("Transpose of matrix is:")
transposed=get_transpose(met)
Print_matrix(transposed)



        rotated=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(m):
                rotated[j][(n-1)-i]=matrix[i][j]

        for i in range(n):
            for j in range(m):
                matrix[i][j]=rotated[i][j]