import os

# Variables to change!!
name_want = "kekw"
dir = "./renames/"

# Get the list of files in the specificed directory
renames = os.listdir(dir)

# Loop through the list of files in the directory and rename
# Only the 2nd file onwards gets a numeric labeling
for num, file in enumerate(renames):
    try:
        if num == 0:
            os.rename(dir + file, dir + name_want + "." + file.split(".")[1])
        else:
            os.rename(dir + file, dir + name_want + f"_{num}." + file.split(".")[1])
    except FileExistsError:
        print("File already exists")
    except IndexError:
        print(f"The file '{file}' has no extention")
    
print("\nThe process has finished")

print(f"New files are {os.listdir(dir)}")