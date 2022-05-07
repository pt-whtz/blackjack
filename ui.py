from tkinter import *
from tkinter import messagebox

BUTTON_COL = "#83BD75"
BUTTON_FONT = ("Courier", 14)


class Interface:
    
    def __init__(self):

        # main window
        self.window = Tk()
        self.window.title("Blackjack")
        self.window.configure(bg="black")
        self.window.wm_resizable(height=False, width=False)

        self.canvas = Canvas(width=630, height=356, bd=0, highlightthickness=0)
        self.bg_image = PhotoImage(file="images/casino-table.png")
        self.canvas.create_image(315, 178, image=self.bg_image)
        self.canvas.grid(row=0, column=0)

        # menu attributes
        self.logo_image = PhotoImage(file="images/logo.png")

        self.new_game_button = Button(self.window, width=20, font=BUTTON_FONT, bg=BUTTON_COL, text="New Game",
                                      activebackground='green', command=self.new_game)
        self.stats_button = Button(self.window, width=20, font=BUTTON_FONT, bg=BUTTON_COL, text="Statistics",
                                      activebackground='green', command=self.show_stats)
        self.exit_button = Button(self.window, width=20, font=BUTTON_FONT, bg=BUTTON_COL, text="Exit",
                                      activebackground='green', command=self.game_exit)
        self.back_button = Button(self.window, text="Back", width=20, bd=0, font=BUTTON_FONT, bg=BUTTON_COL)

        self.main_menu_init()

        self.window.iconbitmap("images/icon.ico")
        self.window.mainloop()

    def main_menu_init(self):
        self.logo = self.canvas.create_image(315, 90, image=self.logo_image)
        self.new_game_but = self.canvas.create_window(315, 200, window=self.new_game_button)
        self.stats_but = self.canvas.create_window(315, 240, window=self.stats_button)
        self.exit_but = self.canvas.create_window(315, 280, window=self.exit_button)

    def show_stats(self):
        messagebox.showwarning("Warning", "Coming soon!")

    def new_game(self):
        self.canvas.delete(self.logo, self.new_game_but, self.stats_but, self.exit_but)
        # messagebox.showwarning("Warning", "Coming soon!")

    def game_exit(self):
        if messagebox.askyesno("Exit", "Do you want to exit?"):
            self.window.destroy()