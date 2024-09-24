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
            row.append(int(input(f"Enter the element for row {i+1} and column {j+1}: ")))
        matrix.append(row)
    return matrix

def matrix_print(matrix1):
    print(matrix1)
    for column in matrix1:
        for element in column:
            print(element, end="\t")
        print()

def main():

    ren, col = define_matrix_size()
    matrix1 = fill_matrix(ren, col)
    matrix_print(matrix1)

main()