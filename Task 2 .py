with open("output.txt" , "w") as fh:
    a = input("Enter text to write to the file : ")
    fh.write(a)
    print("Data successfully written to output.txt.")
    b = input("Enter additional text to append :")
    fh.write(" \n" + b)
    print("Data successfully appeneded.")
print("Final content of output.txt :")
with open("output.txt", "r") as ah:
    data = ah.read()
print(data)