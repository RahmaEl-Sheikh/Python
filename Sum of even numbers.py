nums = []
print("Enter the size of list:", end="")
r= int(input())
print("Enter", r, "Elements for the list: ", end="")
for i in range(r):
    nums.append(int(input()))

sum = 0
count = 0
for i in range(r):
    if nums[i]%2 == 0:
        sum = sum + nums[i]
        count = count+1

if count==0:
    print("\nEven number is not found in this list!")
else:
    print("\nSum of Even Numbers =", sum)