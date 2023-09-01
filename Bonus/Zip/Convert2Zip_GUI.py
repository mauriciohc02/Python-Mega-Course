from PySimpleGUI import *
from modules.zip_creator import compress2zip


theme("DarkGrey15")

label_source = Text("Select Files to Compress: ")
input_source = Input()
button_source = FilesBrowse("Choose", key="source")

label_destination = Text("Select Destination Folder: ")
input_destination = Input()
button_destination = FolderBrowse("Choose", key="destination")

button_compress = Button("Compress")
label_output = Text(key="output", text_color="green")

layout = [
    [label_source, input_source, button_source], 
    [label_destination, input_destination, button_destination],
    [button_compress, label_output]
]

window = Window("File Compressor", layout=layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    # print(event, values)
    if event == WIN_CLOSED:
        break
    else:
        filepaths = values["source"].split(";")
        folder = values["destination"]
        compress2zip(filepaths, folder)
        window["output"].update(value="Compression completed!")


window.close()
