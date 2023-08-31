from modules.functions import get_todos, write_todos
import time
import streamlit as st


st.set_page_config(page_title="To-Do WebApp")

todos = get_todos("files/todos.txt")

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    write_todos(todos_arg=todos, filepath="files/todos.txt")


st.title("To-Do WebApp")
sub = st.subheader(time.strftime("%b %d, %Y"))
st.write("This WebApp is to increase your productivity.")

st.text_input(
    label="",
    label_visibility="collapsed",
    placeholder="Add new To-Do...",
    on_change=add_todo,
    key="new_todo"
)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# $ streamlit run main.py
