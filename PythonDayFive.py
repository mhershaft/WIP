import random
import time
again=True
ones="no"
twos="no"
threes="no"
fours="no"
fives="no"
sixes="no"
three_of_a_kind="no"
four_of_a_kind="no"
full_house="no"
small_straight="no"
large_straight="no"
yahtzee="no"
chance="no"
print ("Welcome to Yahtzee!")
while again==True:
    dice_one = str(random.randint(1, 6))
    dice_two = str(random.randint(1, 6))
    dice_three = str(random.randint(1, 6))
    dice_four = str(random.randint(1, 6))
    dice_five = str(random.randint(1, 6))
    print ("Your dice rolls were "+ dice_one + ", " + dice_two + ", " + dice_three + ", " + dice_four + ", and " + dice_five + ".")
    int(dice_one)
    int(dice_two)
    int(dice_three)
    int(dice_four)
    int(dice_five)
    all_dice=[dice_one, dice_two, dice_three, dice_four, dice_five]
    random_dice_number=random.randint(0,4)
    random_one=all_dice[random_dice]
    random_two=all_dice[random_dice]
    random_three=all_dice[random_dice]
    random_four=all_dice[random_dice]
    random_five=all_dice[random_dice]
    random_all=[random_one, random_two, random_three, random_four, random_five]
    if dice_one==dice_two==dice_three==dice_four==dice_five:
        input("You can do: Yahtzee, Four Of A Kind, Three Of A Kind, Chance, or " + str(dice_one)+ "'s.")
    elif all_dice[random_dice]==all_dice[random_dice]==all_dice[random_dice]==all_dice[random_dice]:
        print("Test")
    #Work on line above