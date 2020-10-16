from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

filenames = None
images = []

# Function for opening the file explorer window
def browseFiles():
    global filenames
    images.clear()
    
    filenames = filedialog.askopenfilenames(initialdir="./", title="Select Images", filetypes=[("images", ".jpg .png")])
    # label_file_explorer.configure(text="File Opened: "+ filenames[0]) 
    for i in filenames:
        images.append(ImageTk.PhotoImage(Image.open(i)))

    # put images onto labels
    if images:
        for i in images:
            my_label = Label(image=i)
            my_label.pack()
        
    return

# start putting on widgets
root = Tk() 
root.title('Upload Images') 
root.geometry("500x500") 
root.config(background = "white") 

# Create a File Explorer label 
# label_file_explorer = Label(root, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue") 

button_explore = Button(root, text = "Upload Images", command = browseFiles) 

# label_file_explorer.grid(column = 1, row = 1) 
button_explore.pack()

root.mainloop()

