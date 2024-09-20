names = ["Ana", "Juan", "Pedro", "Pablo", "Maria", "Jose", "Luis", "Rosa", "Ricardo", "Andrea"]


def insert_name(func_n_of_names):
    for i in range(func_n_of_names):
        f_name=(input(f"What name do you want to insert at index {len(names)}?: "))
        names.append(f_name)
    return names

def list_print():
    for i in range(len(names)):
        print(names[i], end = " ")
    print()


def main():
    print("This program ...")
    n_of_names = int(input("Enter the number of names you want to add: "))
    insert_name(n_of_names)
    list_print()
main()