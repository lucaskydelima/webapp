import streamlit as st
from modules import functions


def add_todo():
    new_todo = st.session_state["new_todo"].title() + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


todos = functions.get_todos()

st.title("My Todo APP")
st.subheader("This is my todo app.")
st.text("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo ...",
              on_change=add_todo, key="new_todo")

