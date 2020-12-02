import random

def dice_rolls(k,n):

    # CREATE LIST TO HOLD NUMBER OF DICE
    build_my_dice_box = []

    for i in range(k):
        build_my_dice_box.append(i+1)

    print("Dice in dice box", build_my_dice_box)


    
    # CREATE DICTIONARY TO CONTAIN VARIABLES OF DICE NUMBERS
    my_dict = {}

    #ADD DICE NUMBERS TO DICTIONARY, ie 2 dice creates twelve numbers, and twelve dictionary keys

    dice_variables = k * 6 #e.g. if there are two dice of six numbers, multiplying number of dice 2 x 6 = 12 variables

    while dice_variables > 0:
        my_dict[dice_variables] = 0
        dice_variables -= 1
        "https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key"
        my_dict = dict(sorted(my_dict.items()))
    print("\n Dictionary Created For Potential Dice Variables", my_dict)


    plusser = 0
    
    throw = n
    throw_counter = 1
    
    while throw > 0:
        a_dice_roll = random.randint(1,6)
        print("Throw:", throw_counter )
        for i in build_my_dice_box:
            
            update = (a_dice_roll + plusser)
            print("Random Throw with dice",i,"is equal to variable", update)

            "https://careerkarma.com/blog/python-dictionary-get/"
            dict_value = my_dict.get(update)
            my_dict[update] = dict_value + 1
            plusser += 6
        throw -= 1
        throw_counter += 1
        plusser = 0

    print("my full dictionary \n",my_dict)


    
    # STRIP 0 VALUES FROM DICTIONARY
    "https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python"
    for key, value in dict(my_dict).items():
        if value == 0: #deletes key from dictionary if value is 0
            del my_dict[key]
    print("my dictionary stripped of zero value keys\n",my_dict)



dice_rolls(2,1000)


