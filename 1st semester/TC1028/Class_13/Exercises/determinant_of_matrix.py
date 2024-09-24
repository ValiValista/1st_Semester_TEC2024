print("Program without functions to capture and print a matrix")

def define_matrix_size():
    ren=int(input("Enter the number of rows: "))
    col=int(input("Enter the number of columns: "))
    return ren, col

def fill_matrix(ren, col):
    matrix = []
    for i in range(ren):
        row=[]
        for j in range (col):
            row.append(int(input(f"Enter the element for row {i} and column {j}: ")))
        matrix.append(row)
    return matrix

def matrix_print(matrix1):

    key_men = int(input("""
1. Print the matrix as a list
2. Print the matrix as a table
3. Exit
Enter the number of your choice:
"""))
    if key_men > 0 and key_men == 1:
        print(matrix1)
        return True
    elif key_men > 0 and key_men == 2:
        for column in matrix1:
            for element in column:
                print(element, end="\t")
            print()
        return True
    elif key_men > 0 and key_men == 3:
        return False
    else:
        print("Invalid option")
        return True
def determinant(matrix):
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return "The matrix must be square"
        for j in range(len(matrix[i])):
            determinant1 = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return determinant1
def main():
    ren, col = define_matrix_size()
    matrix1 = fill_matrix(ren, col)
    print(f"The determinant is {determinant(matrix1)}")

main()