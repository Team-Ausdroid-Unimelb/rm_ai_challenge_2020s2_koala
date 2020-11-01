from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from filemanagement import *

image_file_state = ImageFileState()

# change image based on the slider value
def slider_show_image(value):
    image_file_state.set_current_img_num(int(value) - 1)
    image_label.configure(image=image_file_state.get_current_img())

# start putting on widgets
root = Tk() 
root.title('Upload Images') 
root.geometry("1500x660") 
root.config(background = "white") 

# create widgets
# upload_image_button = Button(root, text = "Upload Images", command = upload_images, compound="c") 

slider = Scale(root, from_=0, to=0, orient=HORIZONTAL, command = slider_show_image)
button_prev = Button(root, text="<<", command=lambda: prev_image(slider, image_label, image_file_state), compound="c")
button_next = Button(root, text=">>", command=lambda: next_image(slider, image_label, image_file_state), compound="c")

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

filemenu.add_command(label="Upload Images", command = lambda: upload_images(slider, image_label, image_file_state))
filemenu.add_command(label="Upload weight, name and config files as a zip", command=lambda: upload_config_files(image_file_state))
filemenu.add_command(label="export", command=lambda: export_file())

menubar.add_cascade(label="Menu", menu=filemenu)

root.config(menu=menubar)

root.mainloop()

