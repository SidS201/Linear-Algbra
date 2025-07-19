
import numpy as np
import row_ech

'''row1= list(i for i in input("Enter the first row of the matrix (space-separated): ").split())
row2= list(i for i in input("Enter the second row of the matrix (space-separated): ").split())
row3= list(i for i in input("Enter the third row of the matrix (space-separated): ").split())
matrix = np.array([row1, row2, row3], dtype=float)
print(matrix)'''

shape= tuple(int(i) for i in input("Enter number of rows, columns seperated by space: ").split())
print(shape)
matrix=np.zeros(shape, dtype=float)
for i in range(int(shape[0])):
    row= list(float(i) for i in input(f"Enter row {i+1} of the matrix (space-separated): ").split())
    matrix[i,:] = np.array(row, dtype=float)
print("Your matrix", matrix, sep="\n")
print()
print()

#%%
#Applying Row Opps
print("UPPER TRIANGLE USING ROW OPPS")
up_tr_mat, row_opps, inv_row_opps = row_ech.row_ech(matrix)
print("Matrix after row opps:", up_tr_mat, sep="\n")
print()
net_row_opp= np.identity(matrix.shape[0])
for i in row_opps:
    net_row_opp = i @ net_row_opp
print("Row operation matrix:", net_row_opp, sep="\n")
print("Matrix after row opps using multiplication by row opp matric:", net_row_opp @ matrix, sep="\n") #should be the same as up_tr_mat
print()
print()


#Applying Columns Opps
print("LOWER TRIANGLE USING COLUMN OPPS")
tr_mat=matrix.transpose()
tr_mat, tpse_row_opps, tpse_inv_row_opps = row_ech.row_ech(tr_mat)
tr_mat= tr_mat.transpose()
print("Matrix after column opps:", tr_mat, sep="\n")

col_opps=[]
inv_col_opps=[]
for i in range(len(tpse_row_opps)):
    col_opps.append(tpse_row_opps[i].transpose())
    inv_col_opps.append(tpse_inv_row_opps[i].transpose())
net_col_opp= np.identity(matrix.shape[0])
for i in col_opps:
    net_col_opp = net_col_opp @ i #order opp of row opps as columns opps occur on right

print("Column operation matrix:", net_col_opp, sep="\n")
print("Matrix after column opps using multiplication by column opp matric:", matrix @ net_col_opp, sep="\n") #should be the same as tr_mat

