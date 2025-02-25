from PIL import Image
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.constants import W
from tkinter import ttk

import json,os,requests,time
from . import config

root = tk.Tk() 
root.title("Extension Maker")
root.wm_iconbitmap('logo.ico')
root.geometry("1200x800") 

name_var=tk.StringVar()
short_name_var = tk.StringVar()
des_var=tk.StringVar()
version_var=tk.StringVar()
manifest_version_var=tk.StringVar()
manifest_version_var.set("3") 

def hello():
    print("hello")

def get_permissions(manifest_version):
    return config.BROWSER_MANIFEST_VERSION_3_PERMISSIONS

def set_result_text(text):
    old_text = result_text.get("1.0", tk.END)
    new_text = old_text + text
    result_text.insert(tk.END, new_text)
    result_text.see(tk.END)


def downloadFile(url, path):
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(path + file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                

def is_valid_version(version_str):
    try:
        version_str = version_str.split('.')
        if len(version_str) != 3:
            return False
        for i in version_str:
            if not i.isdigit():
                return False
        return True
    except:
        return False
    
name_label = tk.Label(root, text = '[*] Extension Name: ', font=('calibre',10, 'bold'))
name_label.grid(row=0, column=0, sticky = W, padx=10, pady=3)

def callback_name_massage(*args):
    if len(name_var.get()) > config.EXTENSION_NAME_MAX_LENGTH:
        name_massage.config(text="Extension Name is too long")
        name_massage.config(fg="red")
    elif len(name_var.get()) == 0:
        name_massage.config(text="Extension Name is required")
        name_massage.config(fg="red")        
    else:
        name_massage.config(text=" ["+str(config.EXTENSION_NAME_MAX_LENGTH - len(name_var.get()))+"] (maximum of "+str(config.EXTENSION_NAME_MAX_LENGTH)+" characters)")
        name_massage.config(fg="green")

name_var.trace_add("write", callback_name_massage)

name_entry = tk.Entry(root, textvariable = name_var, font=('calibre',10,'normal'), width=50)
name_entry.grid(row=0,column=1, sticky = W, pady=3, columnspan=2)

name_massage = tk.Label(root, text = " (maximum of "+str(config.EXTENSION_NAME_MAX_LENGTH)+" characters)", font=('calibre',10, 'bold'), fg="blue")
name_massage.grid(row=0, column=2, pady=3 )

short_name_label = tk.Label(root, text = '[?] Short Name: ', font=('calibre',10, 'bold'))
short_name_label.grid(row=1, column=0, sticky = W, padx=10, pady=3)

def callback_short_name_massage(*args):
    if len(short_name_var.get()) > config.EXTENSION_SHORT_NAME_MAX_LENGTH:
        short_name_massage.config(text="Short Name is too long")
        short_name_massage.config(fg="red")
    elif len(short_name_var.get()) == 0:
        short_name_massage.config(text="Short Name is required")
        short_name_massage.config(fg="red")    
    else:
        short_name_massage.config(text=" ["+str(config.EXTENSION_SHORT_NAME_MAX_LENGTH - len(short_name_var.get()))+"] (maximum of "+str(config.EXTENSION_SHORT_NAME_MAX_LENGTH)+" characters)")
        short_name_massage.config(fg="green")

short_name_var.trace_add("write", callback_short_name_massage)        

short_name_entry = tk.Entry(root, textvariable = short_name_var, font=('calibre',10,'normal'), width=50)
short_name_entry.grid(row=1,column=1, sticky = W, pady=3)

short_name_massage = tk.Label(root, text = " (maximum of "+str(config.EXTENSION_SHORT_NAME_MAX_LENGTH)+" characters)", font=('calibre',10, 'bold'), fg="blue")
short_name_massage.grid(row=1, column=2, pady=3 )

des_label = tk.Label(root, text = '[*] Extension description: ', font=('calibre',10, 'bold'))
des_label.grid(row=2,column=0, sticky = W, padx=10, pady=3)

def callback_des_massage(*args):
    if len(des_entry.get("1.0", tk.END)) > config.EXTENSION_DESCRIPTION_MAX_LENGTH:
        des_massage.config(text="Extension description is too long")
        des_massage.config(fg="red")
    if len(des_entry.get("1.0", tk.END)) == 0:
        des_massage.config(text="Extension description is required")
        des_massage.config(fg="red")    
    else:
        des_massage.config(text=" ["+str(config.EXTENSION_DESCRIPTION_MAX_LENGTH - len(des_entry.get("1.0", tk.END)))+"] (maximum of "+str(config.EXTENSION_DESCRIPTION_MAX_LENGTH)+" characters)")
        des_massage.config(fg="green")

des_var.trace_add("write", callback_des_massage)

des_entry = tk.Text(root, font=('calibre',10,'normal'), width=50,  height=3, wrap=tk.WORD )
des_entry.bind("<Key>", callback_des_massage)
des_entry.grid(row=2,column=1, sticky = W, pady=3, columnspan=2)

des_massage = tk.Label(root, text = " (maximum of "+str(config.EXTENSION_DESCRIPTION_MAX_LENGTH)+" characters)", font=('calibre',10, 'bold'), fg="blue")
des_massage.grid(row=2, column=2, pady=3 )


version_label = tk.Label(root, text = '[?] Extension Version: ', font=('calibre',10, 'bold'))
version_label.grid(row=3, column=0, sticky = W, padx=10, pady=3)

def callback_version_massage(*args):
    if is_valid_version(version_var.get()):
        version_massage.config(text=" (version : "+str(version_var.get())+")")
        version_massage.config(fg="green")
    else:
        version_massage.config(text="Version is not valid:- [Like: 1.0.0]")
        version_massage.config(fg="red")   

version_var.trace_add("write", callback_version_massage)

version_entry = tk.Entry(root, textvariable = version_var, font=('calibre',10,'normal'), width=50)
version_entry.grid(row=3,column=1, sticky = W, pady=3)

version_massage = tk.Label(root, text = " (default version : 1.0.0)", font=('calibre',10, 'bold'), fg="blue")
version_massage.grid(row=3, column=2,sticky = W, pady=3)

manifest_version_label = tk.Label(root, text = '[?] Manifest Version: ', font=('calibre',10, 'bold'))
manifest_version_label.grid(row=4, column=0, sticky = W, padx=10, pady=15)



manifest_version_menu = tk.OptionMenu(root, manifest_version_var, *config.MANIFEST_VERSION_LIST)
manifest_version_menu.grid(row=4, column=1, sticky = W, pady=15)

manifest_permission_label = tk.Label(root, text = '[?] Manifest permissions: ', font=('calibre',10, 'bold'))
manifest_permission_label.grid(row=5, column=0, sticky = W, padx=10, pady=3)


def get_selected_permission(event):
    selected_permissions = manifest_permission_list.curselection()
    MANIFEST_PERMITIONS = [manifest_permission_list.get(i) for i in selected_permissions]
    object_format = {  "permissions": MANIFEST_PERMITIONS }
    selected_items_list_Format = json.dumps(object_format, indent=4)
    manifest_permission_massage.delete('1.0', tk.END)
    manifest_permission_massage.insert(tk.END, str(selected_items_list_Format))

manifest_permission_list = tk.Listbox(root, selectmode=tk.MULTIPLE, width=20, font=('calibre',10,'normal'), exportselection=False)
manifest_permission_list.grid(row=6, column=0, sticky = W, pady=3, padx=25)

manifest_permission_list.bind("<<ListboxSelect>>", get_selected_permission)

for permission in config.BROWSER_MANIFEST_VERSION_3_PERMISSIONS:
    manifest_permission_list.insert(tk.END, permission)


manifest_permission_massage = tk.Text(root, font=('calibre',10, 'bold'), fg="green", height=10, width=45)
manifest_permission_massage.grid(row=6, column=1, pady=3)

def collback_image_upload():
    file_types = [("Image Files", "*.png *.jpg *.jpeg")]
    file_path = tk.filedialog.askopenfilename(filetypes=file_types)
    if len(file_path):
        image = Image.open(file_path)
        image = image.resize((128,128))
        image = ImageTk.PhotoImage(image)
        image_label.image = image
        image_label.text = file_path
        image_label.config(image=image)
        image_label.config(text=file_path)
        print(file_path)

        


image_button = tk.Button(root, text = "Select Logo", font=('calibre',10, 'bold'), command=collback_image_upload)
image_button.grid(row=0, column=3, pady=3, padx=60,rowspan=2)

image_label = tk.Label(root, image=None, text = "", font=('calibre',10, 'bold'))
image_label.config(image=None)
image_label.grid(row=1, column=3, rowspan=4)



host_permission_label = tk.Label(root, text = '[?] Host permissions: ', font=('calibre',10, 'bold'))
host_permission_label.grid(row=5, column=2, sticky = W, padx=10, pady=3)


def get_selected_host_permission(event):
    manifest_permission_list.selection_set(first=0)
    selected_permissions = host_permission_list.curselection()
    HOST_PERMITIONS = [host_permission_list.get(i) for i in selected_permissions]
    object_format = {  "host_permissions": HOST_PERMITIONS }
    selected_items_list_Format = json.dumps(object_format, indent=4)
    host_permission_massage.delete('1.0', tk.END)
    
    host_permission_massage.insert(tk.END, str(selected_items_list_Format))

host_permission_list = tk.Listbox(root, selectmode=tk.MULTIPLE, width=20, font=('calibre',10,'normal'), exportselection=False)
host_permission_list.grid(row=6, column=2, sticky = W, pady=3, padx=25)


host_permission_list.bind("<<ListboxSelect>>", get_selected_host_permission)

for permission in config.MANIFEST_HOST_PERMISSIONS:
    host_permission_list.insert(tk.END, permission)

host_permission_massage = tk.Text(root, font=('calibre',10, 'bold'), fg="green", height=10, width=45)
host_permission_massage.grid(row=6, column=3, pady=3)

file_label = tk.Label(root, text = '[?] Create a file and adding manifest.json', font=('calibre',10, 'bold'))
file_label.grid(row=7, column=0, sticky = W, padx=10, pady=10, columnspan=2)


def get_selected_file_list(event):
    selected_file = file_list.curselection()
    object_format = {}
    for i in selected_file:
        if file_list.get(i) =="background":
            if manifest_version_var.get()=="3":
                object_format["background"] = {
                    "service_worker": "background.js"
                }
            elif manifest_version_var.get()=="2":
                object_format["background"] = {
                    "scripts": ["background.js"]
                }
        if file_list.get(i) =="content":
            if manifest_version_var.get()=="3":
                object_format["content_scripts"] = [
                    {
                        "matches": ["<all_urls>"],
                        "js": ["content-script.js"],
                        "run_at": "document_start",
                        "all_frames": True
                    }
                ]
            elif manifest_version_var.get()=="2":
                object_format["content_scripts"] = [
                    {
                        "matches": ["<all_urls>"],
                        "js": ["content-script.js"],
                        "run_at": "document_start",
                    }
                ]
        if file_list.get(i) =="interface":
            if manifest_version_var.get()=="3":
                object_format["action"] = {
                    "default_icon": {
                        "128": "data/icons/128.png", 
                        "64": "data/icons/64.png", 
                        "48": "data/icons/48.png", 
                        "32": "data/icons/32.png"
                        },
                    "default_popup": "data/interface/popup.html",
                    "default_title": "__MSG_app_name__"
                }
            elif manifest_version_var.get()=="2":
                object_format["browser_action"] = {
                    "default_icon": {
                        "128": "data/icons/128.png", 
                        "64": "data/icons/64.png", 
                        "48": "data/icons/48.png", 
                        "32": "data/icons/32.png"
                        },
                    "default_popup": "data/interface/popup.html",
                    "default_title": "__MSG_app_name__"
                }
        if file_list.get(i) =="options":
            if manifest_version_var.get()=="3":
                object_format["options_ui"] = {
                    "page": "data/options/options.html",
                    "chrome_style": True
                }
            elif manifest_version_var.get()=="2":
                object_format["options_page"] = "data/options/options.html"    

    selected_items_list_Format = json.dumps(object_format, indent=4)
    file_list_massage.delete('1.0', tk.END)
    file_list_massage.insert(tk.END, str(selected_items_list_Format))            
                                       



file_list = tk.Listbox(root, selectmode=tk.MULTIPLE, width=20, font=('calibre',10,'normal'), exportselection=False)
file_list.grid(row=8, column=0, sticky = W, pady=3, padx=25)

file_list.bind("<<ListboxSelect>>", get_selected_file_list)

for file in config.CREATE_EXTENSION_FILE:
    file_list.insert(tk.END, file)

file_list_massage = tk.Text(root, font=('calibre',10, 'bold'), fg="green", height=10, width=45)
file_list_massage.grid(row=8, column=1, pady=3)

libery_label = tk.Label(root, text = '[?] Download a library', font=('calibre',10, 'bold'))
libery_label.grid(row=7, column=2, sticky = W, padx=10, pady=10, columnspan=2)

libery_file = "libery.json"

if not os.path.exists(libery_file):
    LIBERY_DATA = ""
    set_result_text("Error: Extension Folder Not Exist! "+libery_file)
else:
    with open(libery_file) as DATA:
        LIBERY_DATA = json.load(DATA)

if LIBERY_DATA != "":
    LIBERY_KEY = []
    for key in LIBERY_DATA.keys():
       LIBERY_KEY.append(key)
else:
    LIBERY_KEY = []      
        

def get_selected_libery_list(event):
    selected_libery = libery_list.curselection()
    object_format = {}
    for i in selected_libery:
        object_format[libery_list.get(i)] = LIBERY_DATA[libery_list.get(i)]   
    selected_items_list_Format = json.dumps(object_format, indent=4)
    libery_list_massage.delete('1.0', tk.END)
    libery_list_massage.insert(tk.END, str(selected_items_list_Format))

libery_list = tk.Listbox(root, selectmode=tk.MULTIPLE, width=20, font=('calibre',10,'normal'))
libery_list.grid(row=8, column=2, sticky = W, pady=3, padx=25)

libery_list.bind("<<ListboxSelect>>", get_selected_libery_list)


libery_list_massage = tk.Text(root, font=('calibre',10, 'bold'), fg="green", height=10, width=45, exportselection=False)
libery_list_massage.grid(row=8, column=3, pady=3)

for libery in LIBERY_KEY:
    libery_list.insert(tk.END, libery)

def OpenFolder(name):
    if not os.path.exists(name):
        set_result_text("Error: Extension Folder Not Exist! "+name)
    else:
        path = os.path.realpath(name)
        os.startfile(path)  

result_text = tk.Text(root, font=('calibre',10, 'bold'), fg="green", height=6, width=70)
result_text.delete('1.0', tk.END)
result_text.grid(row=9, column=0, sticky = W, padx=25, pady=10, columnspan=2)



generate_progress = ttk.Progressbar(root, orient = 'horizontal', length = 500, mode = 'determinate')
generate_progress.grid(row=10, column=0,  padx=25,  columnspan=2)
generate_progress['value'] = 0

def htmlPackageCreate(file_path, file_name):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        set_result_text("Interface folder created successfully")
    else:
        set_result_text("Interface folder already exists")

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
        set_result_text(file_name+".html file created successfully")

        with open(file_path+"/"+file_name+".js", 'w') as outfile:
            outfile.write("// "+file_name+".js file created")
            set_result_text(file_name+".js file created successfully")

        with open(file_path+"/"+file_name+".css", 'w') as outfile:
            outfile.write("/* "+file_name+" file created */")
            set_result_text(file_name+".css file created successfully") 


def create_extension():
    print(str(manifest_permission_list.curselection()))
    print(str(host_permission_list.curselection()))
    generate_progress['value'] = 0
    generate_progress.update()
    # check all required fields
    if len(name_var.get()) == 0:
        set_result_text("Extension Name is required")
        return
    elif len(name_var.get()) > config.EXTENSION_NAME_MAX_LENGTH:
        set_result_text("Extension Name is too long")
        return
    else:
        set_result_text("Extension Name is valid:- "+ str(name_var.get())) 

    generate_progress['value'] +=5   
    generate_progress.update() 
    if len(short_name_var.get()) == 0:
        set_result_text("Short Name is required")
        return
    elif len(short_name_var.get()) > config.EXTENSION_SHORT_NAME_MAX_LENGTH:
        set_result_text("Short Name is too long")
        return
    else:
        set_result_text("Short Name is valid:- "+ str(short_name_var.get()))

    generate_progress['value'] +=5 
    generate_progress.update()   

    if image_label.cget("image") == None or image_label.cget("image") == "":
        set_result_text("Logo is required")
        return
    else:
        set_result_text("Logo is valid")

    generate_progress['value'] +=5 
    generate_progress.update()  

    if len(des_entry.get("1.0", tk.END)) == 0:
        set_result_text("Extension description is required")
        return
    elif len(des_entry.get("1.0", tk.END)) > config.EXTENSION_DESCRIPTION_MAX_LENGTH:
        set_result_text("Extension description is too long")
        return
    else:
        set_result_text("Extension description is valid:- "+ str(des_entry.get("1.0", tk.END)))

    generate_progress['value'] +=5 
    generate_progress.update()     

    if not is_valid_version(version_var.get()):
        set_result_text("Version is not valid:- [Like: 1.0.0]")
    elif len(version_var.get()) == 0:
        set_result_text("Defult version is : 1.0.0")
    else:
        set_result_text("Version is valid:- "+ str(version_var.get()))

    generate_progress['value'] +=5 
    generate_progress.update() 

    set_result_text("Manifest Version is "+ str(manifest_version_var.get())) 

    generate_progress['value'] +=5 
    generate_progress.update()   

    selected_permissions = manifest_permission_list.curselection()
    MANIFEST_PERMITIONS = [manifest_permission_list.get(i) for i in selected_permissions]
    if len(MANIFEST_PERMITIONS) == 0:
        set_result_text("Manifest permissions is not avalable")
    else:
        set_result_text("Manifest permissions is valid:- "+ str(MANIFEST_PERMITIONS))

    generate_progress['value'] +=5 
    generate_progress.update()  

    selected_host = host_permission_list.curselection()
    HOST_PERMITIONS = [host_permission_list.get(i) for i in selected_host]

    if len(HOST_PERMITIONS) == 0:
        set_result_text("Host permissions is not avalable")
    else:
        set_result_text("Host permissions is valid:- "+ str(HOST_PERMITIONS)) 

    generate_progress['value'] +=5 
    generate_progress.update() 
                          
    if len(version_var.get()) == 0:
        APP_VERSION = "1.0.0"
    else:
        APP_VERSION = str(version_var.get())   


    #create extension folder
    extension_folder = "V"+APP_VERSION+"_M"+manifest_version_var.get()
    if not os.path.exists(extension_folder):
        os.makedirs(extension_folder)
        set_result_text("Extension folder created successfully")
    else:
        set_result_text("Extension folder already exists")
        return

    generate_progress['value'] +=5 
    generate_progress.update() 


    # create _locales folder and en folder and messages.json file
    locales_folder = extension_folder+"/_locales/en"
    if not os.path.exists(locales_folder):
        os.makedirs(locales_folder)
        set_result_text("Locales folder created successfully")
    else:
        set_result_text("Locales folder already exists")

    generate_progress['value'] +=5 
    generate_progress.update()     

    APP_DESCRIPTION = str(des_entry.get("1.0", tk.END)).replace("\n", " ").replace("\r", " ")  
    # create manifest file
    manifest = {
        "manifest_version": int(manifest_version_var.get()),
        "name": "__MSG_app_name__",
        "short_name": "__MSG_app_short_name__",
        "description": "__MSG_app_description__",
        "version": APP_VERSION,
    }
    generate_progress['value'] +=5 
    generate_progress.update() 

    massages_json = {
        "app_name": {
            "message": name_var.get()
        },
        "app_description": {
            "message": APP_DESCRIPTION 
        },
        "app_short_name": {
            "message": short_name_var.get()
        }
    }

    # save messages.json file
    with open(extension_folder+"/_locales/en/messages.json", 'w') as outfile:
        json.dump(massages_json, outfile, indent=4)
        set_result_text("Messages.json file created successfully")
        manifest["default_locale"] = "en"

    generate_progress['value'] +=5 
    generate_progress.update()     


    if len(MANIFEST_PERMITIONS):
        manifest["permissions"] = MANIFEST_PERMITIONS

    if len(HOST_PERMITIONS):
        if manifest_version_var.get() == "3":
            manifest["host_permissions"] = HOST_PERMITIONS

    generate_progress['value'] +=5 
    generate_progress.update()

    selected_file = file_list.curselection()
    if len(selected_file):
        for i in selected_file:
            if file_list.get(i) =="background":
                # create background.js file
                with open(extension_folder+"/background.js", 'w') as outfile:
                    outfile.write("// background.js file created")
                    set_result_text("Background.js file created successfully")   

                if manifest_version_var.get()=="3":
                    manifest["background"] = {
                        "service_worker": "background.js"
                    }

                elif manifest_version_var.get()=="2":
                    manifest["background"] = {
                        "scripts": ["background.js"]
                    }  
   
            if file_list.get(i) =="content":
                # create content-script.js file  
                with open(extension_folder+"/content-script.js", 'w') as outfile:
                    outfile.write("// content-script.js file created")
                    set_result_text("content-script.js file created successfully")   
                if manifest_version_var.get()=="3":
                    manifest["content_scripts"] = [
                        {
                            "matches": ["<all_urls>"],
                            "js": ["content-script.js"],
                            "run_at": "document_start",
                            "all_frames": True
                        }
                    ]
                elif manifest_version_var.get()=="2":
                    manifest["content_scripts"] = [
                        {
                            "matches": ["<all_urls>"],
                            "js": ["content-script.js"],
                            "run_at": "document_start",
                        }
                    ]
            if file_list.get(i) =="interface":
                interface_folder = extension_folder+"/data/interface"
                htmlPackageCreate(interface_folder, "popup")

                if manifest_version_var.get()=="3":
                    manifest["action"] = {
                        "default_icon":{
                            "128": "data/icons/128.png", 
                            "64": "data/icons/64.png", 
                            "48": "data/icons/48.png", 
                            "32": "data/icons/32.png"
                            },
                        "default_popup": "data/interface/popup.html",
                        "default_title": "__MSG_app_name__"
                    }
                elif manifest_version_var.get()=="2":
                    manifest["browser_action"] = {
                        "default_icon": {
                            "128": "data/icons/128.png", 
                            "64": "data/icons/64.png", 
                            "48": "data/icons/48.png", 
                            "32": "data/icons/32.png"
                            },
                        "default_popup": "data/interface/popup.html",
                        "default_title": "__MSG_app_name__"
                    }
            if file_list.get(i) =="options":
                options_folder = extension_folder+"/data/options"
                htmlPackageCreate(options_folder, "options")

                if manifest_version_var.get()=="3":
                    manifest["options_ui"] = {
                        "page": "data/options/options.html",
                        "chrome_style": True
                    }
                elif manifest_version_var.get()=="2":
                    manifest["options_page"] = "data/options/options.html"    

    generate_progress['value'] +=5 
    generate_progress.update()

    # create logo file resize 128x128, 48x48, 64x64, 32x32
    LOGO_NAME = image_label.cget("image")
    LOGO_SRC = image_label.cget("text")
    if LOGO_NAME != "" and LOGO_SRC != "":
        if not os.path.exists(extension_folder+"/data/icons"):
            os.makedirs(extension_folder+"/data/icons")
            set_result_text("Icons folder created successfully")
        else:
            set_result_text("Icons folder already exists") 

        image = Image.open(LOGO_SRC)
        image128 = image.resize((128,128))
        image128.save(extension_folder+"/data/icons/128.png")

        iamge64 = image.resize((64,64))
        iamge64.save(extension_folder+"/data/icons/64.png")

        image48 = image.resize((48,48))
        image48.save(extension_folder+"/data/icons/48.png")

        image32 = image.resize((32,32))
        image32.save(extension_folder+"/data/icons/32.png")

        set_result_text("Logo resized successfully")

        manifest["icons"] = {
            "128": "data/icons/128.png",
            "64": "data/icons/64.png",
            "48": "data/icons/48.png",
            "32": "data/icons/32.png"
        }

    generate_progress['value'] +=5 
    generate_progress.update()

    # save manifest.json file
    with open(extension_folder+"/manifest.json", 'w') as outfile:
        json.dump(manifest, outfile, indent=4)
        set_result_text("Manifest.json file created successfully")   

    generate_progress['value'] +=5 
    generate_progress.update() 

    if LIBERY_KEY:
        try:
            libery_path = extension_folder + "/lib/"
            if not os.path.exists(libery_path):
                os.makedirs(libery_path)
                set_result_text("Libery folder created successfully")
                selected_libery = libery_list.curselection()
                for i in selected_libery:
                    file_path = LIBERY_DATA[libery_list.get(i)]
                    downloadFile(file_path, libery_path)
                    time.sleep(1)
                    set_result_text("Libery downloading..")
                    
            else:
                set_result_text("Libery folder already exists")
            
        except:
            set_result_text("Error: libery download")
    else:
        set_result_text("Libery is not load!")       
        

    generate_progress['value'] = 100
    generate_progress.update()
    set_result_text("Extension created successfully")
    OpenFolder(extension_folder)



generate_button = tk.Button(root, text = "Generate Extension", font=('calibre',10, 'bold'),width=30, height=2, command=create_extension)
generate_button.grid(row=9, column=2,  padx=10, columnspan=2)
root.mainloop()










