# Define the function reverse_string in my_module
def reverse_string(string):
    return string[::-1]

# Import my_module
import my_module

# Prompt the user to enter a string
input_string = input("Enter a string:")

# Reverse the entered string using the reverse_string function from my_module
reversed_str = my_module.reverse_string(input_string)

# Print the reversed string
print("Reversed string:", reversed_str)
