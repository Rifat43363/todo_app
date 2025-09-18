import FreeSimpleGUI as sg
import zipfunctions
label1=sg.Text('choose your file to compress')
input1=sg.Input(tooltip='Choose your File')
button1=sg.FilesBrowse('Choose File')

label2=sg.Text('choose your Destination folder')
input2=sg.Input(tooltip='Choose Folder')
Button2=sg.FolderBrowse('Choose Folder')
Compress=sg.Button('Compress')
label3=sg.Text(key='result')
window= sg.Window("Watashino Compressor",
                  layout=[[label1, input1,button1],
                          [label2, input2,Button2],
                          [Compress,label3]])
while True:
    event, value = window.read()
    match event:
        case 'Compress':
            print(event)
            print(value)
            filepaths= value['Choose File'].split(';')
            folder= value['Choose Folder']
            zipfunctions.make_zip(filepaths,folder)
            window['result'].update(value='compression done')
        case sg.WIN_CLOSED:
            exit()
window.close()