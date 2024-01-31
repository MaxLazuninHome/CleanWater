import tkinter as tk


class ToolTip(object):
    def __init__(self,  widget, obj):
        self.value = obj['value']
        self.widget = widget
        self.min_value = obj['min_value']
        self.max_value = obj['max_value']
        self.text = f'Введите значение от {self.min_value} до {self.max_value}'
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.create_tooltip_event()

    def create_tooltip_event(self):
        self.widget.bind('<Enter>', self.show_tip)
        self.widget.bind('<Leave>', self.hide_tip)

    def show_tip(self, event):
        "Display text in tooltip window"
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # Создание всплывающего окна с подсказкой
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


# Функция создания Entry виджета с подсказкой
# def create_entry_with_tooltip(parent, tooltip_text):
#     entry = tk.Entry(parent)
#     entry.pack()
#     ToolTip(entry, tooltip_text)
#     return entry

# # Пример использования
# root = tk.Tk()
# entry_with_tooltip = create_entry_with_tooltip(root, {'value': 5, 'min_value': 1, 'max_value': 10})
# root.mainloop()