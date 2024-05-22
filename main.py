import customtkinter as ctk
from tkinter import filedialog
import requests
import re 
import string
import os
import shutil


def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        print(f"Selected folder: {folder_selected}")
        folder_label.configure(text=f"Selected folder: {folder_selected}")
        global path
        path = folder_selected
def set_token():
    
    def get_token():
        with open("token.txt", "w") as file:
            entry_token = entry.get()
            file.truncate()
            file.write(entry_token)
        setToken.destroy()
    setToken = ctk.CTk()
    setToken.title("Setting")
    setToken.geometry("200x160")
    
    label = ctk.CTkLabel(setToken, text="Enter Your Uclassify Token:")
    label.pack(pady=(20,0))
    
    entry = ctk.CTkEntry(setToken)
    entry.pack(pady=20)
    
    with open("token.txt", "r") as file:
        token = file.read()
    entry.insert(0,token)
    
    button = ctk.CTkButton(setToken,text="save",command=get_token)
    button.pack()
    
    setToken.mainloop()
def main():
    fileName_topic = dict()
    items = os.listdir(path)

    for item in items:
        fileName_topic[item] = get_request(item)
    
    for item in items:
        move_file((path+"/"+item),(path+"/"+fileName_topic.get(item)))
    folder_label.configure(text="Selected foloder:")
    start_button.configure(text="Start")
    success_messageBox()
    
def success_messageBox():
    messageBox = ctk.CTk()
    messageBox.title("Success Msg")
    messageBox.geometry("300x80")
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    messageBox.attributes('-topmost', True)
    
    button = ctk.CTkButton(messageBox,text="Success!")
    button.pack(pady=20)
    
    messageBox.after(5000,messageBox.destroy)
    
    messageBox.mainloop()
    
        
def convert_file_name(original_string):
     modified_string = re.sub(f"[{re.escape(string.punctuation)}]", " ", original_string)
     return modified_string
 
def get_request(data):
    with open("token.txt", "r") as file:
        token = file.read()
    data = convert_file_name(data)
    url = "https://api.uclassify.com/v1/uclassify/topics/classify"
    params = {
        "readkey": token,
        "text": data
    }

    response = requests.get(url, params=params)
    result = response.json()
    max_class = max(result, key = result.get)
    return max_class

def move_file(source_path,distination_path):
    if not os.path.exists(distination_path):
        os.makedirs(distination_path)
    destination_file = os.path.join(distination_path, os.path.basename(source_path))
    shutil.move(source_path, destination_file)


ctk.set_appearance_mode("dark")

token=""

root = ctk.CTk()
root.title("Auto File Classifier")
root.geometry("400x230")

set_token_button = ctk.CTkButton(root, text="Setting", width=10, command=set_token)
set_token_button.pack(anchor="e",pady=10,padx=10)

select_button = ctk.CTkButton(root, text="Select Folder", command=select_folder)
select_button.pack(pady=10)


folder_label = ctk.CTkLabel(root, text="No folder selected")
folder_label.pack(pady=10)

start_button = ctk.CTkButton(root, text = "Start", command=main)
start_button.pack(fill="x", pady=20, padx=20)


root.mainloop()