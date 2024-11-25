import random

MIN_RANDOM = 10
MAX_RANDOM = 99
CORRECT_NEEDED = 3
italic_start = "\033[3m"
italic_end = "\033[0m"

def main():
    """
    This script simulates a math addition quiz.
    The user is prompted to calculate the sum of two random numbers.
    """
    print("Khansole Academy")

    correct_count = 0  # Counter for correct answers

    while correct_count < CORRECT_NEEDED:
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(f"What is {num1} + {num2}?")

        try:
            guess = int(input("Your answer: "))
            print(f"Your answer: {italic_start}{guess}{italic_end}")
            correct = num1 + num2

            if guess == correct:
                print("Correct!")
                correct_count += 1
            else:
                print(f"Incorrect. The expected answer is {correct}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Congratulations! You answered correctly 3 times in a row.")

if __name__ == '__main__':
    main()
