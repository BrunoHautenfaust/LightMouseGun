import PySimpleGUI as sg

class GUI:
    def __init__(self, title):
        self.buttonColor = '#000'
        self.buttonBGColor = '#F5F5F5'
        self.elSize = (213, 156)
        sg.SetOptions(icon='favicon', font=('default', 10), button_color=(self.buttonColor, self.buttonBGColor))
        self.window = self.__build_UI(title)
        self.print = sg.EasyPrint

    def __build_UI(self, title):
        layout = [
            [sg.Frame('Position', [
                 [sg.Button('◤', key='top_left'), sg.Button('▲', key='top_center'), sg.Button('◥', key='top_right')],
                 [sg.Button('◀', key='middle_left'), sg.Button('◆', key='middle_center'), sg.Button('▶', key='middle_right')],
                 [sg.Button('◣', key='bottom_left'), sg.Button('▼', key='bottom_center'), sg.Button('◢', key='bottom_right')],
                 [sg.Text('')],
                 [sg.Text('')],
                 [sg.Button('Start', key='START'), sg.Text(''), sg.Button('Stop', key='STOP', disabled=True)]
                ], key='pos_frame'),
             sg.Frame('Preview', [
                 [sg.Image(filename='', size=self.elSize, key='OUTPUT')],
                 [sg.Text(' ' * 10), sg.Button('Preview', key='PREVIEW', disabled=True, auto_size_button=False)]
                ])
            ]
        ]
        window = sg.Window(title).Layout(layout)
        window.Finalize()
        return window

    def enable(self, button):
        self.window.Element(button).Update(disabled=False)
        return self

    def disable(self, button):
        self.window.Element(button).Update(disabled=True)
        return self

