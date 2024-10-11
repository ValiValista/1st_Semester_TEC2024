def get_valid_input_int(prompt):
    while True:
        try:
            answer = int(input(prompt))
            if answer >= 0:
                return answer
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_input_str(prompt):
    while True:
        try:
            answer = input(prompt)
            if answer != "":
                answer = answer.strip()
                return answer
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


