# filename=input("Enter file name: ")
# for line in reversed(list(open(filename))):
#     print(line.rstrip())# Define the function reverse_string in my_module
# # Open the file in write mode
# # Open the file in write mode
# #  filename= open("output1.txt", "w")
 
# # Open the input file and get
# # the content into a variable data
# with open("file.txt", "r") as filename:
#     data = filename.read()
 
# # For Full Reversing we will store the
# # value of data into new variable data_1
# # in a reverse order using [start: end: step],
# # where step when passed -1 will reverse
# # the string
# data_1 = data[::-1]
 
# # Now we will write the fully reverse
# # data in the output1 file using
# # following command
print(end="Enter File's Name: ")
fname = input()

try:
  fhand = open(fname, "r")

  fcont = ""
  for cont in fhand:
    fcont = fcont + cont

  print("\n----Content of \"" +str(fname)+ "\" in Original Order----")
  print(fcont)
  print("\n----Content of \"" +str(fname)+ "\" in Reverse Order----")
  fcont = fcont[::-1]
  print(fcont)

except IOError:
  print("\nThe file doesn't exist!")