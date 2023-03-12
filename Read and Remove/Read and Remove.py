# Variable contains the path to the file
# path = r"Read and Remove\Read and Remove from.txt"
 
# # The file is read and its data is stored
# data = open(path, 'r').read()
 
# # Replacing all occurrences of newline in data with ''
# data = data.replace('\n', '')
 
# # Displaying the resultant data
# print(data)

# input text file
inputFile = "Read and Remove\Read and Remove from.txt"

# Opening the given file in read-only mode
with open(inputFile, 'r') as filedata:

   # Reading the file lines using readlines()
   linesList= filedata.readlines()
   
   # Removing the new line character(\n) from the list of lines 
   print([k.rstrip('\n') for k in linesList])

# Closing the input file
filedata.close()