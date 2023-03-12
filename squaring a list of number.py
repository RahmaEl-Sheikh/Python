# importing math module
# import math

# # input list
# inputList= int(input())
# r=[]

# # Printing the input list
# # print("Input List: ", inputList)

# # list comprehension by checking whether the square root
# # of number is equal to the floor of 
# # for r in inputList:
# #                   if (math.sqrt(r) == math.floor(math.sqrt(r))):
                      

# # # Printing all the perfect squares in an input list
# #                         print("Perfect squares in an input list: ", r)
# def square(r):
#     for i in r:
#         r=[number ** 2 for number in inputList]
#     #    print (i**2)
#         r.append(i ** i)
#         return (r)

# # inputList = int(input())
# # r= []
# # for i in range(inputList):

# #     print("Enter value")
# #     inputValue = int(input())
# #     r.append(inputValue)

# # print(f"Your list is:\n {inputList}")


# # def getSquared(lst):
    

# #     newList = []
# #     for num in lst:
# #         newList.append(pow(num, 2))
# #     return newList


# # print(f"The Squared List:\n{getSquared(inputList)}")
# import math 
# LengthOfInput= int(input())
# def int_func(li):
    
#     sqr=[]
#     x=0
#     for i in LengthOfInput:
#        x= pow(i,2)
#        print(x)
#     return sqr
# print(LengthOfInput)
import math

print("Enter the length of the list")

inputLength= int(input())
r = []

for i in range(inputLength):

    print("Enter value")
    inputValue = int(input())
    r.append(inputValue)

print(f"Your list is:\n {r}")


def getSquared(lst):
    newList = []
    for num in lst:
        newList.append(pow(num, 2))
    return newList


print(f"Here's your list squared:\n{getSquared(r)}")