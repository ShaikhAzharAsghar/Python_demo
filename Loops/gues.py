secret_Number = 9
guess_count = 0
count_limit = 3
while guess_count < count_limit:
    guess = int(input("Guess : "))
    guess_count += 1
    if guess == secret_Number:
        print("You Won!")
        break
else:
    print("You are failed!")      