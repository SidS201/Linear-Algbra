import numpy as np #apparently this is needed. also won't affect memory as numpy imported in the other file is used here too


def row_sort(matrix): #to sort the rows of the matrix by the number of leading zeroes
    row_zeroes= np.zeros(matrix.shape[0], dtype=int)
    for i in range(len(row_zeroes)):
        for j in matrix[i,:]:
            if j == 0:
                row_zeroes[i] += 1
            else:
                break
    sort_order=row_zeroes.argsort() #so argsort returns the indices that would sort the array
    matrix = matrix[sort_order] 

    opp= np.zeros(matrix.shape) #storing the row operation in a matrix
    for i in range(len(sort_order)):
        opp[i,sort_order[i]] = 1
    inv_opp=opp #the inverse is the same cuz we're flipping the same row numbers back

    #print(matrix, opp, inv_opp, sep="\n")
    #print()
    return matrix, opp, inv_opp



def row_ech(matrix): #reducing to row echelon form

    #Initial leading zero sort plus storing the row operations
    row_ops=[]
    inv_row_ops=[]
    matrix, opp, inv_opp = row_sort(matrix)
    row_ops.append(opp)
    inv_row_ops.append(inv_opp)

    #performing systematic row operations and storing the row operations
    for i in range(matrix.shape[0]-1):
        for j in range(i+1, matrix.shape[0]):

            #creating and storing the row operation matrix
            opp=np.identity(matrix.shape[0])
            inv_opp=np.identity(matrix.shape[0])
            opp[j,i]= -(matrix[j,i]/matrix[i,i])
            inv_opp[j,i]= (matrix[j,i]/matrix[i,i])
            row_ops.append(opp)
            inv_row_ops.append(inv_opp)
        
            #performing the row operation (could also be done with matrix multiplication)
            matrix[j,:] = matrix[j,:] - (matrix[j,i]/matrix[i,i])*matrix[i,:]

        matrix, opp, inv_opp = row_sort(matrix)
        row_ops.append(opp)
        inv_row_ops.append(inv_opp)
        #print(matrix)

    #print(matrix, row_ops, inv_row_ops, sep="\n")
    return matrix, row_ops, inv_row_ops

    '''A problem here is that it may be dont after one row operation but still go on
        For example, [[1,2,3],[2,4,6],[1,0,0]] is sorted in one run but this code runs the second time anyway.
        I need to check each time if its already in row echelon which may or may not be more computationally effieient'''



    '''matrix[1,:]= matrix[1,:] - (matrix[1,0]/matrix[0,0])*matrix[0,:]
    matrix[2,:] = matrix[2,:] - (matrix[2,0]/matrix[0,0])*matrix[0,:]
    print(matrix)'''


#CODE FOR TESTING
'''
A=np.array([[1,2,3],[0,4,6],[1,0,0]], dtype=float)
A_n, opps, inv_opps = row_ech(A)
print(A) #this is the original matrix
print(A_n) 
print()

for i in range(len(opps)): #checking if inverses are good
    print(opps[i] @ inv_opps[i]) #opps[i] is the i-th row operation matrix
print()

for i in opps: #checking if the row operations are correct
    #print(i, A, sep="\n")
    A= i @ A
print(A)
print(A_n) #this should be the same as now edited A
print()
for i in inv_opps[::-1]: #checking if the inverse row operations are correct
    #print(i, A, sep="\n")
    A= i @ A
print(A) #should be the same as the original A
'''