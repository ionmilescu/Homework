import os


def list_files_in_folder(folder_path):
    if os.path.exists(folder_path):
        if os.path.isdir(folder_path):
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            for file in files:
                print(file)
        else:
            print("Provided path is not a folder.")
    else:
        print("Provided path does not exist.")
        


def rename_file(src, dst):
    os.rename(src, dst)
    print(f"{src} has been renamed to {dst}")

src_path = os.path.join(list_files_in_folder)
dst_path = os.path.join(list_files_in_folder)
rename_file(src_path, dst_path)