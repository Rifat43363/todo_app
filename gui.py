import functions
import FreeSimpleGUI as sg
label= sg.Text('Type in a todo')
#this will stay at the left of the empty box and explain what to enter
input_box= sg.InputText(tooltip='Write Todo', key='todo')
#the input code seems to work with both Input and InputText
button = sg.Button('Add')
window= sg.Window("My To-do List",
                  layout=[[label], [[input_box,button]]],
                  font=('Helvetica',12))
#keeping the label and the input box within the same third bracket ensures that they'll be on the same line.
#if we keep them in separate third brackets then they'll be in separate lines.

while True:
    event,action=window.read()
    print(event)
    print(action)
    match event:
        case 'Add':
            todos=functions.get_todoms()
            new_todos=action['todo'] +'\n'
            todos.append(new_todos)
            functions.write_todoms(todos)
        case sg.WIN_CLOSED:
            break
window.close()