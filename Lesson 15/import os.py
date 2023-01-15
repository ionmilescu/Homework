import os





folder_path = input("Enter the folder path: ")

if os.path.exists(folder_path):
    if os.path.isdir(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        for file in files:
            print(file)
    else:
        print("Provided path is not a folder.")
else:
    print("Provided path does not exist.")