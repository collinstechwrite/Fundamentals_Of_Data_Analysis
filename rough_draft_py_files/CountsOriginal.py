"""October 5th, 2020: Write a Python function called counts that takes a list as input
and returns a dictionary of unique items in the list as keys
and the number of times each item appears as values.
So, the input ['A', 'A', 'B', 'C', 'A'] should have output {'A': 3, 'B': 1, 'C': 1} .
Your code should not depend on any module from the standard library or otherwise.
You should research the task first and include a description with references of your algorithm in the notebook."""


# Creating an empty Dictionary
"""https://www.geeksforgeeks.org/python-dictionary/#:~:text=Creating%20a%20Dictionary,element%20being%20its%20Key%3Avalue%20."""
Dict = {} 

#Python 3 program to sort letters of string alphabetically
def sortList(myList):
    a_sorted_list = sorted(userList)
    return a_sorted_list


#takes a list of inputs separated by commas
"https://pynative.com/python-accept-list-input-from-user/"
input_string = input("Enter a list elements separated by COMMA ")
userList = input_string.split(",")
print("user list is ", userList)


#calls the User list and applies the bubble_sort function to sort it
str = userList
print("The sorted list is:", sortList(str))

my_sorted_dictionary_keys = sortList(str)



#add key value pairs to dictionary
#call function count_letters
"""https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/"""
for letter in my_sorted_dictionary_keys:
    Dict[letter] = my_sorted_dictionary_keys.count(letter)


print("Dictionary sorted by keys from list, count of each letter in list", Dict)








