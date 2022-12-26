
import tkinter
import tkinter.messagebox
from tkinter.ttk import *
import sqlite3


class CreateFoodGUI:
    def __init__(self):
        # create main window
        self.root = tkinter.Tk()

        # set window size
        self.root.geometry('500x325+100+100')

        # display title
        self.root.title('Main Test Window')

        # lines
        tkinter.ttk.Separator(self.root, orient='vertical').grid(column=2, row=0, rowspan=10, sticky='nsw', padx=0)

        # labels

        # food log section
        title_label = tkinter.Label(self.root, text='Enter the following information: ')
        title_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

        food_name_label = tkinter.Label(self.root, text='Enter Food Name: ')
        food_name_label.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

        sodium_label = tkinter.Label(self.root, text='Enter Sodium Amount (mg): ')
        sodium_label.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)

        carb_label = tkinter.Label(self.root, text='Enter Total Carb Amount (g): ')
        carb_label.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady=5)

        fat_label = tkinter.Label(self.root, text='Enter Total Fat Amount (g): ')
        fat_label.grid(column=0, row=4, sticky=tkinter.W, padx=10, pady=5)

        protein_label = tkinter.Label(self.root, text='Enter Protein Amount (g): ')
        protein_label.grid(column=0, row=5, sticky=tkinter.W, padx=10, pady=5)

        calorie_label = tkinter.Label(self.root, text='Enter Caloric Amount: ')
        calorie_label.grid(column=0, row=6, sticky=tkinter.W, padx=10, pady=5)

        # entries
        self.food_name_entry = tkinter.Entry(self.root)
        self.food_name_entry.grid(column=1, row=1, sticky=tkinter.W, padx=10, pady=0)

        self.sodium_entry = tkinter.Entry(self.root)
        self.sodium_entry.grid(column=1, row=2, sticky=tkinter.W, padx=10, pady=0)

        self.carb_entry = tkinter.Entry(self.root)
        self.carb_entry.grid(column=1, row=3, sticky=tkinter.W, padx=10, pady=0)

        self.fat_entry = tkinter.Entry(self.root)
        self.fat_entry.grid(column=1, row=4, sticky=tkinter.W, padx=10, pady=0)

        self.protein_entry = tkinter.Entry(self.root)
        self.protein_entry.grid(column=1, row=5, sticky=tkinter.W, padx=10, pady=0)

        self.calorie_entry = tkinter.Entry(self.root)
        self.calorie_entry.grid(column=1, row=6, sticky=tkinter.W, padx=10, pady=0)

        # create buttons
        create_food_button = tkinter.Button(text='Create Food', command=self.add_food)
        create_food_button.grid(column=1, row=7, sticky=tkinter.E, padx=10, pady=10)

        cancel_button = tkinter.Button(text='Cancel')
        cancel_button.grid(column=1, row=7, sticky=tkinter.W, padx=10, pady=10)

        quit_button = tkinter.Button(text='Quit', command=self.root.destroy)
        quit_button.grid(column=2, row=9, padx=20, pady=10)

        # enter main loop
        tkinter.mainloop()

    def add_food(self):
        try:
            conn = None
            # connect to the database
            conn = sqlite3.connect('sodium.db')

            # get a database cursor
            cur = conn.cursor()

            # creates new entry
            cur.execute('''INSERT INTO Food (food_name, sodium_amt, carb_amt, fat_amt, calorie_amt, protein_amt)
                                VALUES (?, ?, ?, ?, ?, ?)''', (self.food_name_entry.get(), self.sodium_entry.get(),
                                                               self.carb_entry.get(), self.fat_entry.get(),
                                                               self.calorie_entry.get(), self.protein_entry.get()))
            # commit changes
            conn.commit()
            tkinter.messagebox.showinfo('Success!', 'The food item has been added.')

        except sqlite3.IntegrityError:
            tkinter.messagebox.showinfo('ERROR', 'Error. That food name has been used, please use a unique one.')

        except sqlite3.OperationalError:
            tkinter.messagebox.showinfo('ERROR', 'Error. Please try again.')

        finally:
            self.root.destroy()


if __name__ == '__main__':
    test = CreateFoodGUI()
