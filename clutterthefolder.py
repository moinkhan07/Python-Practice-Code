import os

folder_path = "clutterfolder"
dir_list = os.listdir(folder_path)
counter = 1
for file_name in dir_list:
    if file_name.endswith(".png"):
        new_file_name = f"{counter}.png"

        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        os.rename(old_file_path, new_file_path)

        counter += 1
