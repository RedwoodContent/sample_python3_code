#__author__ == 'amanda'

# A first use of TK graphics by creating a simple button

from tkinter import *
from tkinter import ttk

def main():
    print("The Main function started", end='\n')

    # initiate the TK graphics package
    root = Tk()

    # Create the button object
    button = ttk.Button(root, text='Click Me')

    # put button object in the display set
    button.pack()

    # flush any leftover tasks
    button.update_idletasks()

    # Enter the dispatch loop AND display graphics set
    root.mainloop()


if __name__ == "__main__":
    main()
