import functions
import time
now= time.strftime("%d,%B,%Y-- %H:%M:%S")
print(now)


while True:
    user_prompt=input('do you wanna add, show, complete, replace or exit?: ')
    user_prompt=user_prompt.lower()
    if user_prompt.startswith('add'):
        todo= ' '.join(user_prompt.split()[1:])
        todos= functions.get_todoms('todoms.txt')
        todos.append('\n' + todo)
        functions.write_todoms('todoms.txt', todos)
    elif user_prompt.startswith('show'):
        todos= functions.get_todoms('todoms.txt')
        for index,todo in enumerate(todos):
            todo=todo.strip('\n')
            print(f'{index+1}.{todo.capitalize()}')
    elif user_prompt.startswith('complete') or user_prompt.startswith('remove'):
        todos= functions.get_todoms('todoms.txt')
        number = int(user_prompt.split()[1])
        if 1<=number<=len(todos):
            todos.pop(number-1)
            functions.write_todoms( todos,'todoms.txt')
        else:
            print('no such number')
    elif user_prompt.startswith('replace'):
        try:
            number = int(user_prompt.split()[1])
            todos= functions.get_todoms('todoms.txt')
            replacement = input(' what do you want to replace it with?: ')
            todos[number-1]=replacement +'\n'
            functions.write_todoms('todoms.txt', todos)
            print('replaced successfully')
        except IndexError:
               print('Wrong input of number')

    elif user_prompt.startswith('exit'):
        print('exiting')
        break
    else:
        print('bro tumi to vul likhso')
print('bye')