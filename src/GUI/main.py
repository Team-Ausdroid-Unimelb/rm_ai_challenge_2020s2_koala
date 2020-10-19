from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

filenames = None
images = []
img_num = 0 # current image number
image_size = (1300, 600)
config_files = {}

# Function for opening the file explorer window
def upload_images():
    # print("image label: ", image_label.winfo_height(), " ", image_label.winfo_width())
    # print("window: ", root.winfo_height(), " ", root.winfo_width())
    global filenames
    global img_num
    
    filenames = filedialog.askopenfilenames(initialdir="./", title="Select Images", filetypes=[("images", ".jpg .png")])

    if not filenames: # no files are selected
        return 

    # at least one file is selected
    images.clear()  # clear all images
    img_num = 0 # reset image number
    # reset slider
    slider.configure(from_ = 1, to = len(filenames)) 
    slider.set(1)

    for i in filenames:
        im = Image.open(i)
        im.thumbnail(image_size, Image.ANTIALIAS)
        
        images.append(ImageTk.PhotoImage(im))
    
    # display the first image
    image_label.configure(image = images[0])
    return

# next image button
def next_image():
    global images
    global img_num

    # when there is no image or the last image is showing, clicking the button will do nothing
    if not images or img_num >= len(images) - 1:
        return 

    img_num += 1
    slider.set(img_num + 1)

    image_label.configure(image=images[img_num])

def prev_image():
    global images
    global img_num

    # when there is no image or the first image is showing, clicking the button will do nothing
    if not images or img_num <= 0:
        return 

    img_num -= 1
    slider.set(img_num + 1)

    image_label.configure(image=images[img_num])

    # print(img_num)

def slider_show_image(v):
    global img_num

    img_num = int(v) - 1
    image_label.configure(image=images[img_num])

def upload_config_files():
    from zipfile import ZipFile
    cfg_file_names = []
    extract_folder = "config"
    file_name = filedialog.askopenfilename(initialdir="./", title="Select a zip file that contains weight, name and zip file", 
                                            filetypes=[("zip", ".zip")])
    print(file_name)

    # open the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
        # printing all the contents of the zip file 
        # zip.printdir() 
        cfg_file_names = zip.namelist()
        # extracting all the files to the config folder
        zip.extractall(extract_folder) 
    
    # print(cfg_file_names)

    # add corresponding file paths
    for i in cfg_file_names:
        if i.endswith(".weights"):
            config_files["weights"] = extract_folder + "/" + i
        elif i.endswith(".cfg"):
            config_files["cfg"] = extract_folder + "/" + i
        elif i.endswith(".names"):
            config_files["names"] = extract_folder + "/" + i
    print(config_files)

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

