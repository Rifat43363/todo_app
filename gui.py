import functions
import FreeSimpleGUI as sg

label= sg.Text('Type in a todo')
#this will stay at the left of the empty box and explain what to enter
input_box= sg.InputText(tooltip='Write Todo')
button = sg.Button('Add')
window= sg.Window("My To-do List", layout=[[label], [input_box, button]])
#keeping the label and the input box within the same third bracket ensures that they'll be on the same line.
#if we keep them in separate third brackets then they'll be in separate lines.
window.read()
window.close()