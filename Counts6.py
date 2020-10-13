def counts(input_string): #Have created nested functions within counts

    
    
    def count_letters(my_letter,userList):
        count = 0

        for i in userList:
            if i == my_letter:
                count = count + 1

            else:
                continue

        return (count)

        
    def bubble_sort(array):
        n = len(array)

        for i in range(n):
            # Create a flag that will allow the function to
            # terminate early if there's nothing left to sort
            already_sorted = True

            # Start looking at each item of the list one by one,
            # comparing it with its adjacent value. With each
            # iteration, the portion of the array that you look at
            # shrinks because the remaining items have already been
            # sorted.
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    array[j], array[j + 1] = array[j + 1], array[j]

                    # Since you had to swap two elements,
                    # set the `already_sorted` flag to `False` so the
                    # algorithm doesn't finish prematurely
                    already_sorted = False

            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate
            if already_sorted:
                break

        return array


    def counts_part1(input_string): #the function takes a list of inputs separated by commas

        Dict = {} #Creating dictionary in the counts function for final out put
        userList = input_string.split(",")

        str = userList
        my_sorted_dictionary_keys = bubble_sort(str) #calls the User list and applies the bubble_sort function to sort it

        print(my_sorted_dictionary_keys)
        
        for letter in my_sorted_dictionary_keys:
            Dict[letter] = count_letters(letter,userList) #pass two arguments to the count letters function


        print("Dictionary sorted by keys from list, count of each letter in list", Dict)

    counts_part1(input_string)

input_string = input("Enter a list elements separated by COMMA ")
counts(input_string)
