#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
import tkinter as tk
from view.router import navigate
from view.constants import background_color

def main():
    root = tk.Tk()
    root["bg"] = background_color
    canvas = tk.Canvas(root, width=9 * 50, height=14 * 50, highlightthickness=0)
    canvas.grid(columnspan=9, rowspan=14, column=0, row=0, padx=16, pady=16)
    canvas["bg"] = background_color
    logo = tk.Label(root, text="MASTERMIND", fg='grey', bg=background_color, font='Helvetica 18')
    logo.grid(columnspan=5, column=2, row=0)

    navigate(root, canvas, to='home')
    root.winfo_toplevel().title("MasterMind")
    root.mainloop()

main()
