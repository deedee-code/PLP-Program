# Create a new text file
try:
    with open("./Week 5/my_file.txt", "x") as create_file:
        create_file.writelines(["My name is Doris. \n", "I'm currently Learning Python at Power Learn Program. \n", "It's a 3 month program. \n"])
except FileExistsError:
    print("File already exist...")
except Exception as e:
    print("An error occured while creating a new file:", e)
else:
    print("New File created successfully!")


# File Reading and Display
try:
    with open("./Week 5/my_file.txt", "r") as read_file:
        content = read_file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist...")
except PermissionError:
    print("You don't have permission to read the file...")
except Exception as e:
    print("An error occured while reading the file", e)


# File Appending
try:
    with open("./Week 5/my_file.txt", "a") as append_file:
        append_file.write("I'm grateful for this opportunity. \n")
        append_file.write("Learning have been awesome so far. \n")
        append_file.write("At the end of this program, I want to be a Python Developer. \n")
except Exception as e:
    print("An error occured while appending the file", e)
else:
    print("File appended successfully!")