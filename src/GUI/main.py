from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from filemanagement import *

# start putting on widgets
root = Tk() 
root.title('Upload Images') 
root.geometry("1500x660") 
root.config(background = "white") 

# create widgets
# upload_image_button = Button(root, text = "Upload Images", command = upload_images, compound="c") 

button_prev = Button(root, text="<<", command=prev_image, compound="c")
button_next = Button(root, text=">>", command=next_image, compound="c")
slider = Scale(root, from_=0, to=0, orient=HORIZONTAL, command=slider_show_image)

image_label = Label()

# put widgets on screen
button_prev.grid(row = 0, column = 5)
button_next.grid(row = 0, column = 6)
slider.grid(row = 0, column = 7)

image_label.grid(row = 1, column = 0, columnspan = 8)

# menu 
menubar = Menu(root)
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Upload Images", command = upload_images)
filemenu.add_command(label="Upload weight, name and config files as a zip", command=upload_config_files)
filemenu.add_command(label="export", command=lambda: 0)

menubar.add_cascade(label="Menu", menu=filemenu)

root.config(menu=menubar)

root.mainloop()

