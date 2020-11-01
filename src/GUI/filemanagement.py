from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk,Image
from pathlib import Path
import GUI_support

class ImageFileState:
    def __init__(self):
        self.img_num = 0                # current image number
        self.filenames = None
        self.images_folder = None
        self.images = []                # images files
        self.image_size = (1300, 600)
        self.config_files = {}
        self.labelled_images = []       # labelled images output
        self.export_content = ""        # text to be exported with the export button
    
    def set_file_names(self, file_names):
        self.filenames = file_names
    
    def set_images_folder(self, images_folder):
        self.images_folder = images_folder
    
    def set_labelled_images(self, labelled_images):
        self.labelled_images = labelled_images
    
    def set_export_content(self, export_content):
        self.export_content = export_content

    def clear_labelled_images(self):
        self.labelled_images = []

    def clear_export_content(self):
        self.export_content = ""

    def clear_all_images(self):
        self.images.clear()
    
    def set_current_img_num(self, num):
        self.img_num = num
    
    def get_current_img(self):
        return self.images[self.img_num]

# Function for opening the file explorer window
def upload_images(slider, image_label, image_file_state, label_button, left_arrow, right_arrow, output):
    # Get the filenames
    filenames = filedialog.askopenfilenames(initialdir="./", title="Select Images", filetypes=[("images", ".jpg .png")])
    
    if not filenames: # no files are selected
        return
    
    # Save the folder selected
    image_file_state.set_images_folder(Path(filenames[0]).parent)
    # Save file names
    standard_filenames = []
    for filename in filenames:
        standard_filenames.append(Path(filename))
    image_file_state.set_file_names(standard_filenames)

    # at least one file is selected
    image_file_state.clear_all_images()         # clear all images
    image_file_state.clear_labelled_images()    # clear labelled imaged output
    image_file_state.clear_export_content()     # clear export content
    image_file_state.set_current_img_num(0)     # reset image number

    # reset slider
    slider.configure(from_ = 1, to = len(image_file_state.filenames)) 
    slider.set(1)

    for i in filenames:
        im = Image.open(i)
        im.thumbnail(image_file_state.image_size, Image.ANTIALIAS)
        
        image_file_state.images.append(ImageTk.PhotoImage(im))
    
    # display the first image
    image_label.configure(image = image_file_state.images[0])

    # Clear output board
    output.delete(1.0, END)

    # make buttons active
    label_button.configure(state=NORMAL)
    slider.configure(state=NORMAL)
    left_arrow.configure(state=NORMAL)
    right_arrow.configure(state=NORMAL)
    return

# next image button
def next_image(slider, image_label, image_file_state):
    # when there is no image or the last image is showing, clicking the button will do nothing
    if not image_file_state.images or image_file_state.img_num >= len(image_file_state.images) - 1:
        return 

    image_file_state.set_current_img_num(image_file_state.img_num + 1)
    slider.set(image_file_state.img_num + 1)


def prev_image(slider, image_label, image_file_state):

    # when there is no image or the first image is showing, clicking the button will do nothing
    if not image_file_state.images or image_file_state.img_num <= 0:
        return 

    image_file_state.set_current_img_num(image_file_state.img_num - 1)
    slider.set(image_file_state.img_num + 1)


def upload_config_files(image_file_state):
    from zipfile import ZipFile
    cfg_file_names = []
    extract_folder = "config"
    files_needed = ["names", "cfg", "weights"]
    file_name = filedialog.askopenfilename(initialdir="./", title="Select a zip file that contains weight, name and zip file", 
                                            filetypes=[("zip", ".zip")])
    if not file_name:
        print("No file chosen.")
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
            messagebox.showinfo('Information', 'Please include weights, cfg and names files in the .zip')
            image_file_state.config_files.clear() # remove all existing files
            return
    
    messagebox.showinfo('Information', 'Files were uploaded successfully.')
    print("Config files uploaded.")


def write_output(output, labelled_image):
    output.delete(1.0, END)
    output.tag_configure("bold", font=("Segoe UI", 9, "bold"))
    output.insert(END, "Image ID: ", "bold")
    output.insert(END, str(labelled_image.ID) + "\n")
    output.insert(END, "File Name: ", "bold")
    output.insert(END, str(labelled_image.filename) + "\n")
    output.insert(END, "Location Speed: ", "bold")
    output.insert(END, str(labelled_image.speed) + " fps\n")
    output.insert(END, "------\n")
    output.insert(END, "--\n")
    for armour in labelled_image.armours:
        output.insert(END, "Robot: ", "bold")
        output.insert(END, str(armour.robot) + "\n")
        output.insert(END, "Pose: ", "bold")
        output.insert(END, str(armour.pose) + "\n")
        output.insert(END, "Armour Location: ", "bold")
        output.insert(END, "x=" + str(armour.location[0]) + "px, ")
        output.insert(END, "y=" + str(armour.location[1]) + "px, ")
        output.insert(END, "weight=" + str(armour.location[2]) + "px, ")
        output.insert(END, "height=" + str(armour.location[3]) + "px\n")
        output.insert(END, "Confidence: ", "bold")
        output.insert(END, str(armour.confidence) + "\n")
        output.insert(END, "--\n")
    output.insert(END, "------\n")


def export_file(content):
    """Save the current file as a new file."""
    filepath = filedialog.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        for i in content:
            output_file.write(i)

def print(*args):
    top = GUI_support.w
    for arg in args:
        top.Console.insert(END, str(arg))
    top.Console.insert(END, "\n")
