import random

def dice_rolls(k,n):

    dice_variables = k * 6
    # CREATE DICTIONARY
    my_dict = {}

    #ADD DICE NUMBERS TO DICTIONARY, ie 2 dice creates twelve numbers, and twelve dictionary keys
    while dice_variables > 0:
        my_dict[dice_variables] = 0
        dice_variables -= 1
        "https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key"
        my_dict = dict(sorted(my_dict.items()))
    print("\n Dictionary Created For Potential Dice Variables", my_dict)



    build_my_dice_box = []
    plusser = 0
    n = 2

    for i in range(n):
        build_my_dice_box.append(i+1)

        

    print("Dice in dice box", build_my_dice_box)



    a_dice_roll = random.randint(1,6)

    
    for i in build_my_dice_box:
        update = (a_dice_roll + plusser)
        print("Random Throw with dice",i,"is equal to variable", update)
        my_dict[update] = +1
        plusser += 6
    print (my_dict)


    
    # STRIP 0 VALUES FROM DICTIONARY
    "https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python"
    for key, value in dict(my_dict).items():
        if value == 0: #deletes key from dictionary if value is 0
            del my_dict[key]
    print(my_dict)



dice_rolls(2,5)


