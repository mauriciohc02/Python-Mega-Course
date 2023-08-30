from modules.functions import get_todos, write_todos
import time
import os
from PySimpleGUI import *


if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", "w") as file:
        pass

# Theme that the App will be using
#theme("DarkGrey15")
theme("PythonPlus")
# Instance some elements for the GUI
clock = Text("", key="clock")
label = Text("Type in a To-Do")
input_box = InputText(tooltip="Enter To-Do", key="new_todo") # key is like an ID for the object
add_button = Button(
    key="Add",
    size=(50, 50), 
    image_source="images/add_todo.png",
    tooltip="Add To-Do"
)
list_box = Listbox(
    values=get_todos("files/todos.txt"),
    key="todos",
    enable_events=True,
    size=[45, 10]
)
edit_button = Button(
    key="Edit",
    size=(50, 50), 
    image_source="images/edit_todo.png",
    tooltip="Edit To-Do"
)
complete_button = Button(
    key="Complete",
    size=(50, 50), 
    image_source="images/complete_todo.png",
    tooltip="Complete To-Do"
)
exit_button = Button("Exit")

# Layout with the elements for the window
layout = [
    [clock],
    [label], 
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
]
# Create the window with Title, Elements and Fonts
window = Window(
    "To-Do App", 
    layout=layout,
    font=("Helvetica", 20)
)

while True:
    # Get action the user has done
    event, values = window.read(timeout=1000)
    now = time.strftime("%b %d, %Y %H:%M:%S")
    window["clock"].update(value=now)
    print(event, values)

    match event:
        # For updating the clock without closing the App
        case "__TIMEOUT__":
            continue

        # Add a new task for To-Do list 
        case "Add":
            todos = get_todos()
            new_todo = values["new_todo"] + "\n"
            todos.append(new_todo)
            write_todos(todos, "files/todos.txt")
            window["todos"].update(values=todos)

        # Edit an existing task in the To-Do list
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["new_todo"]
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n" if new_todo[-1] != "\n" else new_todo
                print(todos[index])
                write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                popup("Please select an item first", title="Warning", font=("Helvetica", 20))

        # Complete an existing task in the To-Do list
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(filepath="files/todos.txt", todos_arg=todos)
                window["todos"].update(values=todos)
                window["new_todo"].update(value="")
            except IndexError:
                popup("Please select an item first", title="Warning", font=("Helvetica", 20))

        # Exit the App (Exit button)
        case "Exit":
            break
            
        # Update the InputText based on the task selected
        case "todos":
            window["new_todo"].update(value=values["todos"][0])

        # Exit the App (Close button)
        case WIN_CLOSED:
            break


window.close()
