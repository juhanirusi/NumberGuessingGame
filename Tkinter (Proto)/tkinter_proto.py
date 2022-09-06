from tkinter import *

# Python Logo Colors
LIGHT_BLUE = '#4B8BBE'
DARK_BLUE = '#306998'

LIGHT_YELLOW = '#FFE873'
DARK_YELLOW = '#FFD43B'

GRAY = '#646464'
WHITE = '#ffffff'


class StartGame:
    def __init__(self, window):
        self.window = window
        self.label = Label(text="Do you want to play the game? 'yes' or 'no'?", bg=LIGHT_BLUE, fg=WHITE, font=("Courier", 24)).place(relx=0.5, rely=0.1, anchor=CENTER)
        self.entry = Entry(window, width=20, font=('Arial', 24)).place(relx=0.5, rely=0.4, anchor=CENTER)
        self.button = Button(text="SUBMIT", command=self.change_window_color).place(relx=0.5, rely=0.6, anchor=CENTER)

    def change_window_color(self):
        window.config(bg=DARK_YELLOW)


def center_window_on_screen(width=1100, height=650):
    screen_width = window.winfo_screenwidth() # Get screen width
    screen_height = window.winfo_screenheight() # Get screen height

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # The first two parameters are the width and height of the window.
    # The last two parameters are x and y screen coordinates.
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


if __name__ == "__main__":
    window = Tk()
    window.title('Number Guessing Game')
    window.config(bg=LIGHT_BLUE)

    center_window_on_screen()

    StartGame(window)
    window.mainloop()


# class tkinterApp(tk.Tk):

#     # __init__ function for class tkinterApp
#     def __init__(self, *args, **kwargs):

#         # __init__ function for class Tk
#         tk.Tk.__init__(self, *args, **kwargs)

#         # creating a container
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)

#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         # initializing frames to an empty array
#         self.frames = {}

#         # iterating through a tuple consisting
#         # of the different page layouts
#         for F in (StartPage, Page1, Page2):

#             frame = F(container, self)

#             # initializing frame of that object from
#             # startpage, page1, page2 respectively with
#             # for loop
#             self.frames[F] = frame

#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame(StartPage)

#     # to display the current frame passed as
#     # parameter
#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()

# # first window frame startpage


# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

#         # label of frame Layout 2
#         label = ttk.Label(self, text="Startpage", font=LARGEFONT)

#         # putting the grid in its place by using
#         # grid
#         label.grid(row=0, column=4, padx=10, pady=10)

#         button1 = ttk.Button(self, text="Page 1",
#                              command=lambda: controller.show_frame(Page1))

#         # putting the button in its place by
#         # using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)

#         # button to show frame 2 with text layout2
#         button2 = ttk.Button(self, text="Page 2",
#                              command=lambda: controller.show_frame(Page2))

#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)


# # second window frame page1
# class Page1(tk.Frame):

#     def __init__(self, parent, controller):

#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Page 1", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)

#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text="StartPage",
#                              command=lambda: controller.show_frame(StartPage))

#         # putting the button in its place
#         # by using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)

#         # button to show frame 2 with text
#         # layout2
#         button2 = ttk.Button(self, text="Page 2",
#                              command=lambda: controller.show_frame(Page2))

#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)


# # third window frame page2
# class Page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Page 2", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)

#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text="Page 1",
#                              command=lambda: controller.show_frame(Page1))

#         # putting the button in its place by
#         # using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)

#         # button to show frame 3 with text
#         # layout3
#         button2 = ttk.Button(self, text="Startpage",
#                              command=lambda: controller.show_frame(StartPage))

#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)


# # Driver Code
# app = tkinterApp()
# app.mainloop()
