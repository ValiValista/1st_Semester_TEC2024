import random


# Function to generate a question, ensuring it's unique
def generate_unique_question(level, asked_questions):
    while True:  # Keep generating until we find a unique question
        if level == 'easy':
            a, b = random.randint(1, 9), random.randint(1, 9)
            question = (a, b, '+')  # Store as a tuple (operand1, operand2, operator)
            result = a + b
        elif level == 'medium':
            a, b = random.randint(10, 99), random.randint(1, 9)
            question = (a, b, '-')  # Store as a tuple (operand1, operand2, operator)
            result = a - b
        elif level == 'hard':
            a, b = random.randint(1, 9), random.randint(1, 9)
            question = (a, b, '*')  # Store as a tuple (operand1, operand2, operator)
            result = a * b

        if question not in asked_questions:  # Check if the question was asked before
            asked_questions.add(question)  # Add it to the set of asked questions
            return question, result


# Function to ask a math question and check the answer
def ask_question(question, result):
    a, b, operator = question

    if operator == '+':
        answer = int(input(f"What is {a} + {b}? "))
    elif operator == '-':
        answer = int(input(f"What is {a} - {b}? "))
    elif operator == '*':
        answer = int(input(f"What is {a} * {b}? "))

    return answer == result


# Function for each difficulty level
def play_level(level):
    asked_questions = set()  # Store previously asked questions for this level
    correct_answers = 0
    target_correct = 5 if level in ['easy', 'medium'] else 10  # 5 for easy/medium, 10 for hard

    while correct_answers < target_correct:
        if level == 'medium':
            # Generate a unique question and keep asking the same question until the answer is correct
            question, result = generate_unique_question(level, asked_questions)
            while True:  # Keep asking the same question until the correct answer is given
                if ask_question(question, result):
                    print("Correct!")
                    correct_answers += 1
                    break  # Move to the next question
                else:
                    print("Wrong answer! Try again. You must get it right to proceed.")
        else:
            if ask_question(*generate_unique_question(level, asked_questions)):
                print("Correct!")
                correct_answers += 1
            else:
                print("Wrong answer! Try again.")
                return correct_answers, False  # End the game on wrong answer (except Medium)

    return correct_answers, True


# Function for infinite mode
def play_infinite_mode():
    correct_answers = 0
    levels = ['easy', 'medium', 'hard']
    asked_questions = {level: set() for level in levels}  # Track questions for all levels

    while True:  # Infinite loop for continuous play
        level = random.choice(levels)
        question, result = generate_unique_question(level, asked_questions[level])
        if ask_question(question, result):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong answer! You answered {correct_answers} correctly.")
            return correct_answers


# Function to check if the player has a highscore and update it
def check_highscore(score, highscores):
    for i in range(len(highscores)):
        if score > highscores[i]:
            print(f"New highscore: {score}")
            highscores.append(score)
            highscores.sort(reverse=True)
            highscores.pop()  # Maintain only top 3 highscores
            return True  # Indicate that a highscore was set
    return False  # No highscore set


# Function to view high scores
def view_highscores(highscores):
    print("\nHighscores:")
    for i, hs in enumerate(highscores, 1):
        print(f"{i}. {hs}")


# Main menu
def main():
    highscores = [0, 0, 0]  # Placeholder for top 3 high scores

    while True:  # Main loop to keep the game running
        print("\nWelcome to the Math Game!")
        print("1. Play Game")
        print("2. View Highscores")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            total_score = 0

            # Play each level, and if the player fails, return to the menu
            for level_name in ['easy', 'medium', 'hard']:
                print(f"\nStarting {level_name.capitalize()} Level:")
                score, passed = play_level(level_name)
                total_score += score
                if not passed:
                    if check_highscore(total_score, highscores):
                        print(f"Your total score: {total_score}")
                        print("New highscore recorded! Thanks for playing!")
                    else:
                        print(f"Your total score: {total_score}")
                        print("Thanks for playing!")
                    break  # Exit to the main menu after a wrong answer
            else:
                # Infinite Mode
                print("\nWelcome to Infinite Mode!")
                score = play_infinite_mode()
                total_score += score
                if check_highscore(total_score, highscores):
                    print(f"Your total score: {total_score}")
                    print("New highscore recorded! Thanks for playing!")
                else:
                    print(f"Your total score: {total_score}")
                    print("Thanks for playing!")

        elif choice == '2':
            view_highscores(highscores)

        elif choice == '3':
            print("Thanks for playing!")
            break  # Exit the game loop

        else:
            print("Invalid choice. Try again.")


# Run the game
main()
