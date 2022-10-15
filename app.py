import PySimpleGUI as sg

layout = [
    [sg.Text('User')],
    [sg.Input(key='user')],
    [sg.Text('Password')],
    [sg.Input(key='pass')],
    [],
    [sg.Button('Login'),sg.Button('Back')],
    [],
    [sg.Text('',key='mensage')],
]

window = sg.Window('Login Screen',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        pass_corret = '123456'
        user_write = 'luis'
        user = values['user']
        password = values['pass'] 
        if password == pass_corret and user == user_write:
            window['mensage'].update('Login successfully')
        else:
            window['mensage'].update('Incorrect password or username')
    elif event == 'Back':
        window['mensage'].update('Incorrect, not back yet!')