import os


print("current dic\n",os.getcwd())

# Shows where your script is running   C:\flutter_windows_3.24.2-stable\Desk\Python

print(os.listdir())  # Lists all files/folders in the current director

for i in os.listdir():
    print(i)


# print(os.mkdir("test_folder"))

# os.makedirs("a/b/c")

# os.rmdir("test_folder")

os.removedirs("a/b/c")   # Removes nested empty folders
