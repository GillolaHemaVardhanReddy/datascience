# open(file="FileDesctiptionorPath",mode="manychoices")
# mode is an optional string that specifies the mode in which the file is opened. 
# It defaults to 'r' which means open for reading in text mode. 
# Other common values are 'w' for writing (truncating the file if it already exists), 
# 'x' for creating and writing to a new file, and 
# 'a' for appending (which on some Unix systems, means that all writes append to the end of the file regardless of the current seek position). 
# In text mode, if encoding is not specified the encoding used is platform


 # method 1 :
# file = open('myfile.txt',mode='r')
# content = file.read()
# print(content)
# file.close()

# method 2 : effecient method
def readprint(file):
    file.seek(0)  # Ensure the file pointer is at the beginning
    content = file.read()
    print(content)
    
with open('myfile.txt', mode="r+") as file:
    readprint(file)  # Read and print the initial empty file content
    file.seek(0)
    file.write("highest score : 20")
    readprint(file)  # Read and print the updated file content