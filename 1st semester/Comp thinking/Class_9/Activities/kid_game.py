import random


# Function to ask a math question and check the answer
def ask_question(level):
    if level == 'easy':
        a, b = random.randint(1, 9), random.randint(1, 9)
        result = a + b
        answer = int(input(f"What is {a} + {b}? "))
    elif level == 'medium':
        a, b = random.randint(10, 99), random.randint(1, 9)
        result = a + b
        answer = int(input(f"What is {a} + {b}? "))
    elif level == 'hard':
        a, b = random.randint(1, 9), random.randint(1, 9)
        result = a * b
        answer = int(input(f"What is {a} * {b}? "))

    return answer == result


# Function for each difficulty level
def play_level(level):
    correct_answers = 0
    while correct_answers < 10:
        if ask_question(level):
            print("Correct!")
            correct_answers += 1
        else:
            print("Wrong answer! Try again.")
            return correct_answers, False  # Return current score and indicate the game is over
    return correct_answers, True  # Player passed the level


# Function for infinite mode
def play_infinite_mode():
    correct_answers = 0
    levels = ['easy', 'medium', 'hard']

    while True:
        level = random.choice(levels)
        if ask_question(level):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong answer! You answered {correct_answers} correctly.")
            return correct_answers


# Function to check if the player has a highscore and update it
def check_highscore(score, highscores):
    if score > min(highscores):
        print(f"New highscore: {score}")
        highscores.append(score)
        highscores.sort(reverse=True)
        highscores.pop()  # Maintain only top 3 highscores


# Main menu
def main_menu():
    highscores = [0, 0, 0]  # Placeholder for top 3 high scores (combined for all levels)

    while True:
        print("\nWelcome to the Math Game!")
        print("1. Play Game")
        print("2. View Highscores")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            total_score = 0

            # Easy Level
            print("\nStarting Easy Level:")
            score, passed = play_level('easy')
            total_score += score
            if not passed:
                check_highscore(total_score, highscores)
                print("Thanks for playing!")
                continue  # Boot to main menu

            # Medium Level
            print("\nStarting Medium Level:")
            score, passed = play_level('medium')
            total_score += score
            if not passed:
                check_highscore(total_score, highscores)
                print("Thanks for playing!")
                continue  # Boot to main menu

            # Hard Level
            print("\nStarting Hard Level:")
            score, passed = play_level('hard')
            total_score += score
            if not passed:
                check_highscore(total_score, highscores)
                print("Thanks for playing!")
                continue  # Boot to main menu

            # Infinite Mode
            print("\nWelcome to Infinite Mode!")
            score = play_infinite_mode()
            total_score += score
            check_highscore(total_score, highscores)

            print(f"Your total score: {total_score}")
            print("Thanks for playing!")

        elif choice == '2':
            print("\nHighscores:")
            for i, hs in enumerate(highscores, 1):
                print(f"{i}. {hs}")
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the game
main_menu()
