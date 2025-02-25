import os,time
from PIL import Image
from . import config

def htmlPackageCreate(file_path, file_name, callback):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        callback("Interface folder created successfully")
    else:
        callback("Interface folder already exists")

    with open(file_path+"/"+file_name+".html", 'w') as outfile:
        popup_html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Popup</title>
        <link rel="stylesheet" type="text/css" href='"""+file_name+""".css'>
    </head>
    <body>
    </body>
    <script src='"""+file_name+""".js'></script>
</html>
            """
        outfile.write(popup_html)
        callback(file_name+".html file created successfully")

        with open(file_path+"/"+file_name+".js", 'w') as outfile:
            outfile.write("// "+file_name+".js file created")
            callback(file_name+".js file created successfully")
        with open(file_path+"/"+file_name+".css", 'w') as outfile:
            outfile.write("/* "+file_name+" file created */")
            callback(file_name+".css file created successfully")


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


def fileCreate(filepath, callback):
    file_name  = filepath.split("/")[-1]
    callback(f"{file_name} file creating..")
    with open(filepath, 'w') as outfile:
        outfile.write(f"// {file_name} file created")
        callback(f"{file_name} file created successfully") 
        callback(f"file load: {filepath}")


def logoCreate(path, image_src, callback):
    if not os.path.exists(path):
        os.makedirs(path)
        callback("Icons folder created successfully")
        callback(f"Icons folder location: {path}")

        image = Image.open(image_src)
        for size in config.EXTENSION_SIZE:
            resizeImage = image.resize((size,size))
            resizeImage.save(f"{path}/"+str(size)+".png")
            callback("Logo resized in: "+ str(size))
            time.sleep(1)

        callback("Logo resized successfully")   
    else:
        callback("Icons folder already exists")
    