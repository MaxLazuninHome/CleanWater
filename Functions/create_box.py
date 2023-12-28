from tkinter import *

def create_box():
    root = Tk()
    root.title('Главное окно')
    root.update_idletasks()
    s = root.geometry()
    s = s.split('+')
    s = s[0].split('x')
    width_root = int(s[0])
    height_root = int(s[1])

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - width_root // 2
    h = h - height_root // 2
    root.geometry('1550x750+200+100'.format(w, h))
    inside_left_frame = Frame()
    inside_right_frame = Frame()
    inside_left_frame.pack(side='left', anchor='n', padx=20, fill='both', expand=True)
    inside_right_frame.pack(side='left', anchor='n', fill='both', expand=True)
    return root, inside_left_frame, inside_right_frame
