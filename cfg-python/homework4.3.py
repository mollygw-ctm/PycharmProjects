import random

lottery_ticket = [
    2, 5, 10, 25, 30, 44,
]

print(lottery_ticket)

# choice list
lottery_choice = ([*range(1,49)])

lottery_numbers = [
    random.choice(lottery_choice), random.choice(lottery_choice), random.choice(lottery_choice), random.choice(lottery_choice), random.choice(lottery_choice), random.choice(lottery_choice), random.choice(lottery_choice),
]

print(lottery_numbers)

matching_numbers = [
    print(set(lottery_ticket) & set(lottery_numbers))
]

if len(matching_numbers) == 3:
    print("You win £20")
elif len(matching_numbers) == 4:
    print("You win £40")
elif len(matching_numbers) == 5:
    print("You win £100")
elif len(matching_numbers) == 6:
    print("You win £1000")
elif len(matching_numbers) == 7:
    print("You win £100000")
else:
    print("You have not won")




