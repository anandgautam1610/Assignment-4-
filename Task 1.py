try:
    with open("sample1.txt" , "r") as fh:
        Line1 = fh.readline()
        Line2 = fh.readline()
    print("Reading file contents :")
    print(f"Line 1 : {Line1}")
    print(f"Line 2 : {Line2}")
except FileNotFoundError as Error:
    print("Error : The file sample.txt was not found.")

