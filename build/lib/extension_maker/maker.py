import os
def createFolder(folderName, callback):
    download_path = os.path.join(os.path.expanduser("~"), "Downloads", folderName)
    if os.path.exists(download_path):
        i = 1
        new_folder_name = os.path.join(os.path.expanduser("~"), "Downloads", f"{folderName}_{i}")
        while os.path.exists(new_folder_name):
            i += 1
            new_folder_name = os.path.join(os.path.expanduser("~"), "Downloads", f"{folderName}_{i}")
        os.makedirs(new_folder_name)
        callback(f"Folder '{download_path}' already exists. Created '{new_folder_name}' instead.")
        return new_folder_name
    else:
        os.makedirs(download_path)
        callback(f"Folder '{download_path}' created.")
        return download_path

