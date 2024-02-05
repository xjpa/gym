correct_number = 5
number_input = int(input("guess a number between 1 and 10"))
if number_input == correct_number:
    print("you guessed correctly")
elif 4 >= number_input >= 0:
    print("wrong, but so close!")
else:
    print("wrong")