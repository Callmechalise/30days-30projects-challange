import os.path
from PIL import Image
from tkinter.filedialog import askopenfilename

path=askopenfilename(filetypes=[('PNG Files', '*.png'),('All Files', '*.*')])
img=Image.open(path)
print("Input size")
width=int(input("Enter width:-->"))
height=int(input("Enter Height-->"))
size=(width,height)
if path.lower().endswith(('.png','.jpg','.jpeg')):
    filename,extension=os.path.splitext(path)
    resizedimage=img.resize(size)
    resizedimage.save(f"resized.{extension}")
resizedimage.show()