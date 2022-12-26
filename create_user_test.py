
import tkinter
import tkinter.messagebox
from tkinter.ttk import *
import sqlite3


class CreateUserGUI:
    def __init__(self):

        # create main window
        self.root = tkinter.Tk()

        # set window size
        self.root.geometry('500x220+100+100')

        # display title
        self.root.title('Main Test Window')

        # lines
        tkinter.ttk.Separator(self.root, orient='vertical').grid(column=2, row=0, rowspan=10, sticky='nsw', padx=0)

        # labels
        title_label = tkinter.Label(self.root, text='Enter the following information: ')
        title_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

        first_name_label = tkinter.Label(self.root, text='Enter First Name: ')
        first_name_label.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

        last_name_label = tkinter.Label(self.root, text='Enter Last Name: ')
        last_name_label.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)

        age_label = tkinter.Label(self.root, text='Enter Age (yrs): ')
        age_label.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady=5)

        weight_label = tkinter.Label(self.root, text='Enter Weight (lbs): ')
        weight_label.grid(column=0, row=4, sticky=tkinter.W, padx=10, pady=5)

        # entries
        self.first_name_entry = tkinter.Entry(self.root)
        self.first_name_entry.grid(column=1, row=1, sticky=tkinter.W, padx=10, pady=0)

        self.last_name_entry = tkinter.Entry(self.root)
        self.last_name_entry.grid(column=1, row=2, sticky=tkinter.W, padx=10, pady=0)

        self.age_entry = tkinter.Entry(self.root)
        self.age_entry.grid(column=1, row=3, sticky=tkinter.W, padx=10, pady=0)

        self.weight_entry = tkinter.Entry(self.root)
        self.weight_entry.grid(column=1, row=4, sticky=tkinter.W, padx=10, pady=0)

        # buttons
        create_user_button = tkinter.Button(text='Create User', command=self.add_user)
        create_user_button.grid(column=1, row=5, sticky=tkinter.E, padx=10, pady=10)

        cancel_button = tkinter.Button(text='Cancel')
        cancel_button.grid(column=1, row=5, sticky=tkinter.W, padx=10, pady=10)

        quit_button = tkinter.Button(text='Quit', command=self.root.destroy)
        quit_button.grid(column=2, row=5, padx=20, pady=10)

        # enter main loop
        tkinter.mainloop()

    def add_user(self):
        try:
            conn = None
            # connect to the database
            conn = sqlite3.connect('sodium.db')

            # get a database cursor
            cur = conn.cursor()

            # creates new entry
            cur.execute('''INSERT INTO User (first_name, last_name, age, weight)
                                VALUES (?, ?, ?, ?)''', (self.first_name_entry.get(), self.last_name_entry.get(),
                                                            self.age_entry.get(), self.weight_entry.get()))
            # commit changes
            conn.commit()
            tkinter.messagebox.showinfo('Success!', 'The user has been added.')

        except sqlite3.IntegrityError:
            tkinter.messagebox.showinfo('ERROR', 'Error. That first name has been used, please use a unique one.')

        except sqlite3.OperationalError:
            tkinter.messagebox.showinfo('ERROR', 'Error. Please try again.')

        finally:
            self.root.destroy()


if __name__ == '__main__':
    test = CreateUserGUI()
