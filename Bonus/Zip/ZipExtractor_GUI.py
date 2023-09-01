from PySimpleGUI import *
from modules.zip_extractor import extract_archive


theme("DarkGrey15")

label_source = Text("Select Zip to Decompressed: ")
input_source = Input()
button_source = FilesBrowse("Choose", key="source", file_types=(("Zip Files", "*.zip"),))

label_destination = Text("Select Destination Folder:      ")
input_destination = Input()
button_destination = FolderBrowse("Choose", key="destination")

button_compress = Button("Extract")
label_output = Text(key="output", text_color="green")

layout = [
    [label_source, input_source, button_source], 
    [label_destination, input_destination, button_destination],
    [button_compress, label_output]
]

window = Window("Archive Extractor", layout=layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    # print(event, values)
    if event == WIN_CLOSED:
        break
    else:
        zippaths = values["source"].split(";")
        dest_dir = values["destination"]
        extract_archive(zippaths, dest_dir)
        window["output"].update(value="Extraction completed!")


window.close()
