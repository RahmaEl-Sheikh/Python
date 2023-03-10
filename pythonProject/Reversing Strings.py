# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string


R = "RahmaEl-Sheikh"

print("Your Original Sentence Is: ", end="")
print(R)

print("The Sentence After Being Reserved Is : ", end="")
print(reverse(R))
