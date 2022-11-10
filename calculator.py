

class Matrix:
    
    def __init__(self):
        print("Matrix class has been instantiated, you can now create matrices and apply different calculation methods.")
    
    def create_matrices(self, number_of_matrix=1):
        
        n = number_of_matrix
        self.mat_1 = []
        self.mat_2 = []
        while True:
            if type(n)==int and n>0 and n<3:
            
                for i in range(1,n+1):
                    print(f"Enter order for the matrix-{i} in the form 'nxm':", end = " ")
                
                    while True:
                        order = input()
                        print()
                        if "x" in order and order.count("x")==1:
                        
                            try:
                                x,y = order.strip().split("x")
                                x = int(x)
                                y = int(y)
                                if i==1:
                                    self.mat_1 = Matrix.matrix_generation(row=x, col=y)
                                else:
                                    self.mat_2 = Matrix.matrix_generation(row=x, col=y)
                                break
                                    
                            except:
                                print("Please Enter the order in the correct format")
                                print()
                                continue
                break
                                
            else:
                while True:
                    try:
                        a = int(input("Enter the number of matrix 1 or 2: "))
                        break
                    except:
                        print('Wrong Value, Enter again')            
                        print()
                
        
    @staticmethod
    def matrix_generation(row=1, col=1):
        
        matrix = []
        for i in row:
            mat = []
            for j in col:
                
                while True:
                    
                    try:
                        print(f"Enter value for row-{i} column-{j} of your matrix:", end=" ")
                        val = int(input())
                        print()
                        mat.append(val)
                        break
                    
                    except:
                        print("Enter the appropriate value, Try again!")
                        print()
                        continue
        
            matrix.append(mat)
        
        return matrix
    
    @staticmethod
    def matrix_add(mat_1=[], mat_2=[]):
        
        ans_mat = []
        for i in range(len(mat_1)):
            ans = []
            for j in range(len(mat_1[0])):
                ans.append(mat_1[i][j]+mat_2[i][j])
            ans_mat.append(ans)
        
        return ans_mat
        
    @staticmethod
    def matrix_sub(mat_1=[], mat_2=[]):
        
        ans_mat = []
        for i in range(len(mat_1)):
            ans = []
            for j in range(len(mat_1[0])):
                ans.append(mat_1[i][j]-mat_2[i][j])
            ans_mat.append(ans)
        
        return ans_mat
    
    @staticmethod
    def matrix_mul(mat_1=[], mat_2=[]):
        
        ans_mat = []
        for i in range(len(mat_1)):
            ans = []
            for j in range(len(mat_2[0])):
                ans.append(0)
            ans_mat.append(ans)
        
        for i in range(len(ans_mat)):
            for j in range(len(ans_mat[0])):
                for k in range(len(mat_1[0])):
                    ans[i][j] += mat_1[i][k] * mat_2[k][j]
        
        return ans_mat
    
    @staticmethod
    def matrix_dev_num(mat=[], num=1):
        
        ans_mat = []
        for i in range(len(mat)):
            ans = []
            for j in range(len(mat[0])):
                ans.append(j/num)
            ans_mat.append(ans)

        return ans_mat
         
    
    
    def add_matrix(self):
        
        '''This method is designed for the addition of the two matrices'''
        
        print('''
Options: 
    1. Add the already generated matrices
    2. Add two desired matrices''') 
        
        print()
        print("Enter the opertion number: ")       
        
        
                                   