import streamlit as st
import functions1

#print("inicio")
#print(st.sidebar.session_state)
tasks = functions1.get_todos()

def add_task():
    task = st.session_state["new_task"] + "\n"
    if task == "\n":
        return
    else:
        tasks.append(task)
        functions1.write_todos(tasks)


st.title("WELCOME - MY TODO APP")
st.subheader("To do tasks")
st.sidebar.subheader("Done tasks")

st.sidebar.write(functions1.read_done())

for index, task in enumerate(tasks):
    check_box = st.checkbox(task, key=task)
    if check_box:
        tasks_done = functions1.read_done()
        tasks_done.append(tasks[index])
        functions1.write_done(tasks_done)
        tasks.pop(index)
        del st.session_state[task]
        functions1.write_todos(tasks)
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add your task here...", on_change = add_task, key = 'new_task')

#print("fin")

#st.session_state