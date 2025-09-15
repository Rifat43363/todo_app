import FreeSimpleGUI as sg

label1=sg.Text('choose your file to compress')
input1=sg.Input(tooltip='Choose your File')
button1=sg.FilesBrowse('Choose File')

label2=sg.Text('choose your Destination folder')
input2=sg.Input(tooltip='Choose Folder')
Button2=sg.FolderBrowse('Choose Folder')
Compress=sg.Button('Compress')

window= sg.Window("Watashino Compressor", layout=[[label1, input1,button1], [label2, input2,Button2], [Compress]])
window.read()
window.close()