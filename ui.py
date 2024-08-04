import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class UI:
    def __init__(self) -> None:
        self.root = tk.Tk(screenName="AI stuff")
        self.leftbar = []
        self.leftbar_el = None
        self.v_sections: dict[str, ttk.Frame] = {}
        self.sections_frame = None
        self.main_layout()
        self.var_sections()
        self.root.mainloop()

    def main_layout(self) -> None:
        self.leftbar_el = ttk.Frame(self.root, width=200, height=720)
        self.leftbar_el.pack(side=LEFT, padx=0, pady=0)
        
        self.sections_frame = ttk.Frame(self.root, width=1080, height=720)
        self.sections_frame.pack(side=LEFT, padx=0, pady=0)

        
    def var_sections(self) -> None:
        self.v_sections['Classification'] = ttk.Frame(self.sections_frame, width=1080, height=720)
        a = ttk.Label(self.v_sections['Classification'], text="Classification")
        a.pack()
        
        self.v_sections['Conv2d'] = ttk.Frame(self.sections_frame, width=1080, height=720)
        a = ttk.Label(self.v_sections['Conv2d'], text="Conv2d")
        a.pack()

        self.leftbar.append(el := ttk.Button(
            self.leftbar_el,
            text='Classification',
            bootstyle=SUCCESS,
            command=self.switch_sections('Classification')
        ))
        el.pack(side=TOP, padx=5, pady=5)
        self.leftbar.append(el := ttk.Button(
            self.leftbar_el,
            text="Conv2d",
            bootstyle=SUCCESS,
            command=self.switch_sections('Conv2d')
        ))
        el.pack(side=TOP, padx=5, pady=5)
    
    def switch_sections(self, section_name):
        def switch_func():
            for key, section in self.v_sections.items():
                if key != section_name:
                    section.pack_forget()
                else:
                    section.pack()
        return switch_func


if __name__ == '__main__':
    ui = UI()
