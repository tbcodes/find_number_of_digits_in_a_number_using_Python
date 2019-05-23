# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# TRUZZ BLOGG - Python Programming: How to find the total number of digits in a number
# Youtube Link: https://youtu.be/DewBxUNPTqU
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# 1º Method: 

user_input = int(input("Please, enter a number: "))
user_input = abs(user_input)
# First method used to display the content of a variable:
print("Your original number is: ", user_input)
# Another way to display the content stored in a variable:
# print("Your original number is: {}".format(user_input))
# Third method you can use in order to print out the content of a variable
# print("Your original number is: %d " %user_input)

count = 0
while user_input > 0:
  user_input //= 10
  count += 1
  
print("The number of digits in your number is: {} ".format(count))


# Bonus -_- # 2º Method: The easy one!

my_number = 7548
print(len(str(my_number)))

# Or

my_number2 = int(input("Please, enter a number: "))
print(len(str(my_number2)))








