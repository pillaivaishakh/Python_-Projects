import random

def power_game():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    power = random.randint(1, 5)
    correct_answer = num1 ** power * num2

    print("What is {} raised to the power of {} multiplied by {}?".format(num1, power, num2))
    guess = int(input("Enter your answer: "))

    if guess == correct_answer:
        print("Congratulations, you got it right!")
    else:
        print("Sorry, the correct answer is {}.".format(correct_answer))

power_game()

