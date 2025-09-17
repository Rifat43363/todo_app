import functions
import FreeSimpleGUI as sg

label= sg.Text('Enter your todos')
input_box= sg.InputText(key='todo')
button1= sg.Button('add')
button2= sg.Button('edit')

list= sg.Listbox(values=functions.get_todoms(), key='todos', enable_events=True,size=(50,5))

window= sg.Window('Watashino Todos Desu',
                  layout=[[label],[input_box, button1],
                          [list,button2]],
                  font=['Helvetica', 12, 'bold'])
while True:
    event,value = window.read()
    print(event)
    print(value)
    match event:
        case 'add':
            todos = functions.get_todoms()
            new_todo = value['todo'] +'\n'
            todos.append(new_todo)
            functions.write_todoms(todos)
            window['todos'].update(values=todos)
        case 'edit':
            new_todo = value['todo']
            todo_to_edit=value['todos'][0]
            todos=functions.get_todoms()
            index= todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todoms(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break
            #if us used exit() instead of break then the below print function wouldnt be used as the program would/
            # directly instead to just breaking the loop
print('sayonara')
window.close()