from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter_example.tkinter102 import MyGui


class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Ouch!')
        # наследует метод __init__ и замещает метод reply

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()
