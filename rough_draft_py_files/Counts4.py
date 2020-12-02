"""October 5th, 2020: Write a Python function called counts that takes a list as input
and returns a dictionary of unique items in the list as keys
and the number of times each item appears as values.
So, the input ['A', 'A', 'B', 'C', 'A'] should have output {'A': 3, 'B': 1, 'C': 1} .
Your code should not depend on any module from the standard library or otherwise.
You should research the task first and include a description with references of your algorithm in the notebook."""


# Creating an empty Dictionary
"""https://www.geeksforgeeks.org/python-dictionary/#:~:text=Creating%20a%20Dictionary,element%20being%20its%20Key%3Avalue%20."""
Dict = {} 

# Your code should not depend on any module from the standard library or otherwise.
# I have used Bubble sort as an alternative to inbuilt function sorted.
# There are many ready made sort algorithms such as Merge Sort, Tim Sort (which Python uses) each have their own strengths.
# I have copied the Bubble sort code and comments in its entirety from url below.
# Bubble sort is not always the fastest. I have used this Bubble sort code because it is concise and well commented by the author.
"""https://realpython.com/sorting-algorithms-python/"""

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

#takes a list of inputs separated by commas
"https://pynative.com/python-accept-list-input-from-user/"
input_string = input("Enter a list elements separated by COMMA ")
userList = input_string.split(",")
print("user list is ", userList)


#calls the User list and applies the bubble_sort function to sort it
str = userList
print("The sorted list is:", bubble_sort(str))

my_sorted_dictionary_keys = bubble_sort(str)


#python counting letters without count function
"""https://stackoverflow.com/questions/28966495/python-counting-letters-in-string-without-count-function"""


def count_letters(my_letter):
    count = 0

    for i in userList:
        if i == my_letter:
            count = count + 1

        else:
            continue

    return (count)


#add key value pairs to dictionary
#call function count_letters
"""https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/"""
for letter in my_sorted_dictionary_keys:
    Dict[letter] = count_letters(letter)



print("Dictionary sorted by keys from list, count of each letter in list", Dict)








