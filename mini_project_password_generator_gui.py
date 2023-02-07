import random
import pyperclip
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import customtkinter

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


# Function that will generate our password
def generate_password(length):
    random_char = "QWERTYUIOPASDFGHJKLZXVBNMqwertyuiopasdfghjklzxcvbnm1234567890?!@#$%^&*()_+"
    password = ""
    for i in range(length):
        password += random.choice(random_char)
    return password


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.main_screen()

    def main_screen(self):
        window_width = 450
        window_height = 400
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.title('Password generator')
        self.resizable(False, False)

        menubar = tk.Menu(self)
        self.config(menu=menubar)

        help_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        help_menu.add_command(label="Help", command=lambda: tkMessageBox.showinfo(
            title="Help",
            message="This app will generate a strong password based on the length of your choice \n"
                    "\nEnter the length of your choice and click 'Generate Password'"
        ))

        menubar.add_cascade(
            label="Help",
            menu=help_menu
        )

        welcome = customtkinter.CTkLabel(self, text="Welcome to Password Generator APP", font=("Constantia", 20),
                                         corner_radius=8)
        welcome.pack(padx=20, pady=20, anchor=tk.CENTER)

        length_lbl = customtkinter.CTkLabel(self, text="Enter password length: ", corner_radius=8)
        length_lbl.pack(padx=10, pady=(5, 1), fill=tk.BOTH)

        length_entry = customtkinter.CTkEntry(self, placeholder_text="Enter password length", corner_radius=8)
        length_entry.pack(padx=10, pady=(5, 1), fill=tk.BOTH)
        length_entry.focus()

        gen_lbl = customtkinter.CTkLabel(self, text="Your generated password: ", corner_radius=8)
        gen_lbl.pack(padx=10, pady=(10, 1), fill=tk.BOTH)

        gen_entry = customtkinter.CTkEntry(self, placeholder_text="Password will be generated here", corner_radius=8)
        gen_entry.pack(padx=10, pady=(10, 1), fill=tk.BOTH)

        def generate_button_clicked():
            length = int(length_entry.get())  # gets the length from user input
            password = generate_password(length)  # calls the function that generates password
            gen_entry.delete(0, "end")
            gen_entry.insert(0, password)
            copy_button.configure(text="Copy generated password", state="normal")

        gen_button = customtkinter.CTkButton(self, text="Generate password", fg_color="#556b2f",
                                             command=generate_button_clicked, state="disabled", corner_radius=8)
        gen_button.pack(padx=10, pady=20, fill=tk.BOTH)

        # Function that will keep the button disabled until a positive integer is entered
        def enable_button(event):
            try:
                length = int(length_entry.get())
                if length > 0:
                    gen_button.configure(state="normal")
                else:
                    gen_button.configure(state="disabled")
            except ValueError:
                gen_button.configure(state="disabled")

        length_entry.bind("<KeyRelease>", enable_button)

        def copy_password():
            password = gen_entry.get()
            pyperclip.copy(password)
            copy_button.configure(text="Copied!")

        copy_button = customtkinter.CTkButton(self, text="Copy generated password", command=copy_password,
                                              state="disabled", corner_radius=8, fg_color="#556b2f")
        copy_button.pack(padx=10, pady=1, fill=tk.BOTH)


if __name__ == "__main__":
    app = App()
    app.mainloop()
