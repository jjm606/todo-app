import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    todo_item = st.session_state['new_todo'] + "\n"
    todos.append(todo_item)
    write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo-app")
st.write("This app is to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo",
              placeholder="Add new todo...",
              on_change=add_todo,
              key='new_todo')
