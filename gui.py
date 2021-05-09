
from PIL import ImageTk
from tkinter import *

from tkinter import filedialog
from PIL import Image
import os
cwd = os.getcwd()
import final
from tkinter.filedialog import askopenfilename 

root = Tk()
frame = Frame(root)
frame.pack()



image = Image.open(cwd+"/bg.jfif")
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()

label1 = Label(root, text='CHECK SKIN DISEASE')
label1.pack()





def callback():
    myFormats = [('JPEG / JFIF', '*.JPG') ]
    file = askopenfilename(filetypes=myFormats)
    skin_class = final.main(file)
    image = Image.open(file)
    photo = ImageTk.PhotoImage(image)
    # output = 'PATIENT IS SUFFERING WITH '+skin_class+' DISEASE.'

    label.configure(image=photo)
    label.image = photo

    # label1.configure(text=output)
    # label1.text=output


root.title(' Detection Of Melanoma Skin cancer')
root.geometry('800x800') # Size 200, 200
root.resizable(width=True, height=True)


Button(text='BROWSE', command=callback).pack(side=TOP, padx=10)
root.mainloop()
