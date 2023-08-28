from modules.functions import get_todos, write_todos
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # Delete spaces

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos("files/todos.txt")
        # list comprehension that delete each "\n"
        # new_todos = [item.strip("\n") for item in todos]
        for i, item in enumerate(todos):
            item = item.strip("\n")  # Delete the "\n"
            item = item.title()  # Capitalize each word of the string
            print(f"{i + 1}.- {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1
            todos = get_todos("files/todos.txt")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos, "files/todos.txt")
        # In case that user don't enter a number (example: "edit some other words")
        except ValueError:
            print("Your command isn't valid")
            continue
        except IndexError:
            print("There's no item with that number")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos.pop(number - 1)
            todo_to_remove = todo_to_remove.strip("\n")
            write_todos(filepath="files/todos.txt", todos_arg=todos)
            print(f"Todo \"{todo_to_remove.title()}\" was removed from the list.")
        except IndexError:
            print("There's no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("The command entered doesn't exist")


print("Bye!")
