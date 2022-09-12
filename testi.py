import random
from tkinter import *

# Python Logo Colors
LIGHT_BLUE = '#4B8BBE'
DARK_BLUE = '#306998'

LIGHT_YELLOW = '#FFE873'
DARK_YELLOW = '#FFD43B'

GRAY = '#646464'
WHITE = '#ffffff'


class Start(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Number Guessing Game")

        # creating a frame and assigning it to container
        container = Frame(self)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (PlayGame, SidePage):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(PlayGame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class PlayGame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=LIGHT_BLUE)

        self.label = Label(text="Do you want to play the game? 'yes' or 'no'?", bg=LIGHT_BLUE, fg=WHITE, font=("Courier", 24)).place(relx=0.5, rely=0.1, anchor=CENTER)

        self.user_input_text = Entry(width=20, font=('Arial', 24))
        self.user_input_text.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.button = Button(text="SUBMIT", command=self.user_input).place(relx=0.5, rely=0.6, anchor=CENTER)


    def user_input(self):
        text = self.user_input_text.get()
        if text in ('y', 'yup', 'yes', 'yeah'):
            self.answer = random.randint(1, 100)
            print("The correct answer is --> ", self.answer)  # TODO DELETE LATER!
            #self.guesses_left = set_difficulty.difficulty_level()
            print("Ok, the computer challenges you to guess a number between 1 and 100...")
            #self.guess_number()
            self.frame.destroy()
        elif text in ('n', 'no', 'nope', 'no way'):
            print("Okay, I understand, see you next time.")
        else:
            print("Your input was confusing, I assume you don't want to play then.")

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = Button(self, text="Go to the Side Page", command=lambda: self.controller.show_frame(SidePage),)
        switch_window_button.pack(side="bottom", fill=X)


class SidePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(PlayGame),
        )
        switch_window_button.pack(side="bottom", fill=X)


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
    window = Start()
    center_window_on_screen()
    window.mainloop()
