saveData = input("What would you like to save? --> ") #asks the user what they want to save in the text file

file1=open("save.txt", "w") #opens the file to write in it
file1.write(saveData) #writes the saveData variable (in the actual app, this would be the native language of the user) in it (replacing everything else)
file1.close() #closes the file

file2 = open("save.txt", "r") #opens the file to read
fileContent = file2.read() #assigns the variable fileContent to the content of the file
print(fileContent) #prints the fileContent variable
file2.close() #closes the file

