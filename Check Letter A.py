# test_list = ""
# r= str(input(test_list))
# # print("Enter", r, "Elements for the list: ", end="")
# # for i in r(str(input(test_list))):
# #     test_list.append(test_list(input(test_list)))
# # # initializing check letter
# for r in test_list:
    
#         if r.startswith('a') or r.startswith('A'):
#     r.append(test_list)
# # print(test_list)
 
# # printing original list
# print("The original list : " + str(r))
 
# # using list comprehension + lower()
# # Words starting with specific letter
# res = [idx for idx in test_list if idx[0].lower() == find.lower()]
 
# # print result
# # print("The list of matching first letter : " + str(res))
# test_list()

# # def stringlist():
# #     lst = []
# #     newlst = []
# #     n = int(input("enter number of elements in the list: "))
# #     for i in range(0, n):
# #         ele = (input("Enter elements of the list: "))
# #         lst.append(ele)

# #     for n in lst:
# #         if n.startswith('a') or n.startswith('A'):
# #             newlst.append(n)
# #     print(newlst)
    

# # stringlist()

print("Enter the length of the list")

y = int(input())
r = []

for i in range(y):

    print("Enter value")
    inputValue = input()
    r.append(inputValue)

print(f"Your list is:\n {r}")


def startsWithA(lst):
    newlst = []
    for word in lst:
        if word.startswith("a") or word.startswith("A"):
            newlst.append(word)
    return newlst


print(f"The words that starts with A or a are:\n{startsWithA(r)}")