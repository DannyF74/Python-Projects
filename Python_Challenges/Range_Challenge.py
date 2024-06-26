#RANGE CHALLENGE REQUIREMENTS
#
# Challenge 1.
# Start IDLE and use the Python range( ) function with one parameter to display the following:
# 0
# 1
# 2
# 3
#
# Challenge 2.
# Use the Python range( ) function with 3 parameters to display the following:
# 3 2 1 0
#
# Challenge 3.
# Use the Python range( ) function with 3 parameters to display the following:
# 8 6 4 2


# Created a list with the numbers required and created a loop that iterates
# starting at index 0 and continuing through the length of my list, printing
# the value at each index
print("Challenge 1:")
mylist = (0,1,2,3)
mylistlen = len(mylist)
for i in range(0, mylistlen):
    print(mylist[i])

# Used the mylistlen variable -1 to set the start point of my range and -1
# to mark the end of the range. Then iterated through using -1 as the step
# to print the values in decending order.
print("\nChallenge 2:")
for i in range(mylistlen-1, -1, -1):
    print(mylist[i])

# I'm not sure if this was a typo or display error on the LMS portal
# but it looks like it wants me to display the numbers side by side.
#
# Created a new variable and set the values using the range function to
# save time rather than writing the numbers 0 - 9 manually. Then created
# an empty list for the results to go in. Set the range to start at index
# 8, end at index 0 and the step to decrease by 2. Then take each result
# and add it to the empty list. Finally print the list so the results
# are side by side.
print("\nChallenge 3:")
x = range(0,10)
x_result = []
for i in range(8, 0, -2):
    x_result.append(x[i])
print(x_result)

