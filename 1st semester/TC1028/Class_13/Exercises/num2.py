print("Program to create a matrix of n rows and m columns filled with consecutive numbers per rows starting with 1")
def get_valid_input(prompt):
    while True:
        try:
            answer = int(input(prompt))
            if answer >= 0:
                return answer
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def define_matrix_size():
    row=get_valid_input("Enter the number of rows: ")
    col=get_valid_input("Enter the number of columns: ")
    return row, col

def fill_matrix(row, col):
    matrix = []
    for i in range(row):
        rows=[]
        for j in range (col):
            app_sum = i
            rows.append(app_sum)
        matrix.append(rows)
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

def main():
    row, col = define_matrix_size()
    matrix1 = fill_matrix(row, col)
    while matrix_print(matrix1):
        matrix_print(matrix1)

main()