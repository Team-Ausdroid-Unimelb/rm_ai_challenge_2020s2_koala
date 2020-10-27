from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk,Image

class ImageFileState:
    def __init__(self):
        self.img_num = 0 # current image number
        self.filenames = None
        self.images = []
        self.image_size = (1300, 600)
        self.config_files = {}
    
    def set_file_names(self, file_names):
        self.filenames = file_names
    
    def clear_all_images(self):
        self.images.clear()
    
    def set_current_img_num(self, num):
        self.img_num = num
    
    def get_current_img(self):
        return self.images[self.img_num]

# Function for opening the file explorer window
def upload_images(slider, image_label, image_file_state):
    filenames = filedialog.askopenfilenames(initialdir="./", title="Select Images", filetypes=[("images", ".jpg .png")])

    if not filenames: # no files are selected
        return 

    image_file_state.set_file_names(filenames)

    # at least one file is selected
    image_file_state.clear_all_images()  # clear all images
    image_file_state.set_current_img_num(0) # reset image number

    # reset slider
    slider.configure(from_ = 1, to = len(image_file_state.filenames)) 
    slider.set(1)

    for i in filenames:
        im = Image.open(i)
        im.thumbnail(image_file_state.image_size, Image.ANTIALIAS)
        
        image_file_state.images.append(ImageTk.PhotoImage(im))
    
    # display the first image
    image_label.configure(image = image_file_state.images[0])
    return

# next image button
def next_image(slider, image_label, image_file_state):
    # when there is no image or the last image is showing, clicking the button will do nothing
    if not image_file_state.images or image_file_state.img_num >= len(image_file_state.images) - 1:
        return 

    image_file_state.set_current_img_num(image_file_state.img_num + 1)
    slider.set(image_file_state.img_num + 1)

    image_label.configure(image=image_file_state.images[image_file_state.img_num])

    # print(img_num)

def prev_image(slider, image_label, image_file_state):

    # when there is no image or the first image is showing, clicking the button will do nothing
    if not image_file_state.images or image_file_state.img_num <= 0:
        return 

    image_file_state.set_current_img_num(image_file_state.img_num - 1)
    slider.set(image_file_state.img_num + 1)

    image_label.configure(image=image_file_state.images[image_file_state.img_num])

    # print(img_num)

def upload_config_files(image_file_state):
    from zipfile import ZipFile
    cfg_file_names = []
    extract_folder = "config"
    files_needed = ["names", "cfg", "weights"]
    file_name = filedialog.askopenfilename(initialdir="./", title="Select a zip file that contains weight, name and zip file", 
                                            filetypes=[("zip", ".zip")])
    if not file_name:
        print("no file chosen")
        return
    # open the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
        # printing all the contents of the zip file 
        # zip.printdir() 
        cfg_file_names = zip.namelist()
        # extracting all the files to the config folder
        zip.extractall(extract_folder) 

    # remove all previous config files
    image_file_state.config_files.clear()

    # add corresponding file paths
    for i in cfg_file_names:
        if i.endswith(".weights"):
            image_file_state.config_files["weights"] = extract_folder + "/" + i
        elif i.endswith(".cfg"):
            image_file_state.config_files["cfg"] = extract_folder + "/" + i
        elif i.endswith(".names"):
            image_file_state.config_files["names"] = extract_folder + "/" + i

    # check if all required files are present. If not, print an error message
    for file in files_needed:
        if file not in image_file_state.config_files:
            messagebox.showinfo('Information', 'Please include names, cfg and weights files in the zip')
            image_file_state.config_files.clear() # remove all existing files
            return

    print(image_file_state.config_files)

def export_file():
    content = ["123", "456", "789"]

    """Save the current file as a new file."""
    filepath = filedialog.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        for i in content:
            output_file.write(i + "\n")


